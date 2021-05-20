# Set base image (host OS)
from ubuntu:latest

# Set one or more individual labels
LABEL version="0.0.1-beta"
LABEL author="muutttu@live.fi"

# Install updates and dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    apt-transport-https \
    sudo  \
    wget \
    curl \
    gnupg \
    zip \
    unzip \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install awscli --upgrade

