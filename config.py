# Configuration file for the Flask web application

# Secret key for session management. This should be a secret and unique string.
SECRET_KEY = 'mysecretkey'

# Database configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False