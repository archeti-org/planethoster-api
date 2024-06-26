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

class EmailAddBody(object):
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
        'password': 'object',
        'mail_user': 'object',
        'quota': 'object',
        'id': 'object'
    }

    attribute_map = {
        'domain': 'domain',
        'password': 'password',
        'mail_user': 'mailUser',
        'quota': 'quota',
        'id': 'id'
    }

    def __init__(self, domain=None, password=None, mail_user=None, quota=None, id=None):  # noqa: E501
        """EmailAddBody - a model defined in Swagger"""  # noqa: E501
        self._domain = None
        self._password = None
        self._mail_user = None
        self._quota = None
        self._id = None
        self.discriminator = None
        self.domain = domain
        self.password = password
        self.mail_user = mail_user
        if quota is not None:
            self.quota = quota
        self.id = id

    @property
    def domain(self):
        """Gets the domain of this EmailAddBody.  # noqa: E501

        Domain name.  # noqa: E501

        :return: The domain of this EmailAddBody.  # noqa: E501
        :rtype: object
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this EmailAddBody.

        Domain name.  # noqa: E501

        :param domain: The domain of this EmailAddBody.  # noqa: E501
        :type: object
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def password(self):
        """Gets the password of this EmailAddBody.  # noqa: E501

        Email account password.  # noqa: E501

        :return: The password of this EmailAddBody.  # noqa: E501
        :rtype: object
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this EmailAddBody.

        Email account password.  # noqa: E501

        :param password: The password of this EmailAddBody.  # noqa: E501
        :type: object
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def mail_user(self):
        """Gets the mail_user of this EmailAddBody.  # noqa: E501

        Email user.  # noqa: E501

        :return: The mail_user of this EmailAddBody.  # noqa: E501
        :rtype: object
        """
        return self._mail_user

    @mail_user.setter
    def mail_user(self, mail_user):
        """Sets the mail_user of this EmailAddBody.

        Email user.  # noqa: E501

        :param mail_user: The mail_user of this EmailAddBody.  # noqa: E501
        :type: object
        """
        if mail_user is None:
            raise ValueError("Invalid value for `mail_user`, must not be `None`")  # noqa: E501

        self._mail_user = mail_user

    @property
    def quota(self):
        """Gets the quota of this EmailAddBody.  # noqa: E501

        Size of the email quota in MB.  # noqa: E501

        :return: The quota of this EmailAddBody.  # noqa: E501
        :rtype: object
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this EmailAddBody.

        Size of the email quota in MB.  # noqa: E501

        :param quota: The quota of this EmailAddBody.  # noqa: E501
        :type: object
        """

        self._quota = quota

    @property
    def id(self):
        """Gets the id of this EmailAddBody.  # noqa: E501

        World account ID. Can be found with [/get-accounts](#operation/getAccounts).  # noqa: E501

        :return: The id of this EmailAddBody.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmailAddBody.

        World account ID. Can be found with [/get-accounts](#operation/getAccounts).  # noqa: E501

        :param id: The id of this EmailAddBody.  # noqa: E501
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
        if issubclass(EmailAddBody, dict):
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
        if not isinstance(other, EmailAddBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
