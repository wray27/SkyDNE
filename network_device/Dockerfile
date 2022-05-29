FROM ubuntu:20.04

# update package repository list
RUN apt-get update -y  && \
    apt-get upgrade -y

# install python/pip
RUN apt-get -y python3 \
    python3-pip

# install netconf
RUN python3 -m pip install netconf

# keeps the container running
ENTRYPOINT ["tail", "-f", "/dev/null"]