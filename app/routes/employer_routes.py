

from flask import Blueprint
from flask_restful import Api
from app.controllers.employer_controller import EmployerResource

employer_bp = Blueprint('employer', __name__)
api = Api(employer_bp)

# Define routes for Employer
api.add_resource(EmployerResource, '/employer')
