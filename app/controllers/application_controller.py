from flask_restful import Resource
from flask import request
from app.services.application_service import ApplicationService
from flask_jwt_extended import jwt_required, get_jwt_identity

class ApplicationResource(Resource):
    @jwt_required()
    def post(self):
        """Create a new application."""
        data = request.get_json()
        member_id = data.get('member_id')
        job_id = data.get('job_id')

        if not member_id or not job_id:
            return {"error": "Member ID and Job ID are required."}, 400

        status = 'applied'
        application = ApplicationService.create_application(member_id, job_id, status)
        return {"message": "Application created successfully.", "application_id": application.id}, 201

    @jwt_required()
    def get(self, application_id):
        """Get an application by its ID."""
        application = ApplicationService.get_application_by_id(application_id)
        if not application:
            return {"error": "Application not found."}, 404

        return {"application": application.to_dict()}, 200


    @jwt_required()
    def put(self, application_id):
        """Update an application (by the member)."""
        data = request.get_json()
        # Logic for member to update application details if necessary
        # e.g. change resume, cover letter, etc.
        
        application = ApplicationService.update_application(application_id, data)
        if not application:
            return {"error": "Application not found."}, 404

        return {"message": "Application updated successfully.", "application": application.to_dict()}, 200

class ApproveApplicationResource(Resource):
    @jwt_required()
    def put(self, application_id):
        """Approve an application (by the employer)."""
        employer_id = get_jwt_identity()  # Get the employer ID from the JWT token
        new_status = 'approved'
        response, status_code = ApplicationService.update_application_status(application_id, new_status, employer_id)
        return response, status_code


class RejectApplicationResource(Resource):
    @jwt_required()
    def put(self, application_id):
        """Reject an application (by the employer)."""
        employer_id = get_jwt_identity()  # Get the employer ID from the JWT token
        new_status = 'rejected'
        response, status_code = ApplicationService.update_application_status(application_id, new_status, employer_id)
        return response, status_code 