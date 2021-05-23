# Set base image (host OS)
FROM amazonlinux:2

# Author labels
LABEL version="0.0.1-beta"
LABEL author="muutttu@live.fi"

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# Author
LABEL maintainer="AWS IoT Greengrass"

# Replace the args to lock to a specific version
ARG GREENGRASS_RELEASE_VERSION=2.1.0
ARG GREENGRASS_ZIP_FILE=greengrass-${GREENGRASS_RELEASE_VERSION}.zip
ARG GREENGRASS_RELEASE_URI=https://d2s8p88vqu9w66.cloudfront.net/releases/${GREENGRASS_ZIP_FILE}
ARG GREENGRASS_ZIP_SHA256=${GREENGRASS_ZIP_FILE}.sha256

# Set up Greengrass v2 execution parameters
# https://docs.aws.amazon.com/greengrass/v2/developerguide/build-greengrass-dockerfile.html
# TINI_KILL_PROCESS_GROUP allows forwarding SIGTERM to all PIDs in the PID group so Greengrass can exit gracefully
ENV TINI_KILL_PROCESS_GROUP=1 \ 
    # The path to the folder within the container to use as the root for AWS IoT Greengrass Core software:
    GGC_ROOT_PATH=/greengrass/v2 \
    # Determines whether the AWS IoT Greengrass Core provisions AWS resources:
    PROVISION=true \
    # The AWS Region that the AWS IoT Greengrass Core software uses:
    AWS_REGION=eu-central-1 \
    # The name of the AWS IoT thing that you register as this core device:
    THING_NAME=GreengrassCore1-a \
    # The name of the AWS IoT thing group where you add this core device's AWS IoT:
    THING_GROUP_NAME=GreengrassCoreGroup1 \
    # The name of the IAM role to use to acquire AWS credentials:
    TES_ROLE_NAME=GreengrassV2TokenExchangeRole \
    # The name of the AWS IoT role alias that points to the IAM role that provides AWS credentials:
    TES_ROLE_ALIAS_NAME=GreengrassV2TokenExchangeRoleAlias \
    # The name or ID of the system user and group that the AWS IoT Greengrass Core software uses to run components:
    COMPONENT_DEFAULT_USER=ggc_user:ggc_group \
    # Defines whether to download and deploy the Greengrass CLI component in the container image:
    DEPLOY_DEV_TOOLS=true \
    # The path to the configuration file to use to install the AWS IoT Greengrass Core software:
    INIT_CONFIG=/tmp/config/config.yaml
RUN env

# Entrypoint script to install and run Greengrass
COPY "greengrass-entrypoint.sh" /
COPY "${GREENGRASS_ZIP_SHA256}" /

# Install Greengrass v2 dependencies
RUN yum update -y && yum install -y python37 tar unzip wget sudo procps which && \
    amazon-linux-extras enable python3.8 && yum install -y python3.8 java-11-amazon-corretto-headless && \
    wget $GREENGRASS_RELEASE_URI && sha256sum -c ${GREENGRASS_ZIP_SHA256} && \
    rm -rf /var/cache/yum && \
    chmod +x /greengrass-entrypoint.sh && \
    mkdir -p /opt/greengrassv2 $GGC_ROOT_PATH && unzip $GREENGRASS_ZIP_FILE -d /opt/greengrassv2 && rm $GREENGRASS_ZIP_FILE && rm $GREENGRASS_ZIP_SHA256

ENTRYPOINT ["/greengrass-entrypoint.sh"]