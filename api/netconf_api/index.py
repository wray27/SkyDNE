#!/usr/bin/env python3
import logging
from flask import Flask, jsonify, request
from ncclient import manager

from .utilities.netconf_server import NetconfServer

app = Flask(__name__)

def get_device_info():
    return {
        'host': request.args.get('host', 'localhost', type=str),
        'username': request.args.get('username'),
        'password': request.args.get('password')
    }


@app.route("/add", methods=['POST'])
def create_interface():
    device = NetconfServer(**get_device_info())
    name = request.json.get('name')
    description  = request.json.get('description')
    return device.create_loopback(name, description)


@app.route("/list", methods=['GET'])
def get_interfaces():
    device = NetconfServer(**get_device_info())
    return device.list_interfaces()


@app.route("/delete", methods=['DELETE'])
def delete_interface():
    device = NetconfServer(**get_device_info())
    interface_name = request.args.get('interface_name')
    return device.delete_loopback(interface_name)


@app.route("/capabilities", methods=['GET'])
def get_capabillities():
    device = NetconfServer(**get_device_info())
    return jsonify(device.capabilities())
