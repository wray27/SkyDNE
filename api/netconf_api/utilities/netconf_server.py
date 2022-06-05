#!/usr/bin/env python3

from datetime import datetime

import xmltodict
from lxml import etree
from ncclient import manager


class NetconfServer():

    def __init__(self, host, username, password, port=830):
        self.manager = manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False
        )

    def list_interfaces(self):
        print("Sending a <get-config> operation to the device.\n")
        netconf_filter = """
            <filter>
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface></interface>
            </interfaces>
            </filter>"""
        response = self.manager.get_config(source='running', filter=netconf_filter)
        interfaces = xmltodict.parse(response.xml)
        return interfaces

    def create_configuration_xml(self, name: str, description: str):
        return f"""
        <config>
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                    <name>{name}</name>
                    <description>{description}</description>
                    <enabled>true</enabled>
                </interface>
            </interfaces>
        </config>
        """

    def delete_configuration_xml(self, name: str):
        return f"""
        <config>
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface operation="delete">
                    <name>{name}</name>
                </interface>
            </interfaces>
        </config>
        """

    def create_loopback(self, name, description):
        response = self.manager.edit_config(
            config=self.create_configuration_xml(name, description))
        return str(response)

    def delete_loopback(self, name):
        response = self.manager.edit_config(
            config=self.delete_configuration_xml(name), target='running')
        return str(response)

    def capabilities(self):
        return list(self.manager.server_capabilities)

