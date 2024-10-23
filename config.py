import os

class Config:
    """Base configuration class."""
    # Secret keys for various purposes (JWT, sessions, etc.)
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key_here')

    # Database configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///app.db')

    # Flask settings
    DEBUG = False
    TESTING = False

        # JWT settings
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour
    JWT_REFRESH_TOKEN_EXPIRES = 2592000  # 30 days

    
    PER_PAGE = 10  # Pagination
     
    # Flask-Mail settings
    MAIL_SERVER = 'smtp.your-email-provider.com'  # Your SMTP server
    MAIL_PORT = 587  # Port for TLS
    MAIL_USE_TLS = True  # Enable TLS
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'your_email@example.com'  # Your email address
    MAIL_PASSWORD = 'your_password'  # Your email password
    MAIL_DEFAULT_SENDER = 'your_email@example.com'  # Default sender email

