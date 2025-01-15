from ..utils import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):

    __tablename__ = 'users'

    id=db.Column(db.Integer(), primary_key=True)
    username=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(255),nullable=False,unique=True)
    password_hash=db.Column(db.Text(),nullable=False)
    location=db.Column(db.Text(),nullable=True)
    is_staff=db.Column(db.Boolean(),default=False)
    is_active=db.Column(db.Boolean(),default=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)  # Automatically set on creation
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)  # Automatically updated

    orders=db.relationship('Order',backref='client',lazy=True)


    def __repr__(self):
          return f"<User {self.username}>"


    def save_user(self):
              
            db.session.add(self)
            db.session.commit()


    @classmethod
    def get_by_id(cls,id):
          return cls.query.get_or_404(id)