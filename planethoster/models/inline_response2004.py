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

class InlineResponse2004(object):
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
        'is_transfer': 'object',
        'is_registration': 'object',
        'registration_date': 'object',
        'expiry_date': 'object',
        'registration_status': 'object',
        'registration_status_info': 'object',
        'purchase_status': 'object',
        'id_protection': 'object',
        'domain_statuses': 'object',
        'transfer_request_status': 'object',
        'transfer_request_denied_reason': 'object',
        'transfer_request_denied_at': 'object',
        'transfer_request_confirmed_at': 'object'
    }

    attribute_map = {
        'message': 'message',
        'order_id': 'order_id',
        'is_transfer': 'is_transfer',
        'is_registration': 'is_registration',
        'registration_date': 'registration_date',
        'expiry_date': 'expiry_date',
        'registration_status': 'registration_status',
        'registration_status_info': 'registration_status_info',
        'purchase_status': 'purchase_status',
        'id_protection': 'id_protection',
        'domain_statuses': 'domain_statuses',
        'transfer_request_status': 'transfer_request_status',
        'transfer_request_denied_reason': 'transfer_request_denied_reason',
        'transfer_request_denied_at': 'transfer_request_denied_at',
        'transfer_request_confirmed_at': 'transfer_request_confirmed_at'
    }

    def __init__(self, message=None, order_id=None, is_transfer=None, is_registration=None, registration_date=None, expiry_date=None, registration_status=None, registration_status_info=None, purchase_status=None, id_protection=None, domain_statuses=None, transfer_request_status=None, transfer_request_denied_reason=None, transfer_request_denied_at=None, transfer_request_confirmed_at=None):  # noqa: E501
        """InlineResponse2004 - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._order_id = None
        self._is_transfer = None
        self._is_registration = None
        self._registration_date = None
        self._expiry_date = None
        self._registration_status = None
        self._registration_status_info = None
        self._purchase_status = None
        self._id_protection = None
        self._domain_statuses = None
        self._transfer_request_status = None
        self._transfer_request_denied_reason = None
        self._transfer_request_denied_at = None
        self._transfer_request_confirmed_at = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if order_id is not None:
            self.order_id = order_id
        if is_transfer is not None:
            self.is_transfer = is_transfer
        if is_registration is not None:
            self.is_registration = is_registration
        if registration_date is not None:
            self.registration_date = registration_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if registration_status is not None:
            self.registration_status = registration_status
        if registration_status_info is not None:
            self.registration_status_info = registration_status_info
        if purchase_status is not None:
            self.purchase_status = purchase_status
        if id_protection is not None:
            self.id_protection = id_protection
        if domain_statuses is not None:
            self.domain_statuses = domain_statuses
        if transfer_request_status is not None:
            self.transfer_request_status = transfer_request_status
        if transfer_request_denied_reason is not None:
            self.transfer_request_denied_reason = transfer_request_denied_reason
        if transfer_request_denied_at is not None:
            self.transfer_request_denied_at = transfer_request_denied_at
        if transfer_request_confirmed_at is not None:
            self.transfer_request_confirmed_at = transfer_request_confirmed_at

    @property
    def message(self):
        """Gets the message of this InlineResponse2004.  # noqa: E501

        Response message.  # noqa: E501

        :return: The message of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse2004.

        Response message.  # noqa: E501

        :param message: The message of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._message = message

    @property
    def order_id(self):
        """Gets the order_id of this InlineResponse2004.  # noqa: E501

        Domain order ID.  # noqa: E501

        :return: The order_id of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InlineResponse2004.

        Domain order ID.  # noqa: E501

        :param order_id: The order_id of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._order_id = order_id

    @property
    def is_transfer(self):
        """Gets the is_transfer of this InlineResponse2004.  # noqa: E501

        Is the domain a transfer?  # noqa: E501

        :return: The is_transfer of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._is_transfer

    @is_transfer.setter
    def is_transfer(self, is_transfer):
        """Sets the is_transfer of this InlineResponse2004.

        Is the domain a transfer?  # noqa: E501

        :param is_transfer: The is_transfer of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._is_transfer = is_transfer

    @property
    def is_registration(self):
        """Gets the is_registration of this InlineResponse2004.  # noqa: E501

        Is the domain a registration?  # noqa: E501

        :return: The is_registration of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._is_registration

    @is_registration.setter
    def is_registration(self, is_registration):
        """Sets the is_registration of this InlineResponse2004.

        Is the domain a registration?  # noqa: E501

        :param is_registration: The is_registration of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._is_registration = is_registration

    @property
    def registration_date(self):
        """Gets the registration_date of this InlineResponse2004.  # noqa: E501

        Date format: `YYYY-MM-DD`.  # noqa: E501

        :return: The registration_date of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        """Sets the registration_date of this InlineResponse2004.

        Date format: `YYYY-MM-DD`.  # noqa: E501

        :param registration_date: The registration_date of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._registration_date = registration_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this InlineResponse2004.  # noqa: E501

        Date format: `YYYY-MM-DD`. Not present for incomplete domain transfers.  # noqa: E501

        :return: The expiry_date of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this InlineResponse2004.

        Date format: `YYYY-MM-DD`. Not present for incomplete domain transfers.  # noqa: E501

        :param expiry_date: The expiry_date of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._expiry_date = expiry_date

    @property
    def registration_status(self):
        """Gets the registration_status of this InlineResponse2004.  # noqa: E501

        Registration status.  # noqa: E501

        :return: The registration_status of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._registration_status

    @registration_status.setter
    def registration_status(self, registration_status):
        """Sets the registration_status of this InlineResponse2004.

        Registration status.  # noqa: E501

        :param registration_status: The registration_status of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._registration_status = registration_status

    @property
    def registration_status_info(self):
        """Gets the registration_status_info of this InlineResponse2004.  # noqa: E501

        Additional information on why the registration status is the way it is.  # noqa: E501

        :return: The registration_status_info of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._registration_status_info

    @registration_status_info.setter
    def registration_status_info(self, registration_status_info):
        """Sets the registration_status_info of this InlineResponse2004.

        Additional information on why the registration status is the way it is.  # noqa: E501

        :param registration_status_info: The registration_status_info of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._registration_status_info = registration_status_info

    @property
    def purchase_status(self):
        """Gets the purchase_status of this InlineResponse2004.  # noqa: E501

        Registration order status.  # noqa: E501

        :return: The purchase_status of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._purchase_status

    @purchase_status.setter
    def purchase_status(self, purchase_status):
        """Sets the purchase_status of this InlineResponse2004.

        Registration order status.  # noqa: E501

        :param purchase_status: The purchase_status of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._purchase_status = purchase_status

    @property
    def id_protection(self):
        """Gets the id_protection of this InlineResponse2004.  # noqa: E501

        Whether or not WHOIS ID protection is enabled for the domain.  # noqa: E501

        :return: The id_protection of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._id_protection

    @id_protection.setter
    def id_protection(self, id_protection):
        """Sets the id_protection of this InlineResponse2004.

        Whether or not WHOIS ID protection is enabled for the domain.  # noqa: E501

        :param id_protection: The id_protection of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._id_protection = id_protection

    @property
    def domain_statuses(self):
        """Gets the domain_statuses of this InlineResponse2004.  # noqa: E501

        Domain status at the registry. Not always present.  # noqa: E501

        :return: The domain_statuses of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._domain_statuses

    @domain_statuses.setter
    def domain_statuses(self, domain_statuses):
        """Sets the domain_statuses of this InlineResponse2004.

        Domain status at the registry. Not always present.  # noqa: E501

        :param domain_statuses: The domain_statuses of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._domain_statuses = domain_statuses

    @property
    def transfer_request_status(self):
        """Gets the transfer_request_status of this InlineResponse2004.  # noqa: E501

        Only present for ICANN TLDs domain transfers.  # noqa: E501

        :return: The transfer_request_status of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._transfer_request_status

    @transfer_request_status.setter
    def transfer_request_status(self, transfer_request_status):
        """Sets the transfer_request_status of this InlineResponse2004.

        Only present for ICANN TLDs domain transfers.  # noqa: E501

        :param transfer_request_status: The transfer_request_status of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._transfer_request_status = transfer_request_status

    @property
    def transfer_request_denied_reason(self):
        """Gets the transfer_request_denied_reason of this InlineResponse2004.  # noqa: E501

        Only present for ICANN TLDs domain transfers and if the transfer was denied.  # noqa: E501

        :return: The transfer_request_denied_reason of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._transfer_request_denied_reason

    @transfer_request_denied_reason.setter
    def transfer_request_denied_reason(self, transfer_request_denied_reason):
        """Sets the transfer_request_denied_reason of this InlineResponse2004.

        Only present for ICANN TLDs domain transfers and if the transfer was denied.  # noqa: E501

        :param transfer_request_denied_reason: The transfer_request_denied_reason of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._transfer_request_denied_reason = transfer_request_denied_reason

    @property
    def transfer_request_denied_at(self):
        """Gets the transfer_request_denied_at of this InlineResponse2004.  # noqa: E501

        Date format: `YYYY-MM-DD`. Only present for ICANN TLDs domain transfers, and if the transfer was denied.  # noqa: E501

        :return: The transfer_request_denied_at of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._transfer_request_denied_at

    @transfer_request_denied_at.setter
    def transfer_request_denied_at(self, transfer_request_denied_at):
        """Sets the transfer_request_denied_at of this InlineResponse2004.

        Date format: `YYYY-MM-DD`. Only present for ICANN TLDs domain transfers, and if the transfer was denied.  # noqa: E501

        :param transfer_request_denied_at: The transfer_request_denied_at of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._transfer_request_denied_at = transfer_request_denied_at

    @property
    def transfer_request_confirmed_at(self):
        """Gets the transfer_request_confirmed_at of this InlineResponse2004.  # noqa: E501

        Date format: `YYYY-MM-DD`. Only present for ICANN TLDs domain transfers, and if the transfer was confirmed by an email from the registrant.  # noqa: E501

        :return: The transfer_request_confirmed_at of this InlineResponse2004.  # noqa: E501
        :rtype: object
        """
        return self._transfer_request_confirmed_at

    @transfer_request_confirmed_at.setter
    def transfer_request_confirmed_at(self, transfer_request_confirmed_at):
        """Sets the transfer_request_confirmed_at of this InlineResponse2004.

        Date format: `YYYY-MM-DD`. Only present for ICANN TLDs domain transfers, and if the transfer was confirmed by an email from the registrant.  # noqa: E501

        :param transfer_request_confirmed_at: The transfer_request_confirmed_at of this InlineResponse2004.  # noqa: E501
        :type: object
        """

        self._transfer_request_confirmed_at = transfer_request_confirmed_at

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
        if issubclass(InlineResponse2004, dict):
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
        if not isinstance(other, InlineResponse2004):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
