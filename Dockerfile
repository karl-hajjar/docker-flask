FROM python:3.9-slim-buster

WORKDIR /docker-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "main.py"]

# docker build --tag image_name .
# docker run -p container_port_on_machine:app_port_in_container -d image_name
# e.g., docker run -p 5000:5000 -d image_name
# docker stop container_id
# docker rm container_id
# docker rmi image_name
# docker rm $(docker ps -a -f status=exited -q) --> REMOVING exited containers

# Expected ~/.docker/config.json JSON config
#{
#	"auths": {},
#	"credStore": "desktop",
#	"currentContext": "desktop-linux"
#}