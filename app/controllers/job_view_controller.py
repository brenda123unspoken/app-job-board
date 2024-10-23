from flask_restful import Resource
from flask import request
from app.services.job_view_services import JobViewService

class JobViewResource(Resource):
    def post(self):
        """Endpoint to track job views."""
        data = request.get_json()
        member_id = data.get('member_id')
        job_id = data.get('job_id')

        if not member_id or not job_id:
            return {"error": "Member ID and Job ID are required."}, 400

        job_view = JobViewService.track_job_view(member_id, job_id)
        return {"message": "Job view tracked successfully.", "job_view_id": job_view.id}, 201

    def get(self, job_id=None):
        """Handle both getting all job views and views for a specific job."""
        if job_id:
            # Fetch views for a specific job
            job_views = JobViewService.get_views_by_job(job_id)
            return [view.to_dict() for view in job_views], 200
        else:
            # Fetch all job views
            job_views = JobViewService.get_all_job_views()
            return job_views, 200