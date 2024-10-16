from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.job_services import JobService
from app.services.employer_services import EmployerService
from app.utils.authentication import authenticate_admin, authenticate_employer

class JobResource(Resource):
    @jwt_required()
    @authenticate_employer()
    def post(self):
        """ Post a new job for the employer """
        data = request.get_json()
        current_user = get_jwt_identity()

        employer = EmployerService.get_employer_by_unique_identifier(current_user)
        if not employer:
            return jsonify({"msg": "Employer not found"}), 404

        job = JobService.post_job(data, employer.id)
        if not job:
            return jsonify({"msg": "Failed to create job"}), 400
        return jsonify(job.to_dict()), 201
    
    def get(self):
        """Get all jobs."""
        jobs = JobService.get_all_jobs()
        # Assuming get_all_jobs returns a list of job objects
        return jsonify([job.to_dict() for job in jobs]), 200

class SingleJobResource(Resource):
    @jwt_required()
    @authenticate_employer()
    def put(self, job_id):
        """ Update an existing job posting """
        data = request.get_json()
        current_user = get_jwt_identity()

        employer = EmployerService.get_employer_by_unique_identifier(current_user)
        if not employer:
            return jsonify({"msg": "Employer not found"}), 404

        job = JobService.update_job(job_id, data)
        if not job:
            return jsonify({"msg": "Failed to update job posting"}), 400
        return jsonify(job.to_dict()), 200

    @jwt_required()
    @authenticate_admin()
    @authenticate_employer()
    def delete(self, job_id):
        """Delete a job posting by its ID (admin access, employer access)."""
        success = JobService.delete_job(job_id)
        if not success:
            return jsonify({"msg": "Failed to delete job posting"}), 400
        
        return jsonify({"msg": "Job posting deleted successfully"}), 200