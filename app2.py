from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.document import db, Document

# Create the Flask application
app = Flask(__name__)

# Database configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '90328dksalowki1282'  # Replace with a strong random key

# Initialize SQLAlchemy
db.init_app(app)

@app.route('/create-database')
def create_database():
    with app.app_context():
        db.create_all()  # Creates all tables defined by models
    return 'Database tables created successfully'

@app.route('/')
def hello_world():
    return 'Hello World!'

# Route to list documents
@app.route('/table_list')
def table_list():
    documents = Document.query.all()
    if not documents:
        return jsonify({'status': 'fail', 'message': 'No documents found'}), 404

    result = [
        {
            'id': document.id,
            'title': document.title,
            'description': document.description,
            'status': document.status
        } for document in documents
    ]
    return jsonify({'status': 'success', 'data': result}), 200

@app.route('/table_list/<int:document_id>')
def get_document(document_id):
    document = Document.query.get_or_404(document_id)
    return jsonify({
        'id': document.id,
        'title': document.title,
        'description': document.description,
        'status': document.status
    }), 200

# Route to add a new document
@app.route('/add_document', methods=['POST'])
def add_document():
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        status = data.get('status')

        if not title or not description or status is None:
            return jsonify({'status': 'fail', 'message': 'Title, description, and status are required fields'}), 400

        new_document = Document(title=title, description=description, status=status)
        db.session.add(new_document)
        db.session.commit()

        return jsonify({'status': 'success', 'message': 'Document added successfully!'}), 200

    except Exception as e:
        return jsonify({'status': 'fail', 'message': 'Failed to add document', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run()