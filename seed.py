# from app import create_app, db
# from app.models.member import Member
# from app.models.employer import Employer
# from app.models.job import Job
# from faker import Faker

# fake = Faker()

# app = create_app()

# def seed_members():
#     """Seed fake members for testing purposes."""
#     for _ in range(10):  # Adjust the number to how many members you want to seed
#         fake_member = Member(
#             name=fake.name(),  # Random name
#             phone=fake.phone_number(),  # Random phone number
#             email=fake.email(),  # Random email
#             role=fake.random_element(elements=("member", "admin", "supervisor")),  # Random role
#             is_active=True  # Set active status to True by default
#         )
#         fake_member.set_password('password123')  # Set password hash for the member
#         db.session.add(fake_member)

# def seed_employers():
#     """Seed fake employers for testing purposes."""
#     for _ in range(5):  # Adjust the number to how many employers you want to seed
#         fake_employer = Employer(
#             company_name=fake.company(),  # Random company name
#             email=fake.email(),  # Random email
#             phone_number=fake.phone_number(),  # Random phone number
#             about=fake.catch_phrase(),  # Random catchphrase as about
#             password='securePassword123'  # Use a placeholder password
#         )
#         db.session.add(fake_employer)

# def seed_jobs():
#     """Seed fake jobs for testing purposes."""
#     employers = Employer.query.all()  # Get all employers to associate jobs with them
#     for employer in employers:
#         for _ in range(3):  # Adjust the number to how many jobs you want per employer
#             fake_job = Job(
#                 title=fake.job(),  # Random job title
#                 description=fake.text(),  # Random job description
#                 salary=fake.random_int(min=30000, max=120000),  # Random salary
#                 deadline=fake.date_between(start_date='today', end_date='+30d'),  # Random deadline
#                 employer_id=employer.id  # Associate job with the employer
#             )
#             db.session.add(fake_job)

# def seed_database():
#     """Create tables and seed data."""
#     with app.app_context():
#         db.create_all()  # Ensure all tables are created before seeding
#         seed_members()  # Seed the database with members
#         seed_employers()  # Seed the database with employers
#         seed_jobs()  # Seed the database with jobs
#         db.session.commit()  # Commit the session to save all data
#         print("Fake member, employer, and job data seeded successfully!")

# # Run the seeding process
    # seed_database()



from faker import Faker
from app import create_app, db
from app.models.member import Member
from app.models.employer import Employer
from app.models.job import Job
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
            continue
        member = Member(**member_data)
        member.set_password('password123')
        db.session.add(member)

    db.session.commit()

def seed_employers(count=5):
    """Seeds the database with fake Employer data."""
    for _ in range(count):
        employer_data = {
            'company_name': fake.company(),
            'email': fake.company_email(),
            'phone': fake.phone_number(),
            'about': fake.text(),
            'password': 'password123'
        }
        if Employer.query.filter_by(email=employer_data['email']).first() or Employer.query.filter_by(phone=employer_data['phone']).first():
            continue
        employer = Employer(**employer_data)
        employer.set_password('password123')
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
            'description': fake.text(),
            'salary': fake.random_element(elements=("50k", "60k", "70k", "80k")),
            'deadline': datetime.utcnow() + timedelta(days=fake.random_int(min=10, max=90)),
            'employer_id': fake.random_element(employers).id
        }
        job = Job(**job_data)
        db.session.add(job)

    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Ensure tables are created
        seed_members(10)
        seed_employers(5)
        seed_jobs(15)

    print("Database seeded with fake member, employer, and job data.")
