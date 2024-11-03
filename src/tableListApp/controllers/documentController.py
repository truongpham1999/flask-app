from flask import jsonify, request
from src.tableListApp.services.documentService import DocumentService

# Instantiate the DocumentService
document_service = DocumentService()

def get_all_documents():
    documents = document_service.get_documents()
    if not documents:
        return jsonify({'status': 'fail', 'message': 'No documents found'}), 404
    return jsonify({'status': 'success', 'data': documents}), 200

def get_document_by_id(document_id):
    document = document_service.get_document(document_id)
    if document:
        return jsonify(document), 200
    else:
        return jsonify({'status': 'fail', 'message': 'Document not found'}), 404

def add_document():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    status = data.get('status')

    if not title or not description or status is None:
        return jsonify({'status': 'fail', 'message': 'Title, description, and status are required fields'}), 400

    result = document_service.create_document(title, description, status)
    if result:
        return jsonify({'status': 'success', 'message': 'Document added successfully!'}), 201
    else:
        return jsonify({'status': 'fail', 'message': 'Failed to add document'}), 500
