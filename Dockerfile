# Dockerfile

# pull the official docker image
FROM python:3.9.4-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
# RUN pip3 install asyncpg --no-binary :all:
RUN pip3 install -r requirements.txt

# copy project
COPY . .
