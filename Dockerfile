#Pulling the base image
FROM python:3.8-slim-buster


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY . .

RUN  pip install -r requirements.txt

# RUN  apt-get update && apt-get install -y libmagic-dev

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

# Run server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]