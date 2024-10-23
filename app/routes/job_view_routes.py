from flask import Blueprint
from flask_restful import Api
from app.controllers.job_view_controller import JobViewResource

job_view_bp = Blueprint('job_view', __name__)
job_view_api = Api(job_view_bp)

job_view_api.add_resource(JobViewResource, '/job-views', '/job-views/<int:job_id>')

# Register this blueprint in your main app
