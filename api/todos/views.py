from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from .models import TodoModel
from .schema import TodoSchema, TodosEditSchema
from api import db


class TodosViews(Resource):

    def post(self):
        try:
            schema = TodoSchema()
            todo_data = schema.load(request.get_json())
            todo_instance = TodoModel(**todo_data)
            db.session.add(todo_instance)
            db.session.commit()
            return schema.dump(todo_data), 201
        except ValidationError as err:
            return dict(error=err.messages, status_code=400), 400

    def get(self):
        try:
            todo_list = TodoModel.query.all()
            schema = TodoSchema(many=True)
            return schema.dump(todo_list), 200
        except Exception as e:
            return dict(error=str(e), status_code=400), 400

class TodoModificationViews(Resource):
    def get(self, todo_id):
        try:
            todo_record = TodoModel.query.get(todo_id)
            schema = TodoSchema()
            return schema.dump(todo_record), 200
        except Exception as e:
            return dict(error=str(e), status_code=404), 404

    def patch(self, todo_id):
        try:
            todo_record = TodoModel.query.get(todo_id)
            request_data = TodosEditSchema().load(request.get_json())
            todo_record.from_date = request_data[
                "from_date"] if "from_date" in request_data.keys() else todo_record.from_date
            todo_record.to_date = request_data[
                "to_date"] if "to_date" in request_data.keys() else todo_record.to_date
            todo_record.description = request_data[
                "description"] if "description" in request_data.keys() else todo_record.description
            todo_record.completed = request_data[
                "completed"] if "completed" in request_data.keys() else todo_record.completed
            todo_record.title = request_data[
                "title"] if "title" in request_data.keys() else todo_record.title
            db.session.commit()
            return TodosEditSchema().dump(todo_record), 200
        except ValidationError as err:
            return dict(error=err.messages, status_code=400), 400

    def delete(self, todo_id):
        try:
            todo_record = TodoModel.query.get(todo_id)
            db.session.delete(todo_record)
            db.session.commit()
            return {"message": "Todo Record Deleted Successfully"}, 200
        except Exception as err:
            return dict(error=str(err), status_code=404), 404
