from app.extensions import db
import bcrypt
from datetime import datetime

from app.models.saved_jobs import saved_jobs



class Member(db.Model):
    __tablename__ = 'member'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False, default="member")
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)  # Soft delete field

    # Define relationship to JobView
    job_views = db.relationship('JobView', back_populates='member')
    applications = db.relationship('Application', back_populates='member')
    saved_jobs = db.relationship('Job', secondary=saved_jobs, lazy='dynamic', back_populates='saved_by')

    
    
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "role": self.role,
            "is_active": self.is_active, 
            "saved_jobs": [job.to_dict() for job in self.saved_jobs]  # Assuming Job has a to_dict method
        
        }

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    @classmethod
    def get_all_roles(cls):
        return ["member", "admin", "supervisor"]

    def assign_role(self, new_role):
        if new_role in self.get_all_roles():
            self.role = new_role
            db.session.commit()
            return True
        return False

    @classmethod
    def change_role(cls, member_id, new_role):
        member = cls.query.get(member_id)
        if member and new_role in cls.get_all_roles():
            member.role = new_role
            db.session.commit()
            return True
        return False

    def soft_delete(self):
        self.is_active = False
        db.session.commit()

    def restore(self):
        self.is_active = True
        db.session.commit()

    def save_job(self, job):
        """Add a job to the saved jobs."""
        if job not in self.saved_jobs:
            self.saved_jobs.append(job)
            db.session.commit()  # Commit the transaction after modifying the relationship

    def unsave_job(self, job):
        """Remove a job from the saved jobs."""
        if job in self.saved_jobs:
            self.saved_jobs.remove(job)
            db.session.commit()     
