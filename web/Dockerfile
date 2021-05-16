# Set base image (host OS)
FROM python:3.9-slim-buster

ENV LANG C.UTF-8

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to leverage Docker cache
#COPY ./requirements.txt /app/requirements.txt
# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN apt-get -y update
RUN apt-get install -y python3-pip build-essential
RUN pip install -r requirements.txt
#RUN pip3 install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY app.py .
#COPY . /app

# Specify the command to run on container start
CMD [ "python", "./app.py" ]
#CMD ["app.py"]

ENTRYPOINT ["python3"]
