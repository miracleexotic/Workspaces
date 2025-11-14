# syntax=docker/dockerfile:1
#
# Ubuntu Dockerfile
#
# https://github.com/dockerfile/ubuntu
#

# Pull base image.
FROM ubuntu:22.04

#
# Initial OS
#

# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y curl git htop man unzip vim wget iputils-ping net-tools openssh-server sudo

# Supervisord
RUN \
  apt-get update && \
  apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#
# JBOSS
#

# Install Java version 8
RUN \
  apt-get install -y openjdk-8-jdk-headless openjdk-8-jre-headless 

# Verify the installation
RUN java -version && javac -version

# Create JBOSS directoies
RUN \
  mkdir /opt/JBOSS && \
  mkdir /opt/JBOSS/JBOSSMAIN /opt/JBOSS/JBDOMAIN /opt/JBOSS/Slave1 /opt/JBOSS/Slave2

# Download JBOSS file
WORKDIR /opt/JBOSS/JBOSSMAIN
RUN \
  wget https://download.jboss.org/wildfly/10.0.0.Final/wildfly-10.0.0.Final.zip && \
  unzip wildfly-10.0.0.Final.zip

# Create User & Group
COPY ./JBOSSMAIN/wildfly-10.0.0.Final/domain/configuration/mgmt-users.properties /opt/JBOSS/JBOSSMAIN/wildfly-10.0.0.Final/domain/configuration/
COPY ./JBOSSMAIN/wildfly-10.0.0.Final/domain/configuration/mgmt-groups.properties /opt/JBOSS/JBOSSMAIN/wildfly-10.0.0.Final/domain/configuration/

# Connect Java trace data with logs for Splunk Observability Cloud
COPY ./JBOSSMAIN/wildfly-10.0.0.Final/domain/configuration/logging.properties /opt/JBOSS/JBOSSMAIN/wildfly-10.0.0.Final/domain/configuration/

# Copy domain configuration file
RUN \
  cp -rp /opt/JBOSS/JBOSSMAIN/wildfly-10.0.0.Final/domain /opt/JBOSS/JBDOMAIN && \ 
  cp -rp /opt/JBOSS/JBOSSMAIN/wildfly-10.0.0.Final/domain /opt/JBOSS/Slave1 && \ 
  cp -rp /opt/JBOSS/JBOSSMAIN/wildfly-10.0.0.Final/domain /opt/JBOSS/Slave2 

# Copy configuration file
COPY ./JBDOMAIN/domain/configuration/domain.xml /opt/JBOSS/JBDOMAIN/domain/configuration
COPY ./JBDOMAIN/domain/configuration/host-master.xml /opt/JBOSS/JBDOMAIN/domain/configuration
COPY ./Slave1/domain/configuration/host-slave.xml /opt/JBOSS/Slave1/domain/configuration
COPY ./Slave2/domain/configuration/host-slave.xml /opt/JBOSS/Slave2/domain/configuration

#
# o11y Java Agent
#

# Install o11y-java-agent
WORKDIR /opt/o11y/java-agent
RUN \
  curl -L https://github.com/signalfx/splunk-otel-java/releases/latest/download/splunk-otel-javaagent.jar -o splunk-otel-javaagent.jar

# Copy domain.conf inject o11y-java-agent
COPY ./JBOSSMAIN/domain.conf /opt/JBOSS/JBOSSMAIN/wildfly-10.0.0.Final/bin

# Install IM monitor
WORKDIR /opt/splunk-otel-collector
RUN \
  wget https://github.com/signalfx/splunk-otel-collector/releases/download/v0.139.2/otelcol_linux_amd64 -O otelcol && \

COPY ./splunk-otel-collector-agent/agent_config.yaml /opt/splunk-otel-collector
  
WORKDIR /opt

EXPOSE 9990

CMD ["/usr/bin/supervisord"]

