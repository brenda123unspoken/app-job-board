# from app.repositories.job_repository import JobRepository

# class JobService:
#     @staticmethod
#     def post_job(data, employer_id):
#         job = JobRepository.create_job(
#             data['title'],
#             data['description'],
#             data['salary'],
#             data['deadline'],
#             employer_id
#         )
#         return job

#     @staticmethod
#     def update_job(job_id, data):
#         return JobRepository.update_job(job_id, data)
    
#     @staticmethod
#     def get_job_by_id(id):
#         job = JobRepository.get_job_by_id(id)
#         if not job:
#             return {"error": "Job not found"}, 404
#         return job.to_dict(), 200

#     @staticmethod
#     def get_jobs_by_employer(employer_id):
#         jobs = JobRepository.get_jobs_by_employer(employer_id)
#         return [job.to_dict() for job in jobs], 200

#     @staticmethod
#     def get_all_jobs():
#         jobs = JobRepository.get_all_jobs()
#         return [job.to_dict() for job in jobs], 200

from app.repositories.job_repository import JobRepository

class JobService:
    @staticmethod
    def post_job(data, employer_id):
        """Create a new job for the employer."""
        job = JobRepository.create_job(
            data['title'],
            data['description'],
            data['salary'],
            data['deadline'],
            employer_id
        )
        if job:
            return job.to_dict(), 201  # Returning job data with a 201 status
        return {"error": "Failed to create job"}, 400  # Handle creation failure

    @staticmethod
    def update_job(job_id, data):
        """Update an existing job posting."""
        job = JobRepository.update_job(job_id, data)
        if job:
            return job.to_dict(), 200  # Returning updated job data with a 200 status
        return {"error": "Failed to update job posting"}, 400  # Handle update failure

    @staticmethod
    def get_job_by_id(id):
        """Retrieve a job by its ID."""
        job = JobRepository.get_job_by_id(id)
        if not job:
            return {"error": "Job not found"}, 404  # Return not found error
        return job.to_dict(), 200  # Return job data with a 200 status

    @staticmethod
    def get_jobs_by_employer(employer_id):
        """Retrieve all jobs posted by a specific employer."""
        jobs = JobRepository.get_jobs_by_employer(employer_id)
        return [job.to_dict() for job in jobs], 200  # Return list of jobs with a 200 status

    @staticmethod
    def get_all_jobs():
        """Retrieve all jobs."""
        jobs = JobRepository.get_all_jobs()
        return [job.to_dict() for job in jobs], 200  # Return list of all jobs with a 200 status

