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

class ResellerapiRegisterdomainBody(object):
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
        'sld': 'object',
        'tld': 'object',
        'period': 'object',
        'ns1': 'object',
        'ns2': 'object',
        'ns3': 'object',
        'ns4': 'object',
        'ns5': 'object',
        'id_protection': 'object',
        'register_if_premium': 'object',
        'use_planethoster_nameservers': 'object',
        'addtl_field': 'object',
        'registrant_first_name': 'object',
        'registrant_last_name': 'object',
        'registrant_email': 'object',
        'registrant_company_name': 'object',
        'registrant_address1': 'object',
        'registrant_address2': 'object',
        'registrant_city': 'object',
        'registrant_postal_code': 'object',
        'registrant_state': 'object',
        'registrant_country_code': 'object',
        'registrant_phone': 'object'
    }

    attribute_map = {
        'sld': 'sld',
        'tld': 'tld',
        'period': 'period',
        'ns1': 'ns1',
        'ns2': 'ns2',
        'ns3': 'ns3',
        'ns4': 'ns4',
        'ns5': 'ns5',
        'id_protection': 'id_protection',
        'register_if_premium': 'register_if_premium',
        'use_planethoster_nameservers': 'use_planethoster_nameservers',
        'addtl_field': 'addtl_field',
        'registrant_first_name': 'registrant_first_name',
        'registrant_last_name': 'registrant_last_name',
        'registrant_email': 'registrant_email',
        'registrant_company_name': 'registrant_company_name',
        'registrant_address1': 'registrant_address1',
        'registrant_address2': 'registrant_address2',
        'registrant_city': 'registrant_city',
        'registrant_postal_code': 'registrant_postal_code',
        'registrant_state': 'registrant_state',
        'registrant_country_code': 'registrant_country_code',
        'registrant_phone': 'registrant_phone'
    }

    def __init__(self, sld=None, tld=None, period=None, ns1=None, ns2=None, ns3=None, ns4=None, ns5=None, id_protection=None, register_if_premium=None, use_planethoster_nameservers=None, addtl_field=None, registrant_first_name=None, registrant_last_name=None, registrant_email=None, registrant_company_name=None, registrant_address1=None, registrant_address2=None, registrant_city=None, registrant_postal_code=None, registrant_state=None, registrant_country_code=None, registrant_phone=None):  # noqa: E501
        """ResellerapiRegisterdomainBody - a model defined in Swagger"""  # noqa: E501
        self._sld = None
        self._tld = None
        self._period = None
        self._ns1 = None
        self._ns2 = None
        self._ns3 = None
        self._ns4 = None
        self._ns5 = None
        self._id_protection = None
        self._register_if_premium = None
        self._use_planethoster_nameservers = None
        self._addtl_field = None
        self._registrant_first_name = None
        self._registrant_last_name = None
        self._registrant_email = None
        self._registrant_company_name = None
        self._registrant_address1 = None
        self._registrant_address2 = None
        self._registrant_city = None
        self._registrant_postal_code = None
        self._registrant_state = None
        self._registrant_country_code = None
        self._registrant_phone = None
        self.discriminator = None
        self.sld = sld
        self.tld = tld
        self.period = period
        self.ns1 = ns1
        self.ns2 = ns2
        if ns3 is not None:
            self.ns3 = ns3
        if ns4 is not None:
            self.ns4 = ns4
        if ns5 is not None:
            self.ns5 = ns5
        self.id_protection = id_protection
        self.register_if_premium = register_if_premium
        self.use_planethoster_nameservers = use_planethoster_nameservers
        if addtl_field is not None:
            self.addtl_field = addtl_field
        self.registrant_first_name = registrant_first_name
        self.registrant_last_name = registrant_last_name
        self.registrant_email = registrant_email
        if registrant_company_name is not None:
            self.registrant_company_name = registrant_company_name
        self.registrant_address1 = registrant_address1
        if registrant_address2 is not None:
            self.registrant_address2 = registrant_address2
        self.registrant_city = registrant_city
        self.registrant_postal_code = registrant_postal_code
        self.registrant_state = registrant_state
        self.registrant_country_code = registrant_country_code
        self.registrant_phone = registrant_phone

    @property
    def sld(self):
        """Gets the sld of this ResellerapiRegisterdomainBody.  # noqa: E501

        Domain name without the Top-Level Domain.  # noqa: E501

        :return: The sld of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._sld

    @sld.setter
    def sld(self, sld):
        """Sets the sld of this ResellerapiRegisterdomainBody.

        Domain name without the Top-Level Domain.  # noqa: E501

        :param sld: The sld of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if sld is None:
            raise ValueError("Invalid value for `sld`, must not be `None`")  # noqa: E501

        self._sld = sld

    @property
    def tld(self):
        """Gets the tld of this ResellerapiRegisterdomainBody.  # noqa: E501

        TLD without the leading period.  # noqa: E501

        :return: The tld of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._tld

    @tld.setter
    def tld(self, tld):
        """Sets the tld of this ResellerapiRegisterdomainBody.

        TLD without the leading period.  # noqa: E501

        :param tld: The tld of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if tld is None:
            raise ValueError("Invalid value for `tld`, must not be `None`")  # noqa: E501

        self._tld = tld

    @property
    def period(self):
        """Gets the period of this ResellerapiRegisterdomainBody.  # noqa: E501

        Number of years to register the domain name.   See [Tld prices](#operation/tldPrices)   # noqa: E501

        :return: The period of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ResellerapiRegisterdomainBody.

        Number of years to register the domain name.   See [Tld prices](#operation/tldPrices)   # noqa: E501

        :param period: The period of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if period is None:
            raise ValueError("Invalid value for `period`, must not be `None`")  # noqa: E501

        self._period = period

    @property
    def ns1(self):
        """Gets the ns1 of this ResellerapiRegisterdomainBody.  # noqa: E501

        Existing nameserver to use for DNS lookup of the registered domain.  # noqa: E501

        :return: The ns1 of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._ns1

    @ns1.setter
    def ns1(self, ns1):
        """Sets the ns1 of this ResellerapiRegisterdomainBody.

        Existing nameserver to use for DNS lookup of the registered domain.  # noqa: E501

        :param ns1: The ns1 of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if ns1 is None:
            raise ValueError("Invalid value for `ns1`, must not be `None`")  # noqa: E501

        self._ns1 = ns1

    @property
    def ns2(self):
        """Gets the ns2 of this ResellerapiRegisterdomainBody.  # noqa: E501

        Existing nameserver to use for DNS lookup of the registered domain.  # noqa: E501

        :return: The ns2 of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._ns2

    @ns2.setter
    def ns2(self, ns2):
        """Sets the ns2 of this ResellerapiRegisterdomainBody.

        Existing nameserver to use for DNS lookup of the registered domain.  # noqa: E501

        :param ns2: The ns2 of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if ns2 is None:
            raise ValueError("Invalid value for `ns2`, must not be `None`")  # noqa: E501

        self._ns2 = ns2

    @property
    def ns3(self):
        """Gets the ns3 of this ResellerapiRegisterdomainBody.  # noqa: E501

        Existing nameserver to use for DNS lookup of the registered domain.  # noqa: E501

        :return: The ns3 of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._ns3

    @ns3.setter
    def ns3(self, ns3):
        """Sets the ns3 of this ResellerapiRegisterdomainBody.

        Existing nameserver to use for DNS lookup of the registered domain.  # noqa: E501

        :param ns3: The ns3 of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """

        self._ns3 = ns3

    @property
    def ns4(self):
        """Gets the ns4 of this ResellerapiRegisterdomainBody.  # noqa: E501

        Existing nameserver to use for DNS lookup of the registered domain.  # noqa: E501

        :return: The ns4 of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._ns4

    @ns4.setter
    def ns4(self, ns4):
        """Sets the ns4 of this ResellerapiRegisterdomainBody.

        Existing nameserver to use for DNS lookup of the registered domain.  # noqa: E501

        :param ns4: The ns4 of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """

        self._ns4 = ns4

    @property
    def ns5(self):
        """Gets the ns5 of this ResellerapiRegisterdomainBody.  # noqa: E501

        Existing nameserver to use for DNS lookup of the registered domain.  # noqa: E501

        :return: The ns5 of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._ns5

    @ns5.setter
    def ns5(self, ns5):
        """Sets the ns5 of this ResellerapiRegisterdomainBody.

        Existing nameserver to use for DNS lookup of the registered domain.  # noqa: E501

        :param ns5: The ns5 of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """

        self._ns5 = ns5

    @property
    def id_protection(self):
        """Gets the id_protection of this ResellerapiRegisterdomainBody.  # noqa: E501

        Whether or not to order WHOIS ID protection for this domain name.   *Note that not all TLDs support ID protection.*   See [Tld prices](#operation/tldPrices)   # noqa: E501

        :return: The id_protection of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._id_protection

    @id_protection.setter
    def id_protection(self, id_protection):
        """Sets the id_protection of this ResellerapiRegisterdomainBody.

        Whether or not to order WHOIS ID protection for this domain name.   *Note that not all TLDs support ID protection.*   See [Tld prices](#operation/tldPrices)   # noqa: E501

        :param id_protection: The id_protection of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if id_protection is None:
            raise ValueError("Invalid value for `id_protection`, must not be `None`")  # noqa: E501

        self._id_protection = id_protection

    @property
    def register_if_premium(self):
        """Gets the register_if_premium of this ResellerapiRegisterdomainBody.  # noqa: E501

        Register the domain name even if it is a Premium domain, which could be much more expensive.  # noqa: E501

        :return: The register_if_premium of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._register_if_premium

    @register_if_premium.setter
    def register_if_premium(self, register_if_premium):
        """Sets the register_if_premium of this ResellerapiRegisterdomainBody.

        Register the domain name even if it is a Premium domain, which could be much more expensive.  # noqa: E501

        :param register_if_premium: The register_if_premium of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if register_if_premium is None:
            raise ValueError("Invalid value for `register_if_premium`, must not be `None`")  # noqa: E501

        self._register_if_premium = register_if_premium

    @property
    def use_planethoster_nameservers(self):
        """Gets the use_planethoster_nameservers of this ResellerapiRegisterdomainBody.  # noqa: E501

        Only set this to true when using 'nsa.n0c.com', 'nsb.n0c.com', and 'nsc.n0c.com' as your ns1, ns2 and ns3 values (ns4 and ns5 should be empty strings in this case). This option creates a DNS zone for the domain name on the nameservers after successful registration.   # noqa: E501

        :return: The use_planethoster_nameservers of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._use_planethoster_nameservers

    @use_planethoster_nameservers.setter
    def use_planethoster_nameservers(self, use_planethoster_nameservers):
        """Sets the use_planethoster_nameservers of this ResellerapiRegisterdomainBody.

        Only set this to true when using 'nsa.n0c.com', 'nsb.n0c.com', and 'nsc.n0c.com' as your ns1, ns2 and ns3 values (ns4 and ns5 should be empty strings in this case). This option creates a DNS zone for the domain name on the nameservers after successful registration.   # noqa: E501

        :param use_planethoster_nameservers: The use_planethoster_nameservers of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if use_planethoster_nameservers is None:
            raise ValueError("Invalid value for `use_planethoster_nameservers`, must not be `None`")  # noqa: E501

        self._use_planethoster_nameservers = use_planethoster_nameservers

    @property
    def addtl_field(self):
        """Gets the addtl_field of this ResellerapiRegisterdomainBody.  # noqa: E501

        Object that represent additional fields specific for the TLD that is being registered.   See the index of [available additional fields](#) for each TLD.  *Note that some additional fields are required!*   # noqa: E501

        :return: The addtl_field of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._addtl_field

    @addtl_field.setter
    def addtl_field(self, addtl_field):
        """Sets the addtl_field of this ResellerapiRegisterdomainBody.

        Object that represent additional fields specific for the TLD that is being registered.   See the index of [available additional fields](#) for each TLD.  *Note that some additional fields are required!*   # noqa: E501

        :param addtl_field: The addtl_field of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """

        self._addtl_field = addtl_field

    @property
    def registrant_first_name(self):
        """Gets the registrant_first_name of this ResellerapiRegisterdomainBody.  # noqa: E501

        First name of the domain name registrant contact.  # noqa: E501

        :return: The registrant_first_name of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._registrant_first_name

    @registrant_first_name.setter
    def registrant_first_name(self, registrant_first_name):
        """Sets the registrant_first_name of this ResellerapiRegisterdomainBody.

        First name of the domain name registrant contact.  # noqa: E501

        :param registrant_first_name: The registrant_first_name of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if registrant_first_name is None:
            raise ValueError("Invalid value for `registrant_first_name`, must not be `None`")  # noqa: E501

        self._registrant_first_name = registrant_first_name

    @property
    def registrant_last_name(self):
        """Gets the registrant_last_name of this ResellerapiRegisterdomainBody.  # noqa: E501

        Last name of the domain name registrant contact.  # noqa: E501

        :return: The registrant_last_name of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._registrant_last_name

    @registrant_last_name.setter
    def registrant_last_name(self, registrant_last_name):
        """Sets the registrant_last_name of this ResellerapiRegisterdomainBody.

        Last name of the domain name registrant contact.  # noqa: E501

        :param registrant_last_name: The registrant_last_name of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if registrant_last_name is None:
            raise ValueError("Invalid value for `registrant_last_name`, must not be `None`")  # noqa: E501

        self._registrant_last_name = registrant_last_name

    @property
    def registrant_email(self):
        """Gets the registrant_email of this ResellerapiRegisterdomainBody.  # noqa: E501

        Email address of the domain name registrant contact.  # noqa: E501

        :return: The registrant_email of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._registrant_email

    @registrant_email.setter
    def registrant_email(self, registrant_email):
        """Sets the registrant_email of this ResellerapiRegisterdomainBody.

        Email address of the domain name registrant contact.  # noqa: E501

        :param registrant_email: The registrant_email of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if registrant_email is None:
            raise ValueError("Invalid value for `registrant_email`, must not be `None`")  # noqa: E501

        self._registrant_email = registrant_email

    @property
    def registrant_company_name(self):
        """Gets the registrant_company_name of this ResellerapiRegisterdomainBody.  # noqa: E501

        Name of company or organization for which the registrant contact is registering the domain name. *Can be empty if it is for personal use.*   # noqa: E501

        :return: The registrant_company_name of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._registrant_company_name

    @registrant_company_name.setter
    def registrant_company_name(self, registrant_company_name):
        """Sets the registrant_company_name of this ResellerapiRegisterdomainBody.

        Name of company or organization for which the registrant contact is registering the domain name. *Can be empty if it is for personal use.*   # noqa: E501

        :param registrant_company_name: The registrant_company_name of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """

        self._registrant_company_name = registrant_company_name

    @property
    def registrant_address1(self):
        """Gets the registrant_address1 of this ResellerapiRegisterdomainBody.  # noqa: E501

        Civic number and street name of company or registrant contact's primary residence.  # noqa: E501

        :return: The registrant_address1 of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._registrant_address1

    @registrant_address1.setter
    def registrant_address1(self, registrant_address1):
        """Sets the registrant_address1 of this ResellerapiRegisterdomainBody.

        Civic number and street name of company or registrant contact's primary residence.  # noqa: E501

        :param registrant_address1: The registrant_address1 of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if registrant_address1 is None:
            raise ValueError("Invalid value for `registrant_address1`, must not be `None`")  # noqa: E501

        self._registrant_address1 = registrant_address1

    @property
    def registrant_address2(self):
        """Gets the registrant_address2 of this ResellerapiRegisterdomainBody.  # noqa: E501

        Civic number and street name of registrant contact's secondary residence.   *Can be empty.*   # noqa: E501

        :return: The registrant_address2 of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._registrant_address2

    @registrant_address2.setter
    def registrant_address2(self, registrant_address2):
        """Sets the registrant_address2 of this ResellerapiRegisterdomainBody.

        Civic number and street name of registrant contact's secondary residence.   *Can be empty.*   # noqa: E501

        :param registrant_address2: The registrant_address2 of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """

        self._registrant_address2 = registrant_address2

    @property
    def registrant_city(self):
        """Gets the registrant_city of this ResellerapiRegisterdomainBody.  # noqa: E501

        Name of the city in which registrant contact resides.  # noqa: E501

        :return: The registrant_city of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._registrant_city

    @registrant_city.setter
    def registrant_city(self, registrant_city):
        """Sets the registrant_city of this ResellerapiRegisterdomainBody.

        Name of the city in which registrant contact resides.  # noqa: E501

        :param registrant_city: The registrant_city of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if registrant_city is None:
            raise ValueError("Invalid value for `registrant_city`, must not be `None`")  # noqa: E501

        self._registrant_city = registrant_city

    @property
    def registrant_postal_code(self):
        """Gets the registrant_postal_code of this ResellerapiRegisterdomainBody.  # noqa: E501

        Postal code or ZIP code of registrant contact's residence.  # noqa: E501

        :return: The registrant_postal_code of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._registrant_postal_code

    @registrant_postal_code.setter
    def registrant_postal_code(self, registrant_postal_code):
        """Sets the registrant_postal_code of this ResellerapiRegisterdomainBody.

        Postal code or ZIP code of registrant contact's residence.  # noqa: E501

        :param registrant_postal_code: The registrant_postal_code of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if registrant_postal_code is None:
            raise ValueError("Invalid value for `registrant_postal_code`, must not be `None`")  # noqa: E501

        self._registrant_postal_code = registrant_postal_code

    @property
    def registrant_state(self):
        """Gets the registrant_state of this ResellerapiRegisterdomainBody.  # noqa: E501

        State or province of registrant contact's residence.  # noqa: E501

        :return: The registrant_state of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._registrant_state

    @registrant_state.setter
    def registrant_state(self, registrant_state):
        """Sets the registrant_state of this ResellerapiRegisterdomainBody.

        State or province of registrant contact's residence.  # noqa: E501

        :param registrant_state: The registrant_state of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if registrant_state is None:
            raise ValueError("Invalid value for `registrant_state`, must not be `None`")  # noqa: E501

        self._registrant_state = registrant_state

    @property
    def registrant_country_code(self):
        """Gets the registrant_country_code of this ResellerapiRegisterdomainBody.  # noqa: E501

        Two letters code of registrant contact's residence country.   <a href=\"https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\" target=\"_blank\">See country code list</a>   # noqa: E501

        :return: The registrant_country_code of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._registrant_country_code

    @registrant_country_code.setter
    def registrant_country_code(self, registrant_country_code):
        """Sets the registrant_country_code of this ResellerapiRegisterdomainBody.

        Two letters code of registrant contact's residence country.   <a href=\"https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\" target=\"_blank\">See country code list</a>   # noqa: E501

        :param registrant_country_code: The registrant_country_code of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if registrant_country_code is None:
            raise ValueError("Invalid value for `registrant_country_code`, must not be `None`")  # noqa: E501

        self._registrant_country_code = registrant_country_code

    @property
    def registrant_phone(self):
        """Gets the registrant_phone of this ResellerapiRegisterdomainBody.  # noqa: E501

        Phone number, including area code: '+1.' for Canada or '+33.' for France.   *With international calling code at the beginning.*   # noqa: E501

        :return: The registrant_phone of this ResellerapiRegisterdomainBody.  # noqa: E501
        :rtype: object
        """
        return self._registrant_phone

    @registrant_phone.setter
    def registrant_phone(self, registrant_phone):
        """Sets the registrant_phone of this ResellerapiRegisterdomainBody.

        Phone number, including area code: '+1.' for Canada or '+33.' for France.   *With international calling code at the beginning.*   # noqa: E501

        :param registrant_phone: The registrant_phone of this ResellerapiRegisterdomainBody.  # noqa: E501
        :type: object
        """
        if registrant_phone is None:
            raise ValueError("Invalid value for `registrant_phone`, must not be `None`")  # noqa: E501

        self._registrant_phone = registrant_phone

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
        if issubclass(ResellerapiRegisterdomainBody, dict):
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
        if not isinstance(other, ResellerapiRegisterdomainBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
