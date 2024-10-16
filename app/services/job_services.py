from app.repositories.job_repository import JobRepository

class JobService:
    @staticmethod
    def post_job(data, employer_id):
        job = JobRepository.create_job(
            data['title'],
            data['description'],
            data['salary'],
            data['deadline'],
            employer_id
        )
        return job

    @staticmethod
    def update_job(job_id, data):
        return JobRepository.update_job(job_id, data)
