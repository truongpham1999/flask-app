from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from src.tableListApp.routes.documentRoutes import documentBlueprint
from src.tableListApp.models.document import db

# Create the Flask application
app = Flask(__name__, template_folder='src/tableListApp/templates')

# Database configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '90328dksalowki1282'

# Initialize SQLAlchemy and enable CORS
db.init_app(app)
CORS(app)

# Registering the blueprint
app.register_blueprint(documentBlueprint, url_prefix='/documents')

if __name__ == '__main__':
    app.run(debug=True)
