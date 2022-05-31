#!/usr/bin/env python3

from datetime import datetime

from lxml import etree
from ncclient import manager
import xmltodict
from netconf_client.connect import connect_ssh
from netconf_client.ncclient import Manager


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


    def build_configuration_xml(self, name: str, description: str):
        """Builds configuration XML for a loopback interface

        Args:
            name (str): The name of the interface
            description (str): The description for the interface

        Returns:
            etree.Element: the xml for the created configuration
        """
        # xml = etree.Element(
        #     'config', nsmap={None: 'urn:ietf:params:xml:ns:netconf:base:1.0'})
        # configuration = etree.SubElement(xml, 'interfaces', nsmap={
        #                                  'ianaift': 'run:ietf:params:xml:ns:yang:iana-if-type'})
        # interface_cfg = etree.SubElement(configuration, 'interface')
        # etree.SubElement(interface_cfg, 'name').text = name
        # etree.SubElement(interface_cfg, 'description').text = description
        # etree.SubElement(interface_cfg, 'type', nsmap={
        #     'ianaift': 'urn:ietf:params:xml:ns:yang:iana-if-type'}).text = 'anaift:softwareLoopback'
        # etree.SubElement(interface_cfg, 'enabled').text = 'true'
        # return xml
        return f"""<config>
            <interfaces xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                <interface>
                    <name>{name}</name>
                    <description>{description}</description>
                    <enabled>true</enabled>
                    <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                        ianaift:softwareLoopback
                    </type>
                    <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                        <address>
                            <ip>0.0.0.0</ip>
                            <netmask>255.255.255.0</netmask>
                        </address>
                    </ipv4>
                </interface>
            </interfaces>
        </config>
        """

    def create_loopback(self, name, description):
        print("Sending a <edit-config> operation to the device  .\n")
        response = self.manager.edit_config(config=self.build_configuration_xml('test', ''),
                                    target='running')
        return str(response)
