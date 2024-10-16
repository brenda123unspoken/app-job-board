
from app.models.job import Job
from app import db

class JobRepository:
    @staticmethod
    def create_job(title, description, salary, deadline, employer_id):
        """Create a new job."""
        new_job = Job(
            title=title,
            description=description,
            salary=salary,
            deadline=deadline,
            employer_id=employer_id
        )
        db.session.add(new_job)
        db.session.commit()
        return new_job

    @staticmethod
    def update_job(job_id, data):
        """Update an existing job."""
        job = Job.query.get(job_id)
        if not job:
            return None
        
        job.title = data.get('title', job.title)
        job.description = data.get('description', job.description)
        job.salary = data.get('salary', job.salary)
        job.deadline = data.get('deadline', job.deadline)
        
        db.session.commit()
        return job

    @staticmethod
    def delete_job(job_id):
        """Delete a job."""
        job = Job.query.get(job_id)
        if job:
            db.session.delete(job)
            db.session.commit()
            return job
        return None
