# app/services/bulk_upload_service.py

import csv
from io import StringIO
from app.services.member_service import MemberService
from app.services.employer_service import EmployerService
from app import db
from app.websocket.socketio import notify_members_on_bulk_upload, notify_employers_on_bulk_upload  # Ensure to import your notification function


class BulkUploadService:
    @staticmethod
    def upload_members(file):
        try:
            csv_file = StringIO(file.read().decode())
            reader = csv.DictReader(csv_file)

            for row in reader:
                MemberService.create_member(row)
            db.session.commit()
            # Notify members about the new members added
            notify_members_on_bulk_upload("members")  # Notify all connected members

            return {"message": "Members uploaded successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500
       
    @staticmethod
    def upload_employers(file):
        try:
            csv_file = StringIO(file.read().decode())
            reader = csv.DictReader(csv_file)

            for row in reader:
                EmployerService.create_employer(row)
            db.session.commit()
            
            # Notify employers about the new employers added
            notify_employers_on_bulk_upload()  # Notify all connected employers

            return {"message": "Employers uploaded successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500
       
           
