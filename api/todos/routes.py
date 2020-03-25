from flask import Blueprint
from flask_restful import Api
from .views import TodosViews, TodoModificationViews


todo_bp = Blueprint('todos', __name__, url_prefix='/api/v1')

api = Api(todo_bp)

api.add_resource(TodosViews, '/todos')
api.add_resource(TodoModificationViews, '/todos/<int:todo_id>')