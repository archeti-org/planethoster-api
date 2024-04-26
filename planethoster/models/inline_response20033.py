# coding: utf-8

"""
    PlanetHoster API

    | <a href=\"https://apidoc.planethoster.com/fr\">Version Française</a> ## Description The PlanetHoster API allows actions related to domain management and web hosting. ## Details - SSL only: we require that all requests be done over encrypted TLS/SSL connections. - Supported HTTP verbs are GET and POST. If your client does not support all HTTP verbs, you can override the verb with X-Http-Method-Override HTTP header. - Unless otherwise specified in the method documentation, all successful API calls return an **HTTP code 200** with a JSON object. - Errors are returned with an HTTP code 4XX or 5XX, a JSON object with properties \"error\" (an error message) and an \"error_code\" (optional, an integer). - Every string passed to and from the API needs to be UTF-8 encoded. - The API sends ETag headers and supports the If-None-Match header. - Unless otherwise specified, all API methods require authentication with api_user and api_key.  ## Authentication and whitelist 1. In order to be able to contact the API, you must whitelist your IPs. 2. API user and API key are required in the HTTP header.  Whitelisted IP and credentials can be found in the <a href=\"https://my.planethoster.com/domain-reseller\" target=\"_blank\">PlanetHoster Client Area / Reseller section</a>.  <SecurityDefinitions />   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: tech@support.planethoster.info
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20033(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data': 'InlineResponse20033Data',
        'success': 'object',
        'errors': 'object'
    }

    attribute_map = {
        'data': 'data',
        'success': 'success',
        'errors': 'errors'
    }

    def __init__(self, data=None, success=None, errors=None):  # noqa: E501
        """InlineResponse20033 - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._success = None
        self._errors = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if success is not None:
            self.success = success
        if errors is not None:
            self.errors = errors

    @property
    def data(self):
        """Gets the data of this InlineResponse20033.  # noqa: E501


        :return: The data of this InlineResponse20033.  # noqa: E501
        :rtype: InlineResponse20033Data
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse20033.


        :param data: The data of this InlineResponse20033.  # noqa: E501
        :type: InlineResponse20033Data
        """

        self._data = data

    @property
    def success(self):
        """Gets the success of this InlineResponse20033.  # noqa: E501

        Successful response or not.  # noqa: E501

        :return: The success of this InlineResponse20033.  # noqa: E501
        :rtype: object
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InlineResponse20033.

        Successful response or not.  # noqa: E501

        :param success: The success of this InlineResponse20033.  # noqa: E501
        :type: object
        """

        self._success = success

    @property
    def errors(self):
        """Gets the errors of this InlineResponse20033.  # noqa: E501

        Array of encountered errors.  # noqa: E501

        :return: The errors of this InlineResponse20033.  # noqa: E501
        :rtype: object
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this InlineResponse20033.

        Array of encountered errors.  # noqa: E501

        :param errors: The errors of this InlineResponse20033.  # noqa: E501
        :type: object
        """

        self._errors = errors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse20033, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20033):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
