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

class InlineResponse20015(object):
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
        'message': 'object',
        'order_id': 'object',
        'order_total': 'object',
        'expiry_date': 'object'
    }

    attribute_map = {
        'message': 'message',
        'order_id': 'order_id',
        'order_total': 'order_total',
        'expiry_date': 'expiry_date'
    }

    def __init__(self, message=None, order_id=None, order_total=None, expiry_date=None):  # noqa: E501
        """InlineResponse20015 - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._order_id = None
        self._order_total = None
        self._expiry_date = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if order_id is not None:
            self.order_id = order_id
        if order_total is not None:
            self.order_total = order_total
        if expiry_date is not None:
            self.expiry_date = expiry_date

    @property
    def message(self):
        """Gets the message of this InlineResponse20015.  # noqa: E501

        Domain registration order successfully created.  # noqa: E501

        :return: The message of this InlineResponse20015.  # noqa: E501
        :rtype: object
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse20015.

        Domain registration order successfully created.  # noqa: E501

        :param message: The message of this InlineResponse20015.  # noqa: E501
        :type: object
        """

        self._message = message

    @property
    def order_id(self):
        """Gets the order_id of this InlineResponse20015.  # noqa: E501

        Always returned on success.  # noqa: E501

        :return: The order_id of this InlineResponse20015.  # noqa: E501
        :rtype: object
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InlineResponse20015.

        Always returned on success.  # noqa: E501

        :param order_id: The order_id of this InlineResponse20015.  # noqa: E501
        :type: object
        """

        self._order_id = order_id

    @property
    def order_total(self):
        """Gets the order_total of this InlineResponse20015.  # noqa: E501

        Always returned on success.  # noqa: E501

        :return: The order_total of this InlineResponse20015.  # noqa: E501
        :rtype: object
        """
        return self._order_total

    @order_total.setter
    def order_total(self, order_total):
        """Sets the order_total of this InlineResponse20015.

        Always returned on success.  # noqa: E501

        :param order_total: The order_total of this InlineResponse20015.  # noqa: E501
        :type: object
        """

        self._order_total = order_total

    @property
    def expiry_date(self):
        """Gets the expiry_date of this InlineResponse20015.  # noqa: E501

        Date format: `YYYY-MM-DD`. Not always present, as it depends on the TLD.  # noqa: E501

        :return: The expiry_date of this InlineResponse20015.  # noqa: E501
        :rtype: object
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this InlineResponse20015.

        Date format: `YYYY-MM-DD`. Not always present, as it depends on the TLD.  # noqa: E501

        :param expiry_date: The expiry_date of this InlineResponse20015.  # noqa: E501
        :type: object
        """

        self._expiry_date = expiry_date

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
        if issubclass(InlineResponse20015, dict):
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
        if not isinstance(other, InlineResponse20015):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
