

from flask import Blueprint, request, jsonify
from flask_restful import Api
from app.controllers.employer_controller import EmployerResource
from app.utils.validations import validate_required_fields
from flask_jwt_extended import jwt_required
from app.services.employer_services import EmployerService
from app.utils.authentication import authenticate_admin

employer_bp = Blueprint('employer', __name__)
api = Api(employer_bp)

@employer_bp.route('/', methods=['POST'])
def register_employer():
    data = request.get_json()
    valid, error = validate_required_fields(data, ['company_name', 'email', 'phone', 'about', 'password'])
    if not valid:
        return jsonify({"error": error}), 400
    return EmployerService.create_employer(data)

@employer_bp.route('/', methods=['GET'])
@jwt_required()
@authenticate_admin()
def get_all_employers():
    return EmployerService.get_all_employers()

@employer_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
@authenticate_admin()
def get_employer(id):
    return EmployerService.get_employer_by_id(id)

# Define routes for Employer
api.add_resource(EmployerResource, '/employer')
