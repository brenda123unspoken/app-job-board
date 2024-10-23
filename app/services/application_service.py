# from app.models.application import Application
# from app import db
# from app.websocket.socketio import notify_application_status
# from app.utils.email_utils import send_application_status_email
# from app.repositories.application_repository import ApplicationRepository


# class ApplicationService:
#     @staticmethod
#     def create_application(member_id, job_id, status):
#         """Create a new application with an initial status."""
#         initial_status = 'applied'
#         return ApplicationRepository.create_application(member_id, job_id, initial_status)

# @staticmethod
#     def update_application_status(application_id, new_status):
#         # Fetch the application by ID
#         application = Application.query.get(application_id)
#         if application:
#             # Update the application status
#             application.status = new_status
#             db.session.commit()

#             # Notify the member about the application status via WebSocket
#             notify_application_status(application.member_id, new_status)

#             # Send email notification
#             send_application_status_email(application.member.email, application.job.title, new_status)


# class ApplicationService:
#     @staticmethod
#     def create_application(member_id, job_id, status):
#         """Create a new application with an initial status."""
#         initial_status = 'applied'
#         return ApplicationRepository.create_application(member_id, job_id, initial_status)

# @staticmethod
#     def update_application_status(application_id, new_status):
#         # Fetch the application by ID
#         application = Application.query.get(application_id)
#         if application:
#             # Update the application status
#             application.status = new_status
#             db.session.commit()

#             # Notify the member about the application status via WebSocket
#             notify_application_status(application.member_id, new_status)

#             # Send email notification
#             send_application_status_email(application.member.email, application.job.title, new_status)
from app.models.application import Application
from app import db
from app.websocket.socketio import notify_application_status
from app.utils.email_utils import send_application_status_email
from app.repositories.application_repository import ApplicationRepository


class ApplicationService:
    @staticmethod
    def create_application(member_id, job_id, status):
        """Create a new application with an initial status."""
        return ApplicationRepository.create_application(member_id, job_id, status)
    

    @staticmethod
    def update_application(application_id, data):
        """Update an existing application."""
        # Fetch the application by ID
        application = ApplicationRepository.get_application_by_id(application_id)
        if not application:
            return None  # Return None if the application is not found

        # Update application fields based on the provided data
        if 'status' in data:
            application.status = data['status']

        # You can add other fields here like resume, cover letter, etc.
        # if 'resume' in data:
        #     application.resume = data['resume']

        # Commit the changes to the application
        ApplicationRepository.update_application(application)

        # Notify the member about the application update via WebSocket (optional)
        notify_application_status(application.member_id, application.status)

        # Send email notification to the member (optional)
        send_application_status_email(application.member.email, application.job.title, application.status)

        return application


    @staticmethod
    def update_application_status(application_id, new_status, employer_id=None):
        """Update the application status, with optional employer authorization for approval/rejection."""
        application = ApplicationRepository.get_application_by_id(application_id)
        if not application:
            return {"error": "Application not found."}, 404

        # If employer action, ensure only employers can approve/reject
        if employer_id:
            # Here, you could add logic to verify that the employer has the right to approve/reject
            application.status = new_status
        else:
            # Regular member updates (not status change)
            application.status = new_status

        # Commit the changes to the application
        ApplicationRepository.update_application(application)

        # Notify the member about the application status via WebSocket
        notify_application_status(application.member_id, new_status)

        # Send email notification to the member
        send_application_status_email(application.member.email, application.job.title, new_status)

        return {"message": f"Application status updated to {new_status} successfully."}, 200
    
    @staticmethod
    def get_application_by_id(application_id):
        """Fetch an application by ID."""
        return ApplicationRepository.get_application_by_id(application_id)