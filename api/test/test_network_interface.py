#!/usr/bin/env python3
import os
import unittest

from lxml import etree

from netconf_api.utilities.network_interface import NetworkInterface


class TestNetworkInterface(unittest.TestCase):

    def setUp(self):
        self.interface = NetworkInterface('', '', '')

    def test_build_configration_xml(self):
        xml_file = etree.parse(f'{os.path.dirname(__file__)}/test_xml/expected.xml')
        expected = etree.tostring(xml_file).decode('utf-8').replace('\n', '').replace('    ', '')
        actual = etree.tostring(self.interface.build_configuration_xml('test', 'hello world')).decode('utf-8')
        print(expected)
        print(actual)
        self.assertEqual(expected, actual)



