# Deployment Guide

## Local Setup

1. Clone the repository
2. Create virtual environment
3. Install dependencies
4. Run services using uvicorn

## Commands

uvicorn user_service.main:app --port 8001
uvicorn task_service.main:app --port 8002
uvicorn api_gateway.main:app --port 8000

## CI/CD

GitHub Actions is used to automatically run tests on every push.
