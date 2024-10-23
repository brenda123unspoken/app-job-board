from app.extensions import db
from datetime import datetime

class JobView(db.Model):
    __tablename__ = 'job_views'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    viewed_at = db.Column(db.DateTime, default=datetime.utcnow)

    member = db.relationship('Member', back_populates='job_views')
    job = db.relationship('Job', back_populates='job_views')
    
    def to_dict(self):
        """Convert the JobView instance to a dictionary."""
        return {
            'id': self.id,
            'member_id': self.member_id,
            'job_id': self.job_id,
            'viewed_at': self.viewed_at.isoformat(),  # Convert datetime to string
            'member': self.member.to_dict() if self.member else None,  # Serialize member data if needed
            'job': self.job.to_dict() if self.job else None  # Serialize job data if needed
        }
