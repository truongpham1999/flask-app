from flask import Blueprint, render_template
from src.tableListApp.controllers.documentController import get_all_documents, get_document_by_id, add_document

documentBlueprint = Blueprint('documents', __name__)

# API endpoints
documentBlueprint.route('/api/', methods=['GET'])(get_all_documents)
documentBlueprint.route('/api/<int:document_id>', methods=['GET'])(get_document_by_id)
documentBlueprint.route('/api/', methods=['POST'])(add_document)


# Routes to render HTML templates
@documentBlueprint.route('/', methods=['GET'])
def show_document_list():
    return render_template('table.html')

@documentBlueprint.route('/add', methods=['GET'])
def show_add_document_form():
    return render_template('add_document.html')