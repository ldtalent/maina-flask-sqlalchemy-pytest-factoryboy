import json
import datetime
from .factories import TodoFactory

def test_user_can_retrieve_empty_list_todos(client, db):
    response = client.get('/api/v1/todos')
    response_body = response.get_json()
    assert response.status == '200 OK'
    assert len(response_body) == 0

def test_user_can_create_a_todo(client, db):
    todo = {
            "title": "Write tests for api",
	     "description": "Write tests for todo api",
	     "from_date": "2020-02-01T00:00:00",
	     "to_date": "2020-02-02T00:00:00",
	      "completed": False
	     }
    response = client.post('/api/v1/todos', 
                            headers={'Content-Type': 'application/json'},
                             data=json.dumps(todo),
                             )
    assert response.status == '201 CREATED'
    assert response.get_json() == todo

def test_user_can_edit_existing_todo(client, db):
    TodoFactory(id=1)
    edit_data = {"title": "Cool vacation to Mombasa"}
    response = client.patch('api/v1/todos/1', 
                            headers={'Content-Type': 'application/json'},
                             data=json.dumps(edit_data))
    assert response.status == '200 OK'
    assert response.get_json()["title"] == edit_data["title"]

def test_user_can_delete_existing_todo(client, db):
    TodoFactory(id=1)
    response = client.delete('api/v1/todos/1', 
                            headers={'Content-Type': 'application/json'})
    assert response.status == '200 OK'
    assert response.get_json()["message"] == "Todo Record Deleted Successfully"