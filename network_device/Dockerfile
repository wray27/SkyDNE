FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

# update package repository list
RUN apt-get update -y  && \
    apt-get upgrade -y

# install python/pip
RUN apt-get install -y python3 \
    python3-pip \
    vim

RUN apt-get install -y openssh-server

# install netconf
RUN python3 -m pip install netconf

# create test user
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 test
RUN  echo 'test:test' | chpasswd

# start ssh
RUN service ssh start

# keeps the container running
CMD ["/usr/sbin/sshd", "-D"]