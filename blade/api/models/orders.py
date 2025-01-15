from ..utils import db
from enum import Enum
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


class OrderStatus(Enum):
    BLUNT='BLUNT'
    WHETTING='WHETTING'
    SHARPENING='SHARPENING'
    SHARP='SHARP'

class Service(Enum):
    REPAIR='REPAIR'
    WHETTING='WHETTING'

class Order(db.Model):
    __tablename__ = 'orders'
    id=db.Column(db.Integer(), primary_key=True)
    order_status=db.Column(db.Enum(OrderStatus),default=OrderStatus.BLUNT)
    service=db.Column(db.Enum(Service),default=Service.WHETTING, nullable=False)
    quantity=db.Column(db.Integer(),default=3,nullable=False)
    total=db.Column(db.Float(), nullable=True)
    date_created_at=db.Column(db.DateTime(),default=datetime.utcnow)

    user_id=db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Order {self.id}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

