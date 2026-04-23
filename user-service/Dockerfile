# Base image
FROM python:3.10

# Set working dir
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install fastapi uvicorn sqlalchemy python-jose passlib[bcrypt]

# Run app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]