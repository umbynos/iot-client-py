# coding: utf-8

"""
    Iot API

    Collection of all public API endpoints.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ArduinoSeriesBatch(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'resp_version': 'int',
        'responses': 'list[ArduinoSeriesResponse]'
    }

    attribute_map = {
        'resp_version': 'resp_version',
        'responses': 'responses'
    }

    def __init__(self, resp_version=None, responses=None):  # noqa: E501
        """ArduinoSeriesBatch - a model defined in OpenAPI"""  # noqa: E501

        self._resp_version = None
        self._responses = None
        self.discriminator = None

        self.resp_version = resp_version
        self.responses = responses

    @property
    def resp_version(self):
        """Gets the resp_version of this ArduinoSeriesBatch.  # noqa: E501

        Response version  # noqa: E501

        :return: The resp_version of this ArduinoSeriesBatch.  # noqa: E501
        :rtype: int
        """
        return self._resp_version

    @resp_version.setter
    def resp_version(self, resp_version):
        """Sets the resp_version of this ArduinoSeriesBatch.

        Response version  # noqa: E501

        :param resp_version: The resp_version of this ArduinoSeriesBatch.  # noqa: E501
        :type: int
        """
        if resp_version is None:
            raise ValueError("Invalid value for `resp_version`, must not be `None`")  # noqa: E501

        self._resp_version = resp_version

    @property
    def responses(self):
        """Gets the responses of this ArduinoSeriesBatch.  # noqa: E501

        Responses of the request  # noqa: E501

        :return: The responses of this ArduinoSeriesBatch.  # noqa: E501
        :rtype: list[ArduinoSeriesResponse]
        """
        return self._responses

    @responses.setter
    def responses(self, responses):
        """Sets the responses of this ArduinoSeriesBatch.

        Responses of the request  # noqa: E501

        :param responses: The responses of this ArduinoSeriesBatch.  # noqa: E501
        :type: list[ArduinoSeriesResponse]
        """
        if responses is None:
            raise ValueError("Invalid value for `responses`, must not be `None`")  # noqa: E501

        self._responses = responses

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ArduinoSeriesBatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
