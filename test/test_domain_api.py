# coding: utf-8

"""
    PlanetHoster API

    | <a href=\"https://apidoc.planethoster.com/fr\">Version Française</a> ## Description The PlanetHoster API allows actions related to domain management and web hosting. ## Details - SSL only: we require that all requests be done over encrypted TLS/SSL connections. - Supported HTTP verbs are GET and POST. If your client does not support all HTTP verbs, you can override the verb with X-Http-Method-Override HTTP header. - Unless otherwise specified in the method documentation, all successful API calls return an **HTTP code 200** with a JSON object. - Errors are returned with an HTTP code 4XX or 5XX, a JSON object with properties \"error\" (an error message) and an \"error_code\" (optional, an integer). - Every string passed to and from the API needs to be UTF-8 encoded. - The API sends ETag headers and supports the If-None-Match header. - Unless otherwise specified, all API methods require authentication with api_user and api_key.  ## Authentication and whitelist 1. In order to be able to contact the API, you must whitelist your IPs. 2. API user and API key are required in the HTTP header.  Whitelisted IP and credentials can be found in the <a href=\"https://my.planethoster.com/domain-reseller\" target=\"_blank\">PlanetHoster Client Area / Reseller section</a>.  <SecurityDefinitions />   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: tech@support.planethoster.info
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import planethoster
from planethoster.api.domain_api import DomainApi  # noqa: E501
from planethoster.rest import ApiException


class TestDomainApi(unittest.TestCase):
    """DomainApi unit test stubs"""

    def setUp(self):
        self.api = DomainApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_n0c_add_domain(self):
        """Test case for n0c_add_domain

        Add  # noqa: E501
        """
        pass

    def test_n0c_add_sub_domain(self):
        """Test case for n0c_add_sub_domain

        Add sub-domain  # noqa: E501
        """
        pass

    def test_n0c_change_doc_root(self):
        """Test case for n0c_change_doc_root

        Change doc-root  # noqa: E501
        """
        pass

    def test_n0c_delete_redirection(self):
        """Test case for n0c_delete_redirection

        Delete redirection  # noqa: E501
        """
        pass

    def test_n0c_domain_waf_logs(self):
        """Test case for n0c_domain_waf_logs

        WAF logs  # noqa: E501
        """
        pass

    def test_n0c_domain_waf_rules(self):
        """Test case for n0c_domain_waf_rules

        WAF rules  # noqa: E501
        """
        pass

    def test_n0c_domains(self):
        """Test case for n0c_domains

        Domains  # noqa: E501
        """
        pass

    def test_n0c_redirections(self):
        """Test case for n0c_redirections

        Redirections  # noqa: E501
        """
        pass

    def test_n0c_remove_domain(self):
        """Test case for n0c_remove_domain

        Remove  # noqa: E501
        """
        pass

    def test_n0c_set_external_redirection(self):
        """Test case for n0c_set_external_redirection

        External redirection  # noqa: E501
        """
        pass

    def test_n0c_set_rediction(self):
        """Test case for n0c_set_rediction

        Internal redirection  # noqa: E501
        """
        pass

    def test_n0c_suspend_domain(self):
        """Test case for n0c_suspend_domain

        Suspend domains  # noqa: E501
        """
        pass

    def test_n0c_unsuspend_domain(self):
        """Test case for n0c_unsuspend_domain

        Unsuspend domains  # noqa: E501
        """
        pass

    def test_n0c_update_waf_rules(self):
        """Test case for n0c_update_waf_rules

        Update waf rules  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()