# 🏢 Enterprise Task Management System

A production-ready microservices-based task management system built using FastAPI, implementing enterprise architecture patterns, authentication, CI/CD, and testing.

 

## 🚀 Features

* 🔐 JWT Authentication (Login/Signup)
* 🧩 Microservices Architecture
* 📦 API Gateway Implementation
* 📝 Task Management (CRUD)
* 🧪 Automated Testing (Pytest)
* ⚙️ CI/CD Pipeline (GitHub Actions)
* 📄 API Documentation (Swagger)

 

## 🏗️ Architecture

* **User Service** → Authentication & User Management
* **Task Service** → Task Operations
* **API Gateway** → Request Routing

 

## 🛠️ Tech Stack

* Python (FastAPI)
* SQLAlchemy (SQLite)
* JWT Authentication
* Pytest
* GitHub Actions

 

## ▶️ Setup Instructions

```bash
git clone <your-repo>
cd enterprise-task-manager
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Run services:

```bash
uvicorn user_service.main:app --port 8001
uvicorn task_service.main:app --port 8002
uvicorn api_gateway.main:app --port 8000
```

 

## 🧪 Run Tests

```bash
pytest
```

 

## 📌 API Docs

* User Service → http://127.0.0.1:8001/docs
* Task Service → http://127.0.0.1:8002/docs
* API Gateway → http://127.0.0.1:8000/docs

 

## 🎯 Highlights

* Designed scalable microservices architecture
* Implemented secure JWT-based authentication
* Integrated CI/CD pipeline for automated testing
* Achieved modular and maintainable code structure

 

## 💼 Author

Aditya Vishwakarma
