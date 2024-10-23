from app import db
from app.models.job_views import JobView

class JobViewRepository:
    @staticmethod
    def create_job_view(member_id, job_id):
        job_view = JobView(member_id=member_id, job_id=job_id)
        db.session.add(job_view)
        db.session.commit()
        return job_view

    @staticmethod
    def get_job_views_by_member(member_id):
        return JobView.query.filter_by(member_id=member_id).all()

    @staticmethod
    def get_job_views_by_job(job_id):
        return JobView.query.filter_by(job_id=job_id).all()

    
    @staticmethod
    def get_all():
        return db.session.query(JobView).all()  # Use SQLAlchemy's query interface
