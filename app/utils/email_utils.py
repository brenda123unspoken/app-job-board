from flask_mail import Message
from app import mail

def send_application_status_email(member_email, job_title, status):
    msg = Message(
        subject=f"Your Application Status for '{job_title}'",
        recipients=[member_email],
        body=(
            f"Dear Applicant,\n\n"
            f"Your application for '{job_title}' has been {status}.\n\n"
            "Thank you for your interest!\n"
            "Best regards,\n"
            "The Job Board Team"
        ),
    )
    mail.send(msg)
