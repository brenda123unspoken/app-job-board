
from app.models.employer import Employer
from app import db

class EmployerRepository:
    @staticmethod
    def find_by_identifier(identifier):
        """Find an employer by a unique identifier like email or username."""
        return Employer.query.filter((Employer.email == identifier) | (Employer.identifier == identifier)).first()

    @staticmethod
    def find_by_id(employer_id):
        """Find an employer by their ID."""
        return Employer.query.get(employer_id)

    @staticmethod
    def save(employer):
        """Save an employer to the database."""
        db.session.add(employer)
        db.session.commit()
        return employer
    
    @staticmethod
    def create_employer(employer):
        db.session.add(employer)
        db.session.commit()

    @staticmethod
    def get_all_employers():
        return Employer.query.all()

    @staticmethod
    def get_employer_by_id(id):
        return Employer.query.get(id)

    @staticmethod
    def update_employer():
        db.session.commit()

    @staticmethod
    def find_by_email_or_phone(email, phone):
        return Employer.query.filter((Employer.email == email) | (Employer.phone == phone)).first()
