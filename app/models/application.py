from app.extensions import db
from datetime import datetime

class Application(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # 'approved', 'rejected'  or 'applied'
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)

    member = db.relationship('Member', back_populates='applications')
    job = db.relationship('Job', back_populates='applications')
    
    def to_dict(self):
        """Convert Application instance to dictionary."""
        return {
            'id': self.id,
            'member_id': self.member_id,
            'job_id': self.job_id,
            'status': self.status,
            'applied_at': self.applied_at.isoformat() if self.applied_at else None,
            'member': self.member.to_dict() if self.member else None,  # Assuming Member has a to_dict method
            'job': self.job.to_dict() if self.job else None  # Assuming Job has a to_dict method
        }