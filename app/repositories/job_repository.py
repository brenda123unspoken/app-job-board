
# from app.models.job import Job
# from app import db

# class JobRepository:
#     @staticmethod
#     def create_job(title, description, salary, deadline, employer_id):
#         """Create a new job."""
#         new_job = Job(
#             title=title,
#             description=description,
#             salary=salary,
#             deadline=deadline,
#             employer_id=employer_id
#         )
#         db.session.add(new_job)
#         db.session.commit()
#         return new_job

#     @staticmethod
#     def update_job(job_id, data):
#         """Update an existing job."""
#         job = Job.query.get(job_id)
#         if not job:
#             return None
        
#         job.title = data.get('title', job.title)
#         job.description = data.get('description', job.description)
#         job.salary = data.get('salary', job.salary)
#         job.deadline = data.get('deadline', job.deadline)
        
#         db.session.commit()
#         return job

#     @staticmethod
#     def delete_job(job_id):
#         """Delete a job."""
#         job = Job.query.get(job_id)
#         if job:
#             db.session.delete(job)
#             db.session.commit()
#             return job
#         return None
    

#     @staticmethod
#     def get_job_by_id(id):
#         return Job.query.get(id)

#     @staticmethod
#     def get_jobs_by_employer(employer_id):
#         return Job.query.filter_by(employer_id=employer_id).all()

#     @staticmethod
#     def get_all_jobs():
#         return Job.query.all()

from app import db
from app.models.job import Job

class JobRepository:
    @staticmethod
    def create(data):
        """Create a new job."""
        job = Job(**data)
        db.session.add(job)
        db.session.commit()
        return job

    @staticmethod
    def get_all():
        """Fetch all jobs."""
        return Job.query.all()

    @staticmethod
    def get_by_id(job_id):
        """Fetch a job by ID."""
        return Job.query.get(job_id)

    @staticmethod
    def update(job, data):
        """Update an existing job."""
        for key, value in data.items():
            setattr(job, key, value)
        db.session.commit()
        return job

    @staticmethod
    def delete(job):
        """Delete a job."""
        db.session.delete(job)
        db.session.commit()

    @staticmethod
    def get_jobs_by_employer(employer_id):
        """Fetch all jobs for a specific employer."""
        return Job.query.filter_by(employer_id=employer_id).all()
   
