from main import db

class StudentModel(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String,unique=True,nullable=False)
    collage=db.Column(db.String,nullable=False)

db.create_all()