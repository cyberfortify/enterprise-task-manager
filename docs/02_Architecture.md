# Architecture Design

## Overview

The application follows a microservices architecture:

* User Service → Handles authentication and user management
* Task Service → Manages task-related operations
* API Gateway → Routes requests to appropriate services

## Architecture Flow

Client → API Gateway → Services → Database

## Key Design Decisions

* Separation of concerns using microservices
* Stateless authentication using JWT
* Centralized routing via API Gateway
* Lightweight database using SQLite for simplicity
