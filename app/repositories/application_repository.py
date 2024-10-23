from app import db
from app.models.application import Application

class ApplicationRepository:
    @staticmethod
    def create_application(member_id, job_id, status):
        application = Application(member_id=member_id, job_id=job_id, status=status)
        db.session.add(application)
        db.session.commit()
        return application

    @staticmethod
    def update_application(application):
        db.session.commit()

    @staticmethod
    def get_application_by_id(application_id):
        return Application.query.get(application_id)
