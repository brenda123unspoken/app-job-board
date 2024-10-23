from faker import Faker
from app import create_app, db
from app.models.member import Member
from app.models.employer import Employer
from app.models.job import Job
from datetime import datetime, timedelta
from app.models.job_views import JobView  # Import JobView model
from app.models.application import Application  # Import Application model
from app.models.saved_jobs import saved_jobs
from datetime import datetime, timedelta

fake = Faker()

def seed_members(count=10):
    """Seeds the database with fake Member data."""
    for _ in range(count):
        member_data = {
            'name': fake.name(),
            'phone': fake.phone_number(),
            'email': fake.email(),
            'role': fake.random_element(elements=("member", "admin", "supervisor")),
            'is_active': True
        }
        if Member.query.filter_by(email=member_data['email']).first() or Member.query.filter_by(phone=member_data['phone']).first():
            continue  # Skip if email or phone already exists
        member = Member(**member_data)
        member.set_password('password123')  # Set the password hash for the member
        db.session.add(member)

    db.session.commit()

def seed_employers(count=5):
    """Seeds the database with fake Employer data."""
    for _ in range(count):
        employer_data = {
            'company_name': fake.company(),
            'email': fake.company_email(),
            'phone': fake.phone_number(),
            'about': fake.catch_phrase(),  # Updated to a catchphrase for variety
            'password': 'password123'
        }
        if Employer.query.filter_by(email=employer_data['email']).first() or Employer.query.filter_by(phone=employer_data['phone']).first():
            continue  # Skip if email or phone already exists
        employer = Employer(**employer_data)
        employer.set_password('password123')  # Set the password hash for the employer
        db.session.add(employer)

    db.session.commit()

def seed_jobs(count=15):
    """Seeds the database with fake Job data."""
    employers = Employer.query.all()
    if not employers:
        print("Please seed employers first.")
        return

    for _ in range(count):
        job_data = {
            'title': fake.job(),
            'description': fake.catch_phrase(),
            'salary': fake.random_int(min=30000, max=120000),  # Random salary as a float
            'deadline': datetime.utcnow() + timedelta(days=fake.random_int(min=10, max=90)),
            'employer_id': fake.random_element(employers).id
        }
        job = Job(**job_data)
        db.session.add(job)

    db.session.commit()
def seed_job_views(count=20):
    """Seeds the database with fake JobView data."""
    members = Member.query.all()
    jobs = Job.query.all()
    if not members or not jobs:
        print("Please seed members and jobs first.")
        return

    for _ in range(count):
        job_view_data = {
            'member_id': fake.random_element(members).id,
            'job_id': fake.random_element(jobs).id,
            'viewed_at': datetime.utcnow() - timedelta(days=fake.random_int(min=1, max=30))
        }
        job_view = JobView(**job_view_data)
        db.session.add(job_view)

    db.session.commit()

def seed_applications(count=20):
    """Seeds the database with fake Application data."""
    members = Member.query.all()
    jobs = Job.query.all()
    if not members or not jobs:
        print("Please seed members and jobs first.")
        return

    for _ in range(count):
        application_data = {
            'member_id': fake.random_element(members).id,
            'job_id': fake.random_element(jobs).id,
            'status': fake.random_element(elements=("applied", "approved", "rejected")),
            'applied_at': datetime.utcnow() - timedelta(days=fake.random_int(min=1, max=30))
        }
        application = Application(**application_data)
        db.session.add(application)

    db.session.commit()

def seed_saved_jobs(count=20):
    """Seeds the database with fake SavedJob data."""
    members = Member.query.all()
    jobs = Job.query.all()
    if not members or not jobs:
        print("Please seed members and jobs first.")
        return

    for _ in range(count):
        saved_job_data = {
            'member_id': fake.random_element(members).id,
            'job_id': fake.random_element(jobs).id,
        }
        saved_job = SavedJob(**saved_job_data)
        db.session.add(saved_job)

    db.session.commit()    



if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Ensure tables are created
        seed_members(10)  # Seed members
        seed_employers(5)  # Seed employers
        seed_jobs(15)  # Seed jobs
        seed_job_views(20)  # Seed job views
        seed_applications(20)  # Seed applications


    print("Database seeded with fake member, employer, and job data.")
