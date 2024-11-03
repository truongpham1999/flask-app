from flask import Blueprint
from src.tableListApp.controllers.documentController import get_all_documents, get_document_by_id, add_document

documentBlueprint = Blueprint('documents', __name__)

documentBlueprint.route('/', methods=['GET'])(get_all_documents)
documentBlueprint.route('/<int:document_id>', methods=['GET'])(get_document_by_id)
documentBlueprint.route('/', methods=['POST'])(add_document)
