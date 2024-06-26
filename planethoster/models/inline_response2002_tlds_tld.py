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

class InlineResponse2002TldsTld(object):
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
        'register': 'object',
        'transfer': 'object',
        'renew': 'object',
        'transfer_requires_epp_code': 'object',
        'id_protection_supported': 'object'
    }

    attribute_map = {
        'register': 'register',
        'transfer': 'transfer',
        'renew': 'renew',
        'transfer_requires_epp_code': 'transfer_requires_epp_code',
        'id_protection_supported': 'id_protection_supported'
    }

    def __init__(self, register=None, transfer=None, renew=None, transfer_requires_epp_code=None, id_protection_supported=None):  # noqa: E501
        """InlineResponse2002TldsTld - a model defined in Swagger"""  # noqa: E501
        self._register = None
        self._transfer = None
        self._renew = None
        self._transfer_requires_epp_code = None
        self._id_protection_supported = None
        self.discriminator = None
        if register is not None:
            self.register = register
        if transfer is not None:
            self.transfer = transfer
        if renew is not None:
            self.renew = renew
        if transfer_requires_epp_code is not None:
            self.transfer_requires_epp_code = transfer_requires_epp_code
        if id_protection_supported is not None:
            self.id_protection_supported = id_protection_supported

    @property
    def register(self):
        """Gets the register of this InlineResponse2002TldsTld.  # noqa: E501

        Price in USD to register for one year.  # noqa: E501

        :return: The register of this InlineResponse2002TldsTld.  # noqa: E501
        :rtype: object
        """
        return self._register

    @register.setter
    def register(self, register):
        """Sets the register of this InlineResponse2002TldsTld.

        Price in USD to register for one year.  # noqa: E501

        :param register: The register of this InlineResponse2002TldsTld.  # noqa: E501
        :type: object
        """

        self._register = register

    @property
    def transfer(self):
        """Gets the transfer of this InlineResponse2002TldsTld.  # noqa: E501

        Price in USD to transfer.  # noqa: E501

        :return: The transfer of this InlineResponse2002TldsTld.  # noqa: E501
        :rtype: object
        """
        return self._transfer

    @transfer.setter
    def transfer(self, transfer):
        """Sets the transfer of this InlineResponse2002TldsTld.

        Price in USD to transfer.  # noqa: E501

        :param transfer: The transfer of this InlineResponse2002TldsTld.  # noqa: E501
        :type: object
        """

        self._transfer = transfer

    @property
    def renew(self):
        """Gets the renew of this InlineResponse2002TldsTld.  # noqa: E501

        Price in USD for a one year renewal.  # noqa: E501

        :return: The renew of this InlineResponse2002TldsTld.  # noqa: E501
        :rtype: object
        """
        return self._renew

    @renew.setter
    def renew(self, renew):
        """Sets the renew of this InlineResponse2002TldsTld.

        Price in USD for a one year renewal.  # noqa: E501

        :param renew: The renew of this InlineResponse2002TldsTld.  # noqa: E501
        :type: object
        """

        self._renew = renew

    @property
    def transfer_requires_epp_code(self):
        """Gets the transfer_requires_epp_code of this InlineResponse2002TldsTld.  # noqa: E501

        Is the domaine EPP required for the transfer?  # noqa: E501

        :return: The transfer_requires_epp_code of this InlineResponse2002TldsTld.  # noqa: E501
        :rtype: object
        """
        return self._transfer_requires_epp_code

    @transfer_requires_epp_code.setter
    def transfer_requires_epp_code(self, transfer_requires_epp_code):
        """Sets the transfer_requires_epp_code of this InlineResponse2002TldsTld.

        Is the domaine EPP required for the transfer?  # noqa: E501

        :param transfer_requires_epp_code: The transfer_requires_epp_code of this InlineResponse2002TldsTld.  # noqa: E501
        :type: object
        """

        self._transfer_requires_epp_code = transfer_requires_epp_code

    @property
    def id_protection_supported(self):
        """Gets the id_protection_supported of this InlineResponse2002TldsTld.  # noqa: E501

        Is ID protection supported?  # noqa: E501

        :return: The id_protection_supported of this InlineResponse2002TldsTld.  # noqa: E501
        :rtype: object
        """
        return self._id_protection_supported

    @id_protection_supported.setter
    def id_protection_supported(self, id_protection_supported):
        """Sets the id_protection_supported of this InlineResponse2002TldsTld.

        Is ID protection supported?  # noqa: E501

        :param id_protection_supported: The id_protection_supported of this InlineResponse2002TldsTld.  # noqa: E501
        :type: object
        """

        self._id_protection_supported = id_protection_supported

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
        if issubclass(InlineResponse2002TldsTld, dict):
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
        if not isinstance(other, InlineResponse2002TldsTld):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
