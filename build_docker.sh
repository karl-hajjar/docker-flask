#!/bin/bash

# First check docker config and modify if needed
source env/bin/activate
python3 check_docker_config_job.py
cat ~/.docker/config.json

# Then build image
imagename="python-docker"
echo "Building docker image"
docker build --tag $imagename .

# Finally run container
dockerport=5000
if [ -z "$1" ]; then flaskport=5000; else flaskport=$1; fi # set port to 5000 if not specified as argument
echo "Using port $dockerport for docker container and port $flaskport for flask app"

echo "Running container"
# docker run -p $dockerport:$flaskport -d $imagename
docker run -p $flaskport:$dockerport -d $imagename