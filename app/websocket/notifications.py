# app/services/notifications.py
from app.utils.email_utils import send_application_status_email  # Ensure you have this utility defined
from app.websocket.socketio import notify_members_on_update, notify_members_on_delete

class NotificationService:
    @staticmethod
    def notify_on_job_update(job_id):
        notify_members_on_update(job_id)

    @staticmethod
    def notify_on_job_delete(job_id):
        notify_members_on_delete(job_id)

    @staticmethod
    def notify_on_application_status(member_email, job_title, status):
        # Notify via Email
        send_application_status_email(member_email, job_title, status)
