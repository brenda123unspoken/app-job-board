# app/routes/bulk_upload_routes.py

from flask import Blueprint, request, jsonify
from app.services.bulk_upload_service import BulkUploadService
from app.utils.authentication import authenticate_admin
from flask_jwt_extended import jwt_required

bulk_upload_bp = Blueprint('bulk_upload', __name__)

@bulk_upload_bp.route('/members/bulk-upload', methods=['POST'])
@jwt_required()
@authenticate_admin()
def bulk_upload_members():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "CSV file is required"}), 400
    return BulkUploadService.upload_members(file)

@bulk_upload_bp.route('/employers/bulk-upload', methods=['POST'])
@jwt_required()
@authenticate_admin()
def bulk_upload_employers():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "CSV file is required"}), 400
    return BulkUploadService.upload_employers(file)
