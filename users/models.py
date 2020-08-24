from libs.orm import db
class User(db.Model):
    __tablename__='User'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20),nullable=True)
    age=db.Column(db.Integer,nullable=True)
    phone=db.Column(db.String(30),nullable=True)
    city=db.Column(db.String(30),nullable=True)
