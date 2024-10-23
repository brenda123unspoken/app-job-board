
from flask import Blueprint
from flask_restful import Api
from app.controllers.job_controller import JobResource, SingleJobResource, JobsByEmployerResource

job_bp = Blueprint('job', __name__)
api = Api(job_bp)

# Define routes for Job
api.add_resource(JobResource, '/')
api.add_resource(SingleJobResource, '/<int:job_id>')  # For updating or deleting a specific job
api.add_resource(JobsByEmployerResource, '/employer/<int:employer_id>/jobs')