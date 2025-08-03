# TODO list

First version of TODO list application REST API created on Flask.

## Updates:

- Added flask_smorest
- Added Swagger-UI for API documentation

## Endpoints:

- GET `/tasks` - Shows user all tasks
- GET `/tasks/task_id` - Shows user exact task by id
- POST `/tasks` - Creates new task
- PUT `/tasks/task_id` - Updates task name and status
- PATCH `/tasks/task_id` - Updates only task status
- DELETE `/tasks/task_id` - Deletes task

## How to run

First you need to create python virtual environment

```
python -m venv .venv
```

Second you need to install required libraries

```
pip install -r requirements.txt
```

For the first version you can launch application type in terminal

```
flask run
```

## Accessing Swagger-UI

Type on browser `localhost:5000/docs` to see API documentation

## How to use

Use Postman/Insomnia/Bruno or other testing applications

## Planned to add:

- Database
- Authorization
- Schemas
- Frontend
