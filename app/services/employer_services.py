from app.models.employer import Employer
from app.repositories.employer_repository import EmployerRepository

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
            phone_number=data.get('phone_number'),
            about=data.get('about'),
            identifier=identifier  # Store the unique identifier for the employer
        )
        return EmployerRepository.save(new_employer)

    @staticmethod
    def update_employer(employer_id, data):
        """Update an employer's details."""
        employer = EmployerRepository.find_by_id(employer_id)
        if not employer:
            return None
        employer.company_name = data.get('company_name', employer.company_name)
        employer.email = data.get('email', employer.email)
        employer.phone_number = data.get('phone_number', employer.phone_number)
        employer.about = data.get('about', employer.about)

        return EmployerRepository.save(employer)
