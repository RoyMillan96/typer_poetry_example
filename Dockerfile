# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY pyproject.toml poetry.lock /app/

# Install Poetry and your project dependencies
RUN pip install poetry && poetry install

# Copy your Python application code to the container
COPY . /app

# Install cron
RUN apt-get update && apt-get -y install cron

# Add a cron job
COPY cron-job /etc/cron.d/my-cron-job
RUN chmod 0644 /etc/cron.d/my-cron-job

# Apply cron job
RUN crontab /etc/cron.d/my-cron-job

# Command to run your Python application and start cron in the foreground
CMD service cron start && poetry run python cron_service_cleaner.py

# Definir variables de entorno
ENV apikey='kxiSQEbqAlvHjVWA8NRVbpXUGfilvuGq'