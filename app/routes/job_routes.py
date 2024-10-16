
from flask import Blueprint
from flask_restful import Api
from app.controllers.job_controller import JobResource

job_bp = Blueprint('job', __name__)
api = Api(job_bp)

# Define routes for Job
api.add_resource(JobResource, '/job')
