from flask import Blueprint
from flask_restful import Api
from app.controllers.application_controller import ApplicationResource, ApproveApplicationResource, RejectApplicationResource

application_bp = Blueprint('applications', __name__)
api = Api(application_bp)


# Register this blueprint in your main app
api.add_resource(ApplicationResource, '/applications', '/applications/<int:application_id>', endpoint='application_detail')    

api.add_resource(ApproveApplicationResource, '/applications/<int:application_id>/approve')
api.add_resource(RejectApplicationResource, '/applications/<int:application_id>/reject')
