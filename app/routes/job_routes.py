
from flask import Blueprint
from flask_restful import Api
from app.controllers.job_controller import JobResource, SingleJobResource

job_bp = Blueprint('job', __name__)
api = Api(job_bp)

# Define routes for Job
api.add_resource(JobResource, '/')
api.add_resource(SingleJobResource, '/<int:id>')  # For updating or deleting a specific job