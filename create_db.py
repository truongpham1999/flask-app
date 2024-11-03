from app import app
from src.tableListApp.models.document import db

with app.app_context():
    db.create_all()
    print("Database tables created.")