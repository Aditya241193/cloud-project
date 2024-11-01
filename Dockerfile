# Use a lightweight Python image
FROM python:3.9-slim

# Set environment variables to prevent Python from generating .pyc files and to buffer output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
RUN pip install django

# Copy the application code to the container
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Run Gunicorn with the WSGI application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

