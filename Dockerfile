# Define a base stage that uses the official python runtime base image
FROM python:3.12.10-slim-bullseye AS base

ENV FLASK_APP=prom.py
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONUNBUFFERED=1

# Add curl for healthcheck
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl

# Set the application directory
WORKDIR /usr/local/app

# Install our requirements.txt
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy our code from the current folder to the working directory inside the container
COPY . .

# Make port 80 available for links and/or publish
EXPOSE 8080

# Define our command to be run when launching the container
CMD ["gunicorn", "-b", "0.0.0.0:8080", "-w", "2", "prom:app"]
