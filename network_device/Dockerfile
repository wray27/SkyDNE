FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

# update package repository list
RUN apt-get update -y  && \
    apt-get upgrade -y

# install ssh and netconf
RUN apt-get install -y openssh-server \
    netconfd \
    vim

# create test user
RUN useradd -rm -d /home/test -s /bin/bash -g root -G sudo -u 1000 test
RUN usermod -G root test
RUN usermod -g 0 -o

RUN echo 'test:test' | chpasswd

# configures ssh for netconf
RUN printf "Port 22\nPort 830\nSubsystem netconf /usr/sbin/netconf-subsystem" >> /etc/ssh/sshd_config

COPY ./iana-if-type.yang /usr/share/yuma/modules/ietf
COPY ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh

ENTRYPOINT  ["./entrypoint.sh"]