# coding: utf-8

"""
    Grafeas API

    An API to insert and retrieve annotations on cloud artifacts.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

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
import re


class Basis(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, resource_url=None, fingerprint=None):
        """
        Basis - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'resource_url': 'str',
            'fingerprint': 'Fingerprint'
        }

        self.attribute_map = {
            'resource_url': 'resourceUrl',
            'fingerprint': 'fingerprint'
        }

        self._resource_url = resource_url
        self._fingerprint = fingerprint

    @property
    def resource_url(self):
        """
        Gets the resource_url of this Basis.
        The resource_url for the resource representing the basis of associated occurrence images.

        :return: The resource_url of this Basis.
        :rtype: str
        """
        return self._resource_url

    @resource_url.setter
    def resource_url(self, resource_url):
        """
        Sets the resource_url of this Basis.
        The resource_url for the resource representing the basis of associated occurrence images.

        :param resource_url: The resource_url of this Basis.
        :type: str
        """

        self._resource_url = resource_url

    @property
    def fingerprint(self):
        """
        Gets the fingerprint of this Basis.
        The fingerprint of the base image

        :return: The fingerprint of this Basis.
        :rtype: Fingerprint
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """
        Sets the fingerprint of this Basis.
        The fingerprint of the base image

        :param fingerprint: The fingerprint of this Basis.
        :type: Fingerprint
        """

        self._fingerprint = fingerprint

    def to_dict(self):
        """
        Returns the model properties as a dict
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
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other