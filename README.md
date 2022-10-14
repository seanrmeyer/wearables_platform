# app overview

This repo is the configuration for building a Wearables Data Sharing Platform using FastAPI, Docker, and Postgres.

# URLs

- pgAdmin UI - 127.0.0.1:5050 
- API documentation - 127.0.0.1:8008/docs

# folder contents

- `templates` (folder) - contains html templates for the flask API
- `app` - python code which serves the API
- `docker_compose.sh` - a script to build and start the docker image
- `docker_test_api.sh` - a curl script to test the API once the container is running
- `docker-compose.yml` - config file for building docker image
- `Dockerfile` - docker image build instructions
- `README.md` - this file. a general overview of this app
- `requirements.txt` - required python libraries

# getting started

1. build and start the docker image by running `sh docker_compose.sh`
2. test the API by running `sh docker_test_api.sh`

# Creating a new database

1. open a terminal or shell and type `docker ps`
2. copy the container id for `postgres:13-alpine`
3. type `docker inspect <container_id>`
4. copy `IPAddress` under `networks` (e.g. 172.18.0.2)
5. paste in pgAdmin connection section under "add a server"
6. enter fastapi_traefik as maintenance db, username, and password

# Uploading data

1. Open pgAdmin via web browser
2. Tools > Storage Manager > Upload (icon)

Note: To increase file upload capacity, go to File > Storage > Options within pgAdmin UI

# Importing data

1. Select the wearables database
2. Use Tools -> Import/Export data to upload binary (.bin), comma separated values (.csv), or text files (.txt)
3. Columns to import must match by order of table

