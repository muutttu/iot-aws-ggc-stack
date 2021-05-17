# Set base image (host OS)
FROM python:3.9-slim-buster

# Set environment variables in the container
ENV LANG C.UTF-8

# By default, listen on port 5000 (Flask)
EXPOSE 5000/tcp

# Creates and sets the working directory in the container for further commands
WORKDIR /app

# Copy the dependencies file to the current working directory
COPY requirements.txt .

# Install any dependencies
RUN apt -y update
RUN apt -y install python3-pip build-essential
RUN pip install -r requirements.txt

# Copy the app.py file to the current working directory
COPY app.py .

# Specify the command to run on container start
CMD ["app.py"]

# Sets the image’s main command
ENTRYPOINT ["python3"]