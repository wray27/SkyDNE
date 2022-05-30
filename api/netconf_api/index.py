#!/usr/bin/env python3

from flask import Flask

from .utilities.etwork_interface import NetworkInterface

app = Flask(__name__)

@app.route("/configure_interface")
def configure_interface():
    return ''