#!/usr/bin/env python3

from datetime import datetime

from lxml import etree
from ncclient import manager


class NetworkInterface():

    def __init__(self, host, user, password):
        pass

    def build_configuration_xml(self, name: str, description: str) -> etree.Element():
        """Builds configuration XML for a loopback interface

        Args:
            self (NetworkInterface): NetworkInterface class
            name (str): The name of the interface
            description (str): The description for the interface

        Returns:
            etree.Element: the xml fo rthe created configuration
        """
        xml = etree.Element('config')
        configuration = etree.SubElement(xml, 'interfaces', nsmap={
                                         None: 'urn:ietf:params:xml:ns:yang:ietf-interfaces'})
        interface_cfg = etree.SubElement(configuration, 'interface')
        etree.SubElement(interface_cfg, 'name').text = name
        etree.SubElement(interface_cfg, 'description').text = 'hello world'
        etree.SubElement(interface_cfg, 'type', nsmap={
            'ianaift': 'urn:ietf:params:xml:ns:yang:iana-if-type'}).text = 'anaift:softwareLoopback'
        etree.SubElement(interface_cfg, 'enabled').text = 'true'
        return xml

    def create_loopback_interface():
        pass
