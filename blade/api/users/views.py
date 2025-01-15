from ..models.users import User
from flask_restx import Resource,Namespace,fields
from ..models.users import User
from ..utils import db


users_namespace=Namespace("users", description="namespace for User operations")

user_model=users_namespace.model(
    'User',{
        'id':fields.Integer(description='An ID'),
        'username':fields.String(description='Username'),
        'email':fields.String(description='Email'),
        'location':fields.String(description='Location'),
        'is_staff':fields.Boolean(description='Staff status'),
        'is_active':fields.Boolean(description='Active status'),
        'created_at':fields.DateTime(description='Date created'),
        'updated_at':fields.DateTime(description='Date updated'),
    }
)

@users_namespace.route("/users/")
class UserResource(Resource):
    def get():
        pass