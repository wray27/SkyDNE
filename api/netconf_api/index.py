#!/usr/bin/env python3
import logging
from flask import Flask, jsonify
from ncclient import manager

from .utilities.netconf_server import NetconfServer

app = Flask(__name__)

@app.route("/add")
def create_interface():
    logging.basicConfig(level=logging.DEBUG)
    device = NetconfServer(
        host='localhost', username='root', password='')
    return device.create_loopback('lo2', '')


@app.route("/list")
def get_interfaces():
    logging.basicConfig(level=logging.DEBUG)
    device = NetconfServer(
        host='localhost', username='root', password='test')
    return device.list_interfaces()


@app.route("/delete")
def delete_interface():
    logging.basicConfig(level=logging.DEBUG)
    device = NetconfServer(
        host='localhost', username='root', password='test')
    return device.delete_loopback('test')


@app.route("/capabilities")
def get_capabillities():
    logging.basicConfig(level=logging.DEBUG)
    device = NetconfServer(
        host='localhost', username='root', password='test')
    return jsonify(device.capabilities())
