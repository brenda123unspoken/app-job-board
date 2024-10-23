from app.repositories.job_view_repository import JobViewRepository

class JobViewService:
    @staticmethod
    def track_job_view(member_id, job_id):
        """Track when a member views a job."""
        return JobViewRepository.create_job_view(member_id, job_id)

    @staticmethod
    def get_views_by_member(member_id):
        """Get all job views for a specific member."""
        return JobViewRepository.get_job_views_by_member(member_id)

    @staticmethod
    def get_views_by_job(job_id):
        """Get all views for a specific job."""
        return JobViewRepository.get_job_views_by_job(job_id)

    @staticmethod
    def get_all_job_views():
        # Retrieve all job views from the database
        
        job_views = JobViewRepository.get_all()  # Fetch job views
        return [job_view.to_dict() for job_view in job_views]  # Convert to dict
