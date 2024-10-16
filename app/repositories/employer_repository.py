
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
