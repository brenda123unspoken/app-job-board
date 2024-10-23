from flask import Flask
from config import Config
from app.extensions import db, migrate, jwt, socketio, mail



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")
    mail.init_app(app) 


    # Import and register the blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.member_routes import member_bp
    from app.routes.employer_routes import employer_bp  
    from app.routes.job_routes import job_bp 
    from app.routes.job_view_routes import job_view_bp
    from app.routes.application_routes import application_bp

    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(member_bp, url_prefix='/members')
    app.register_blueprint(employer_bp, url_prefix='/api/employers')
    app.register_blueprint(job_bp, url_prefix='/jobs')  
    app.register_blueprint(job_view_bp, url_prefix='/api')
    app.register_blueprint(application_bp, url_prefix='/api')

    return app
