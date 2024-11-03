from src.tableListApp.models.document import db, Document

class DocumentService:
    def get_documents(self):
        documents = Document.query.all()
        return [{'id': doc.id, 'title': doc.title, 'description': doc.description, 'status': doc.status} for doc in documents]

    def get_document(self, document_id):
        document = Document.query.get(document_id)
        if document:
            return {'id': document.id, 'title': document.title, 'description': document.description, 'status': document.status}
        return None

    def create_document(self, title, description, status):
        new_document = Document(title=title, description=description, status=status)
        db.session.add(new_document)
        db.session.commit()
        return True
