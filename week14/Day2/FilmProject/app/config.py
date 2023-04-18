import os

# Set the secret key for the Flask application
SECRET_KEY = os.environ.get('1234') or 'my-secret-key'

# Set the database URL
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///mydatabase.db'

# Set SQLALCHEMY_TRACK_MODIFICATIONS to False to suppress warning messages
SQLALCHEMY_TRACK_MODIFICATIONS = False
