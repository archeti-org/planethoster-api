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

class WordpressAddBody(object):
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
        'admin_user': 'object',
        'admin_password': 'object',
        'admin_email': 'object',
        'domain': 'object',
        'path': 'object',
        'title': 'object',
        'locale': 'object',
        'id': 'object'
    }

    attribute_map = {
        'admin_user': 'adminUser',
        'admin_password': 'adminPassword',
        'admin_email': 'adminEmail',
        'domain': 'domain',
        'path': 'path',
        'title': 'title',
        'locale': 'locale',
        'id': 'id'
    }

    def __init__(self, admin_user=None, admin_password=None, admin_email=None, domain=None, path=None, title=None, locale=None, id=None):  # noqa: E501
        """WordpressAddBody - a model defined in Swagger"""  # noqa: E501
        self._admin_user = None
        self._admin_password = None
        self._admin_email = None
        self._domain = None
        self._path = None
        self._title = None
        self._locale = None
        self._id = None
        self.discriminator = None
        self.admin_user = admin_user
        self.admin_password = admin_password
        self.admin_email = admin_email
        self.domain = domain
        self.path = path
        self.title = title
        if locale is not None:
            self.locale = locale
        self.id = id

    @property
    def admin_user(self):
        """Gets the admin_user of this WordpressAddBody.  # noqa: E501

        The administrator user  # noqa: E501

        :return: The admin_user of this WordpressAddBody.  # noqa: E501
        :rtype: object
        """
        return self._admin_user

    @admin_user.setter
    def admin_user(self, admin_user):
        """Sets the admin_user of this WordpressAddBody.

        The administrator user  # noqa: E501

        :param admin_user: The admin_user of this WordpressAddBody.  # noqa: E501
        :type: object
        """
        if admin_user is None:
            raise ValueError("Invalid value for `admin_user`, must not be `None`")  # noqa: E501

        self._admin_user = admin_user

    @property
    def admin_password(self):
        """Gets the admin_password of this WordpressAddBody.  # noqa: E501

        Administrator password  # noqa: E501

        :return: The admin_password of this WordpressAddBody.  # noqa: E501
        :rtype: object
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """Sets the admin_password of this WordpressAddBody.

        Administrator password  # noqa: E501

        :param admin_password: The admin_password of this WordpressAddBody.  # noqa: E501
        :type: object
        """
        if admin_password is None:
            raise ValueError("Invalid value for `admin_password`, must not be `None`")  # noqa: E501

        self._admin_password = admin_password

    @property
    def admin_email(self):
        """Gets the admin_email of this WordpressAddBody.  # noqa: E501

        Administrator e-mail  # noqa: E501

        :return: The admin_email of this WordpressAddBody.  # noqa: E501
        :rtype: object
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """Sets the admin_email of this WordpressAddBody.

        Administrator e-mail  # noqa: E501

        :param admin_email: The admin_email of this WordpressAddBody.  # noqa: E501
        :type: object
        """
        if admin_email is None:
            raise ValueError("Invalid value for `admin_email`, must not be `None`")  # noqa: E501

        self._admin_email = admin_email

    @property
    def domain(self):
        """Gets the domain of this WordpressAddBody.  # noqa: E501

        The associated domain name  # noqa: E501

        :return: The domain of this WordpressAddBody.  # noqa: E501
        :rtype: object
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this WordpressAddBody.

        The associated domain name  # noqa: E501

        :param domain: The domain of this WordpressAddBody.  # noqa: E501
        :type: object
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def path(self):
        """Gets the path of this WordpressAddBody.  # noqa: E501

        The installation path  # noqa: E501

        :return: The path of this WordpressAddBody.  # noqa: E501
        :rtype: object
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this WordpressAddBody.

        The installation path  # noqa: E501

        :param path: The path of this WordpressAddBody.  # noqa: E501
        :type: object
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def title(self):
        """Gets the title of this WordpressAddBody.  # noqa: E501

        The wordpress title  # noqa: E501

        :return: The title of this WordpressAddBody.  # noqa: E501
        :rtype: object
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this WordpressAddBody.

        The wordpress title  # noqa: E501

        :param title: The title of this WordpressAddBody.  # noqa: E501
        :type: object
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def locale(self):
        """Gets the locale of this WordpressAddBody.  # noqa: E501

        Wordpress locales  # noqa: E501

        :return: The locale of this WordpressAddBody.  # noqa: E501
        :rtype: object
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this WordpressAddBody.

        Wordpress locales  # noqa: E501

        :param locale: The locale of this WordpressAddBody.  # noqa: E501
        :type: object
        """

        self._locale = locale

    @property
    def id(self):
        """Gets the id of this WordpressAddBody.  # noqa: E501

        World account ID. Can be found with [/get-accounts](#operation/getAccounts).  # noqa: E501

        :return: The id of this WordpressAddBody.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WordpressAddBody.

        World account ID. Can be found with [/get-accounts](#operation/getAccounts).  # noqa: E501

        :param id: The id of this WordpressAddBody.  # noqa: E501
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
        if issubclass(WordpressAddBody, dict):
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
        if not isinstance(other, WordpressAddBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
