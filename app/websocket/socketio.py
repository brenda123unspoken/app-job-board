from flask_socketio import SocketIO, emit, join_room, leave_room
from app.models.job_views import JobView
from app.extensions import socketio, db
from datetime import datetime  # Assuming you are using this for timestamps


# Function to notify members when a job is updated
def notify_members_on_update(job_id):
    socketio.emit('job_updated', {'job_id': job_id}, namespace='/', to='/')

# Function to notify members when a job is deleted
def notify_members_on_delete(job_id):
    socketio.emit('job_deleted', {'job_id': job_id}, namespace='/', to='/')

# Function to track job views
def track_job_view(member_id, job_id):
    view = JobView(member_id=member_id, job_id=job_id)
    db.session.add(view)
    db.session.commit()

def notify_application_status(member_id, status):
    """
    Notify clients about the updated application status for a specific member.
    """
    socketio.emit('application_status_update', {
        'member_id': member_id,
        'status': status
    }, namespace='/', to='/')


# WebSocket events
@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit('connected', {'message': 'You are connected to the job board WebSocket!'}, namespace='/')

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")
    emit('disconnected', {'message': 'You are disconnected.'}, namespace='/')

@socketio.on('join_job_updates')
def join_job_updates(data):
    job_id = data['job_id']
    join_room(job_id)
    emit('message', {'message': f'Joined room for job {job_id}'}, room=job_id, namespace='/')

@socketio.on('leave_job_updates')
def leave_job_updates(data):
    job_id = data['job_id']
    leave_room(job_id)
    emit('message', {'message': f'Left room for job {job_id}'}, room=job_id, namespace='/')


# Notify members on bulk upload
def notify_members_on_bulk_upload(upload_type):
    socketio.emit('bulk_upload', {'type': upload_type}, namespace='/', to='/')

# Notify employers on bulk upload
def notify_employers_on_bulk_upload():
    socketio.emit('bulk_upload_employer', {'message': 'New employers have been added!'}, namespace='/', to='/')


# Notify about application status updates
@socketio.on('application_status_update')
def handle_application_status_update(data):
    socketio.emit('application_status_notification', {
        'data': data,
        'message': 'Application status has been updated',
        'timestamp': str(datetime.utcnow())  # Including timestamp
    }, namespace='/', to='/')
