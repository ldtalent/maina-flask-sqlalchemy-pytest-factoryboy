
# Project Title

TODO API endpoints

## Getting Started

### Prerequisites
- Python 3+
- Postgres

### Virtual environment
- Clone the repository to your local machine. 
- Move into the project folder clones
- Create a virtual environment and activate it
- Install all dependecies in the `requirements.txt` using `pip install -r requirements.txt`

### Postgres
Set up postgres on your machine and create a database.

### .env
- Create a .env file that resembles the `.env_example` provided
- Export the variables into the virtual environment

## Running the application
- Run 'flask run` to start up your server


### Migrations
To apply migrations run the following commands:
- `python manage.py db init`
- `python manage.py db migrate`
- `python manage.py db upgrade`

#### Endpoints

|  Method  | Endpoint |  Description |
|---|---|---|
| POST  | /api/v1/todos  | Creates a new todo record  |
| GET  | /api/v1/todos  | Retrieves all todo records in the DB  |
| GET  | /api/v1/todos/<int: id>  | Retrieves a single todo record|
| DELETE  | /api/v1/todos/<int: id>  | Deletes a single todo record based on the id  |
| PATCH  | /api/v1/todos/<int: id>  | Edits parts of a todo record based on the id |

## Running the tests

To run tests use:
- `pytest`


