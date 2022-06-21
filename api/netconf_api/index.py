#!/usr/bin/env python3

import os
import logging

from flask import Flask, Response, jsonify, request, abort
from ncclient import manager

from utilities.netconf_server import NetconfServer

app = Flask(__name__)

def get_device_info():
    return {
        'host': request.args.get('host', 'localhost', type=str),
        'username': request.args.get('username'),
        'password': request.args.get('password')
    }


def require_interface_name(interface_name):
    if not interface_name:
        return abort(400, 'interface name is required')


@app.route("/add", methods=['POST'])
def create_interface():
    device = NetconfServer(**get_device_info())
    interface_name = request.json.get('name')
    require_interface_name(interface_name)
    description  = request.json.get('description')
    return device.create_loopback(interface_name, description)


@app.route("/list", methods=['GET'])
def get_interfaces():
    device = NetconfServer(**get_device_info())
    return device.list_interfaces()


@app.route("/delete", methods=['DELETE'])
def delete_interface():
    device = NetconfServer(**get_device_info())
    interface_name = request.args.get('interface_name')
    require_interface_name(interface_name)
    return device.delete_loopback(interface_name)


@app.route("/capabilities", methods=['GET'])
def get_capabillities():
    device = NetconfServer(**get_device_info())
    return jsonify(device.capabilities())


if __name__ == "__main__":
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
