#!/bin/bash

service ssh start
netconfd --log-level=debug --module="/usr/share/yuma/modules/ietf/ietf-interfaces@2014-05-08.yang" \
    --module="/usr/share/yuma/modules/ietf/iana-if-type.yang"