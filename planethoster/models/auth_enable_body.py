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

class AuthEnableBody(object):
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
        'domain': 'object',
        'mail_user': 'object',
        'auth': 'object',
        'id': 'object'
    }

    attribute_map = {
        'domain': 'domain',
        'mail_user': 'mailUser',
        'auth': 'auth',
        'id': 'id'
    }

    def __init__(self, domain=None, mail_user=None, auth=None, id=None):  # noqa: E501
        """AuthEnableBody - a model defined in Swagger"""  # noqa: E501
        self._domain = None
        self._mail_user = None
        self._auth = None
        self._id = None
        self.discriminator = None
        self.domain = domain
        self.mail_user = mail_user
        self.auth = auth
        self.id = id

    @property
    def domain(self):
        """Gets the domain of this AuthEnableBody.  # noqa: E501

        Domain name.  # noqa: E501

        :return: The domain of this AuthEnableBody.  # noqa: E501
        :rtype: object
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AuthEnableBody.

        Domain name.  # noqa: E501

        :param domain: The domain of this AuthEnableBody.  # noqa: E501
        :type: object
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def mail_user(self):
        """Gets the mail_user of this AuthEnableBody.  # noqa: E501

        Email user.  # noqa: E501

        :return: The mail_user of this AuthEnableBody.  # noqa: E501
        :rtype: object
        """
        return self._mail_user

    @mail_user.setter
    def mail_user(self, mail_user):
        """Sets the mail_user of this AuthEnableBody.

        Email user.  # noqa: E501

        :param mail_user: The mail_user of this AuthEnableBody.  # noqa: E501
        :type: object
        """
        if mail_user is None:
            raise ValueError("Invalid value for `mail_user`, must not be `None`")  # noqa: E501

        self._mail_user = mail_user

    @property
    def auth(self):
        """Gets the auth of this AuthEnableBody.  # noqa: E501

        Email authentication.  # noqa: E501

        :return: The auth of this AuthEnableBody.  # noqa: E501
        :rtype: object
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this AuthEnableBody.

        Email authentication.  # noqa: E501

        :param auth: The auth of this AuthEnableBody.  # noqa: E501
        :type: object
        """
        if auth is None:
            raise ValueError("Invalid value for `auth`, must not be `None`")  # noqa: E501

        self._auth = auth

    @property
    def id(self):
        """Gets the id of this AuthEnableBody.  # noqa: E501

        World account ID. Can be found with [/get-accounts](#operation/getAccounts).  # noqa: E501

        :return: The id of this AuthEnableBody.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthEnableBody.

        World account ID. Can be found with [/get-accounts](#operation/getAccounts).  # noqa: E501

        :param id: The id of this AuthEnableBody.  # noqa: E501
        :type: object
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if issubclass(AuthEnableBody, dict):
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
        if not isinstance(other, AuthEnableBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
