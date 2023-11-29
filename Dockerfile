FROM python:3.9-slim-buster

WORKDIR /docker-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "main.py"]

# docker build --tag image_name .
# docker run -p container_port_on_machine:app_port_in_container image_name -d
# e.g., docker run -p 5000:5000 image_name -d
# docker stop container_id
# docker rm container_id
# docker rmi image_name