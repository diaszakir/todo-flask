# TODO list

First version of TODO list application REST API created on Flask.

## Endpoints:

- GET `/tasks` - Shows user all tasks
- GET `/tasks/task_id` - Shows user exact task by id
- POST `/tasks` - Creates new task
- PUT `/tasks/task_id` - Updates task name and status
- PATCH `/tasks/task_id` - Updates only task status
- DELETE `/tasks/task_id` - Deletes task

## How to run

For the first version you can launch application type in terminal

```
flask run
```

## How to use

Use Postman/Insomnia/Bruno or other testing applications

## Planned to add:

- Database
- Authorization
- Swagger-UI for documentation
- Frontend
