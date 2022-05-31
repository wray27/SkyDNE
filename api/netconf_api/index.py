#!/usr/bin/env python3
import logging
from flask import Flask
from ncclient import manager

from .utilities.netconf_server import NetconfServer

app = Flask(__name__)

@app.route("/add")
def create_interface():
    logging.basicConfig(level=logging.DEBUG)
    device = NetconfServer(
        host='localhost', username='test', password='test')
    return device.create_loopback_interface('testInterface', '')


@app.route("/get")
def get_interfaces():
    logging.basicConfig(level=logging.DEBUG)
    device = NetconfServer(
        host='localhost', username='test', password='test')
    return device.list_interfaces()
