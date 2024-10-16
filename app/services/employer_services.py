from app.models.employer import Employer
from app.repositories.employer_repository import EmployerRepository
from app import db

class EmployerService:
    @staticmethod
    def get_employer_by_unique_identifier(identifier):
        """Retrieve the employer based on a unique identifier like email, username, etc."""
        return EmployerRepository.find_by_identifier(identifier)

    @staticmethod
    def register_employer(data, identifier):
        """Create a new employer based on the data and identifier."""
        new_employer = Employer(
            company_name=data.get('company_name'),
            email=data.get('email'),
            phone=data.get('phone'),
            about=data.get('about'),
            identifier=identifier, # Store the unique identifier for the employer
            password=data.get('password') 
        )

        new_employer.set_password(data['password']) 
        return EmployerRepository.save(new_employer)

    @staticmethod
    def update_employer(employer_id, data):
        """Update an employer's details."""
        employer = EmployerRepository.find_by_id(employer_id)
        if not employer:
            return None
        employer.company_name = data.get('company_name', employer.company_name)
        employer.email = data.get('email', employer.email)
        employer.phone = data.get('phone', employer.phone)
        employer.about = data.get('about', employer.about)

        return EmployerRepository.save(employer)

    @staticmethod
    def create_employer(data):
        required_fields = ['company_name', 'email', 'phone', 'about', 'password']
        for field in required_fields:
            if field not in data or not data[field]:
                return {"error": f"'{field}' is required"}, 400

        if EmployerRepository.find_by_email_or_phone(data['email'], data['phone']):
            return {"error": "Email or Phone already exists"}, 400

        try:
            employer = Employer(
                company_name=data['company_name'],
                email=data['email'],
                phone=data['phone'],
                about=data['about'],
                password=data['password']
            )
            employer.set_password(data['password'])

            EmployerRepository.create_employer(employer)
            return employer.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    @staticmethod
    def get_all_employers():
        employers = EmployerRepository.get_all_employers()
        return [employer.to_dict() for employer in employers], 200

    @staticmethod
    def get_employer_by_id(id):
        employer = EmployerRepository.get_employer_by_id(id)
        if not employer:
            return {"error": "Employer not found"}, 404
        return employer.to_dict(), 200
    
    