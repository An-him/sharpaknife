from flask_restx import Namespace,Resource, fields
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.orders import Order
from ..models.users import User
from ..utils import db



order_namespace=Namespace("orders", description="Namespace for Orders")

order_model=order_namespace.model(
    'Order',{
        'id':fields.Integer(description='An ID'),
        'quantity':fields.Integer(required=False,description='Quantity of the order'),
        'username':fields.String(description='User name of client'),
        'service':fields.String(required=True,description='Service to be provided'),
        'date_created_at':fields.DateTime(description='Date created'),
        'order_status':fields.String(description='Status of the order',
            enum=['BLUNT','WHETTING','SHARPENING','SHARP']),
    }
)

order_status_model=order_namespace.model(
    'OrderStatus',{
        'order_status':fields.String(description='Status of the order',
            enum=['BLUNT','WHETTING','SHARPENING','SHARP']),
    }
)

order_status_models_list=order_namespace.model(
    'Order',{
        'id':fields.Integer(description='An ID'),
        'quantity':fields.Integer(required=False,description='Quantity of the order'),
        'user_id':fields.Integer(description='User ID'),
        'username':fields.String(description='User name of client'),
        'date_created_at':fields.DateTime(description='Date created'),
        'service':fields.String(required=True,description='Service to be provided'),
        'order_status':fields.String(description='Status of the order',
            enum=['BLUNT','WHETTING','SHARPENING','SHARP']),
    }
)
@order_namespace.route("/orders/")
class OrderGetCreate(Resource):


    @order_namespace.marshal_with(order_model)
    @order_namespace.doc(description="Retrieves all orders")
    @jwt_required()
    def get(self):
        """
        Get all orders
        """
        orders=Order.query.all()
        return orders, HTTPStatus.OK

    @order_namespace.expect(order_model)
    @order_namespace.marshal_with(order_model)
    @order_namespace.doc(description="Place an order")
    @jwt_required()
    def post(self):
        """
            Place a new order
        """

        username=get_jwt_identity()

        current_user=User.query.filter_by(username=username).first()
        data=order_namespace.payload

        new_order=Order(
            quantity=data['quantity'],
        )
        new_order.client=current_user
    

        new_order.save()

        return new_order, HTTPStatus.CREATED

@order_namespace.route("/orders/<int:order_id>")
class GetUpdateDeleteOrder(Resource):

    @order_namespace.marshal_with(order_status_models_list)
    @order_namespace.doc(
        description="Place an order",
        params={
            'order_id':'An ID for a given order'
        }
        )
    @jwt_required()
    def get(self,order_id):
        """
            Retrieves an order by id
        """
        order=Order.get_by_id(order_id)
        order.customer_name=order.client.username


        return order, HTTPStatus.OK
    
    @order_namespace.expect(order_model)
    @order_namespace.marshal_with(order_model)
    @order_namespace.doc(
        description="Update an order",
        params={
            'order_id':'An ID for a given order'
        }
        )
    @jwt_required()
    def put(self,order_id):
        """
            Update an order by id
        """
        order_to_update=Order.get_by_id(order_id)

        data=order_namespace.payload

        order_to_update.quantity=data['quantity']
        order_to_update.service=data['service']
        order_to_update.order_status=data['order_status']


        db.session.commit()

        return order_to_update, HTTPStatus.OK
    
    @jwt_required()
    @order_namespace.doc(
        description="Delete an order",
        params={
            'order_id':'An ID for a given order'
        }
        )
    def delete(self,order_id):
        """
            Delete an order by id
        """
        order_to_delete=Order.get_by_id(order_id)

        order_to_delete.delete()

        return order_to_delete, HTTPStatus.NO_CONTENT


@order_namespace.route("/user/<int:user_id>/order/<int:order_id>/")
class GetSpecificOrderByUser(Resource):

    @order_namespace.marshal_with(order_model)
    @order_namespace.doc(
        description="Get a specific order by a user ID",
        params={
            "user_id":"An ID for a given user",
            "order_id":"A user's for a given order"
        }
        )
    @jwt_required()
    def get(self,user_id,order_id):
        """
            Get all Orders by specific users
        """
        user=User.get_by_id(user_id)

        order=Order.query.filter_by(id=order_id).filter_by(client=user).first()

        return order, HTTPStatus.OK



@order_namespace.route("/user/<int:user_id>/orders")
class UserOrders(Resource):


    @order_namespace.marshal_list_with(order_model)
    @order_namespace.doc(
        description="Get all orders of a user",
        params={
            'user_id':'An ID for a given user'
        }
        )
    @jwt_required()
    def get(self,user_id):
        """
            Gets all orders of a Specified user
        """
        user=User.get_by_id(user_id)

        orders=user.orders
        Order.customer_name=user.username

        return orders, HTTPStatus.OK

@order_namespace.route("/status/<int:order_id>")
class UpdateOrderStatus(Resource):


    @order_namespace.expect(order_status_model)
    @order_namespace.marshal_with(order_model)
    @order_namespace.doc(
        description="Update order's status given the ID",
        params={
            'order_id':'An ID for a given order'
        }
        )
    @jwt_required()
    def patch(self, order_id):
        """
            Update order's status
        """
        data=order_namespace.payload

        order_to_update=Order.get_by_id(order_id)


        order_to_update.order_status=data['order_status']

        db.session.commit()

        return order_to_update, HTTPStatus.OK