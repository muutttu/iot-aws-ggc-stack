# Set base image (host OS)
FROM python:3.9-slim-buster

# Set one or more individual labels
LABEL version="0.0.1-beta"
LABEL author="muutttu@live.fi"

# Set environment variables in the container
ENV LANG C.UTF-8

# By default, listen on port 5000 (Flask)
#EXPOSE 5000/tcp

# Creates and sets the working directory in the container for further commands
WORKDIR /app

# Copy the dependencies file to the current working directory
COPY requirements.txt .

# Install any dependencies
RUN apt -y update
RUN apt -y install python3-pip build-essential
RUN pip3 install -r requirements.txt

# Copy the app.py file to the current working directory
COPY app.py .

# Specify the command to run on container start
#CMD ["app.py"]
#WORKDIR /
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "-t", "360", "--reload", "wsgi:app"]
#CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]

# Sets the image’s main command
#ENTRYPOINT ["python3"]
#ENTRYPOINT ["gunicorn"]