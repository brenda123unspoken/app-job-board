from app.extensions import db

# Association table to link members and jobs
saved_jobs = db.Table('saved_jobs',
    db.Column('member_id', db.Integer, db.ForeignKey('member.id'), primary_key=True),
    db.Column('job_id', db.Integer, db.ForeignKey('jobs.id'), primary_key=True)
)
