# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems


class V1EndpointPort(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Swagger model

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'port': 'int',
            'protocol': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'port': 'port',
            'protocol': 'protocol'
        }

        self._name = None
        self._port = None
        self._protocol = None

    @property
    def name(self):
        """
        Gets the name of this V1EndpointPort.
        The name of this port (corresponds to ServicePort.Name). Must be a DNS_LABEL. Optional only if one port is defined.

        :return: The name of this V1EndpointPort.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1EndpointPort.
        The name of this port (corresponds to ServicePort.Name). Must be a DNS_LABEL. Optional only if one port is defined.

        :param name: The name of this V1EndpointPort.
        :type: str
        """
        self._name = name

    @property
    def port(self):
        """
        Gets the port of this V1EndpointPort.
        The port number of the endpoint.

        :return: The port of this V1EndpointPort.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this V1EndpointPort.
        The port number of the endpoint.

        :param port: The port of this V1EndpointPort.
        :type: int
        """
        self._port = port

    @property
    def protocol(self):
        """
        Gets the protocol of this V1EndpointPort.
        The IP protocol for this port. Must be UDP or TCP. Default is TCP.

        :return: The protocol of this V1EndpointPort.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this V1EndpointPort.
        The IP protocol for this port. Must be UDP or TCP. Default is TCP.

        :param protocol: The protocol of this V1EndpointPort.
        :type: str
        """
        self._protocol = protocol

    def to_dict(self):
        """
        Return model properties dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Return model properties str
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
