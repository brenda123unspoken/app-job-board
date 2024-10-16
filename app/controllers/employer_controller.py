from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.employer_services import EmployerService

class EmployerResource(Resource):
    @jwt_required()
    def post(self):
        """Register a new employer."""
        data = request.get_json()
        current_user = get_jwt_identity()  # Adjust based on JWT token structure

        # Check if the user already has an employer profile using a unique identifier other than `user_id`
        existing_employer = EmployerService.get_employer_by_unique_identifier(current_user)
        if existing_employer:
            return jsonify({"msg": "Employer profile already exists"}), 400

        # Register the new employer
        employer = EmployerService.register_employer(data, current_user)
        if not employer:
            return jsonify({"msg": "Employer registration failed"}), 400
        return jsonify(employer.to_dict()), 201

    @jwt_required()
    def get(self):
        """Get the current employer's profile."""
        current_user = get_jwt_identity()

        employer = EmployerService.get_employer_by_unique_identifier(current_user)
        if not employer:
            return jsonify({"msg": "Employer profile not found"}), 404
        return jsonify(employer.to_dict()), 200

    @jwt_required()
    def put(self):
        """Update employer profile details."""
        data = request.get_json()
        current_user = get_jwt_identity()

        employer = EmployerService.get_employer_by_unique_identifier(current_user)
        if not employer:
            return jsonify({"msg": "Employer profile not found"}), 404

        updated_employer = EmployerService.update_employer(employer.id, data)
        if not updated_employer:
            return jsonify({"msg": "Failed to update employer profile"}), 400
        return jsonify(updated_employer.to_dict()), 200
