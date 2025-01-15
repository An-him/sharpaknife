from ..utils import db

class Blade(db.Model):
    __tablename__ = 'blades'
    id=db.Column(db.Integer(), primary_key=True)
    type=db.Column(db.String(255),nullable=False)
    NumberOfKnives=db.Column(db.Integer(),nullable=False)    