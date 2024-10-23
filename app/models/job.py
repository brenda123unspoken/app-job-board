from app.extensions import db
from datetime import datetime
from app.models.employer import Employer

from app.models.saved_jobs import saved_jobs


class Job(db.Model):
    __tablename__ = 'jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    salary = db.Column(db.Float, nullable=True)  # Float for salary handling
    deadline = db.Column(db.DateTime, nullable=False)
    
    # Relationship with Employer
    employer_id = db.Column(db.Integer, db.ForeignKey('employers.id'), nullable=False)
    employer = db.relationship('Employer', back_populates='jobs')  # Define relationship with Employer
    # Define relationship to JobView
    job_views = db.relationship('JobView', back_populates='job')
    applications = db.relationship('Application', back_populates='job')
    saved_by = db.relationship('Member', secondary=saved_jobs, lazy='dynamic', back_populates='saved_jobs')
    
    
    # Timestamp fields
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Set on creation
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Updated on modification

    def to_dict(self):
        """Convert Job model to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "salary": self.salary,
            "deadline": self.deadline.isoformat() if self.deadline else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "employer_id": self.employer_id,
            # Safely handle the employer relationship in case it's not loaded
            "employer_name": self.employer.company_name if self.employer else None,
            "saved_by": [member.id for member in self.saved_by],  # Include saved_by member IDs
        }
