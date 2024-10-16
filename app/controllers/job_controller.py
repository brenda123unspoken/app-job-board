from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.job_services import JobService
from app.services.employer_services import EmployerService

class JobResource(Resource):
    @jwt_required()
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

    @jwt_required()
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
