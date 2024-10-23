from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.job_services import JobService
from app.services.employer_services import EmployerService
from app.utils.authentication import authenticate_admin, authenticate_employer

# class JobResource(Resource):
#     @jwt_required()
#     @authenticate_employer()
#     def post(self):
#         """ Post a new job for the employer """
#         data = request.get_json()
#         current_user = get_jwt_identity()

#         employer = EmployerService.get_employer_by_unique_identifier(current_user)
#         if not employer:
#             return jsonify({"msg": "Employer not found"}), 404

#         job_response = JobService.post_job(data, employer.id)
#         if isinstance(job_response, dict) and 'error' in job_response:
#             return jsonify(job_response), 400
#         return jsonify(job_response), 201
    
#     def get(self):
#         """Get all jobs."""
#         jobs = JobService.get_all_jobs()
        
#         if not jobs:
#             return jsonify({"msg": "No jobs found"}), 404    

#         try:
#             job_dicts = []
#             for job in jobs:
#                 # Check if the job is already a dictionary
#                 if isinstance(job, dict):
#                     job_dicts.append(job)
#                 else:
#                     # Call `to_dict()` only if the object is not already a dictionary
#                     job_dicts.append(job.to_dict())
        
#             return jsonify(job_dicts), 200

       
#         except AttributeError as e:
#             print(f"Error: {e}") 
#             return jsonify({"error": "One or more job objects are missing 'to_dict' method"}), 500   
            

     
# class SingleJobResource(Resource):
#     @jwt_required()
#     @authenticate_employer()
#     def put(self, job_id):
#         """ Update an existing job posting """
#         data = request.get_json()
#         current_user = get_jwt_identity()

#         employer = EmployerService.get_employer_by_unique_identifier(current_user)
#         if not employer:
#             return jsonify({"msg": "Employer not found"}), 404

#         job_response = JobService.update_job(job_id, data)
#         if isinstance(job_response, dict) and 'error' in job_response:
#             return jsonify(job_response), 400
#         return jsonify(job_response), 200
    
    
#     @jwt_required()
#     def delete(self, job_id):
#         """Delete a job posting by its ID (admin or employer access)"""
#         current_user = get_jwt_identity()

#         # Check if the user is an admin first
#         if authenticate_admin(current_user):
#             is_admin = True
#         else:
#             # Check if the user is an employer
#             employer = EmployerService.get_employer_by_unique_identifier(current_user)
#             is_admin = False

    
#             return jsonify({"msg": "Unauthorized: Not an employer or admin"}), 403

#         # Proceed with job deletion
#         success = JobService.delete_job(job_id)
#         if not success:
#             return jsonify({"msg": "Failed to delete job posting"}), 400
#         return jsonify({"msg": "Job posting deleted successfully"}), 200
    

class JobResource(Resource):
    @jwt_required()
    def post(self):
        """Create a new job for the logged-in employer."""
        data = request.get_json()
        
        current_user = get_jwt_identity()  # Assuming employer ID comes from JWT
        employer_id = current_user['id']
        current_user_email = current_user.get('email') # Ensure to extract the email
        # Check if the current user is a registered employer
        if current_user_email is None:
            return {'message': 'User email not found in token'}, 401

        
        employer = EmployerService.get_employer_by_unique_identifier(current_user_email)
        
        if not employer:
            # If the user is not a registered employer, ask them to register first
            return jsonify({"msg": "You need to register as an employer before posting a job."}), 400
        
        
        result, status = JobService.create_job(data, employer_id)
        return result, status

    def get(self):
        """Fetch all jobs."""
        jobs, status = JobService.get_all_jobs()
        return jobs, status

class SingleJobResource(Resource):
    def get(self, job_id):
        """Fetch a single job by ID."""
        job, status = JobService.get_job_by_id(job_id)
        return job, status   

    @jwt_required()
    def put(self, job_id):
        """Update a job by ID."""
        data = request.get_json()
        result, status = JobService.update_job(job_id, data)
        return result, status

    @jwt_required()
    def delete(self, job_id):
        """Delete a job by ID."""
        result, status = JobService.delete_job(job_id)
        return result, status    

class JobsByEmployerResource(Resource):
    def get(self, employer_id):
        """Fetch all jobs for a specific employer by employer ID."""
        jobs, status = JobService.get_jobs_by_employer(employer_id)
        return jobs, status

