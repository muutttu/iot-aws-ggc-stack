FROM python:3.9-slim-buster

ENV LANG C.UTF-8

# Copy requirements.txt to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN apt-get -y update
RUN apt-get install -y python3-pip build-essential
RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]

CMD ["app.py"]
