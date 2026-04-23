# API Documentation

## Authentication APIs

POST /signup

* Registers a new user

POST /login

* Returns JWT token

## Task APIs

POST /tasks

* Create a task

GET /tasks

* Fetch user tasks

PUT /tasks/{id}

* Update task

DELETE /tasks/{id}

* Delete task

## Authentication

All protected APIs require:

Authorization: Bearer <token>
