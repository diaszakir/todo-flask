# TODO list

First version of TODO list application REST API created on Flask.

## Updates:

- Added `SQLAlchemy` ORM
- Added migrations using `flask_migrations` and `alembic`

## Endpoints:

- GET `/tasks` - Shows user all tasks
- GET `/tasks/task_id` - Shows user exact task by id
- POST `/tasks` - Creates new task
- PUT `/tasks/task_id` - Updates task name and status
- PATCH `/tasks/task_id` - Updates only task status
- DELETE `/tasks/task_id` - Deletes task
- POST `/register` - Register new user

## How to run

First, you need to create python virtual environment

```
python -m venv .venv
```

Second, you need to install required libraries

```
pip install -r requirements.txt
```

Third, you need to initialize database

```
flask db init
```

Fourth, make migration

```
flask db migrate
```

After

```
flask db upgrade
```

Next create JWT Secret Key in jwt_generate.py and paste it in your .env

```
python jwt_generate.py
```

For the first version you can launch application type in terminal

```
flask run
```

If you want use other database (MySQL, PostgreSQL and etc.) you should add connection with .env file

## Accessing Swagger-UI

Type on browser `localhost:5000/docs` to see API documentation

## How to use

Use Postman/Insomnia/Bruno or other testing applications

## Planned to add:

- Authorization
- Frontend
