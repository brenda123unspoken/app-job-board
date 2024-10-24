# from app.repositories.job_repository import JobRepository

# class JobService:
    
#     @staticmethod
#     def post_job(data, employer_id):
#         """Create a new job for the employer."""
#         try:
#             # Ensure necessary fields are present in the data
#             required_fields = ['title', 'description', 'salary', 'deadline']
#             for field in required_fields:
#                 if field not in data:
#                     return {"error": f"Missing required field: {field}"}

#             # Create the job using the repository
#             job = JobRepository.create_job(
#                 title=data['title'],
#                 description=data['description'],
#                 salary=data['salary'],
#                 deadline=data['deadline'],
#                 employer_id=employer_id
#             )
#             if job:
#                 return job.to_dict()  # Service layer should only return data
            
#             return {"error": "Failed to create job"}  # Handle creation failure
#         except Exception as e:
#             # Log the exception (you could use a logger here instead of print)
#             print(f"Error occurred while creating job: {e}")
#             return {"error": "An error occurred during job creation"}

#     @staticmethod
#     def update_job(job_id, data):
#         """Update an existing job posting."""
#         try:
#             job = JobRepository.update_job(job_id, data)
#             if job:
#                 return job.to_dict()  # Return updated job data
            
#             return {"error": "Failed to update job posting"}  # Handle update failure
#         except Exception as e:
#             print(f"Error occurred while updating job: {e}")
#             return {"error": "An error occurred during job update"}

#     @staticmethod
#     def get_job_by_id(job_id):
#         """Retrieve a job by its ID."""
#         try:
#             job = JobRepository.get_job_by_id(job_id)
#             if not job:
#                 return {"error": "Job not found"}  # Return not found error
            
#             return job.to_dict()  # Return job data
#         except Exception as e:
#             print(f"Error occurred while retrieving job by ID: {e}")
#             return {"error": "An error occurred while retrieving the job"}

#     @staticmethod
#     def get_jobs_by_employer(employer_id):
#         """Retrieve all jobs posted by a specific employer."""
#         try:
#             jobs = JobRepository.get_jobs_by_employer(employer_id)
#             return [job.to_dict() for job in jobs]  # Return list of jobs
#         except Exception as e:
#             print(f"Error occurred while retrieving jobs by employer: {e}")
#             return {"error": "An error occurred while retrieving jobs for the employer"}

#     @staticmethod
#     def get_all_jobs():
#         """Retrieve all jobs."""
#         try:
#             jobs = JobRepository.get_all_jobs()
#             return [job.to_dict() for job in jobs]  # Return list of all jobs
#         except Exception as e:
#             print(f"Error occurred while retrieving all jobs: {e}")
#             return {"error": "An error occurred while retrieving all jobs"}

from app.repositories.job_repository import JobRepository
from app.websocket.socketio import notify_members_on_update, notify_members_on_delete
from app.repositories.application_repository import ApplicationRepository
from datetime import datetime

class JobService:
    @staticmethod
    def create_job(data, employer_id):
        """Business logic for creating a job."""
        data['employer_id'] = employer_id

        required_fields = ['title', 'description', 'salary']
        for field in required_fields:
            if field not in data or not data[field]:
                return {"error": f"'{field}' is required"}, 400

        if 'deadline' in data:
            data['deadline'] = datetime.fromisoformat(data['deadline'])  # Convert to datetime
        
        job = JobRepository.create(data)
        return job.to_dict(), 201

    @staticmethod
    def get_all_jobs():
        """Business logic for retrieving all jobs."""
        jobs = JobRepository.get_all()
        return [job.to_dict() for job in jobs], 200

    @staticmethod
    def get_job_by_id(job_id):
        """Business logic for retrieving a single job by ID."""
        job = JobRepository.get_by_id(job_id)
        if not job:
            return {"message": "Job not found"}, 404
        return job.to_dict(), 200

    @staticmethod
    def update_job(job_id, data):
        """Business logic for updating a job."""
        job = JobRepository.get_by_id(job_id)
        if not job:
            return {"message": "Job not found"}, 404
        
        if 'deadline' in data:
            data['deadline'] = datetime.fromisoformat(data['deadline'])  # Convert to datetime
        
        if 'created_at' in data:
            data['created_at'] = datetime.fromisoformat(data['created_at'])
        if 'updated_at' in data:
            data['updated_at'] = datetime.fromisoformat(data['updated_at'])
        
        updated_job = JobRepository.update(job, data)
        notify_members_on_update(job_id)

        return updated_job.to_dict(), 200
        

    @staticmethod
    def delete_job(job_id):
        """Business logic for deleting a job."""
        job = JobRepository.get_by_id(job_id)
        if not job:
            return {"message": "Job not found"}, 404
        
        JobRepository.delete(job)
        notify_members_on_delete(job_id)
        return {"message": "Job deleted successfully"}, 200
        

    
    @staticmethod
    def get_jobs_by_employer(employer_id):
        """Business logic for retrieving jobs by employer ID."""
        jobs = JobRepository.get_jobs_by_employer(employer_id)
        if not jobs:
            return {"message": "No jobs found for this employer."}, 404
        
        job_list = []
        for job in jobs:
            # Fetch applications for the job using ApplicationRepository
            applications = ApplicationRepository.get_applications_by_job_id(job.id)
            
            # Prepare application details with member info
            application_data = []
            for application in applications:
                member = application.member  # Assuming Application has a member relationship
                application_data.append({
                    'application_id': application.id,
                    'status': application.status,
                    'applied_at': application.applied_at.isoformat(),
                    'member': {
                        'member_id': member.id,
                        'name': member.name,
                        'email': member.email,
                        'phone': member.phone
                    }
                })
            
            # Build the job response
            job_list.append({
                'job_id': job.id,
                'title': job.title,
                'description': job.description,
                'salary': job.salary,
                'applications': application_data  # Include applications here
            })

        return job_list, 200

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
        
