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
from planethoster.api.ftp_api import FTPApi  # noqa: E501
from planethoster.rest import ApiException


class TestFTPApi(unittest.TestCase):
    """FTPApi unit test stubs"""

    def setUp(self):
        self.api = FTPApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_n0c_change_ftp_password(self):
        """Test case for n0c_change_ftp_password

        Change password  # noqa: E501
        """
        pass

    def test_n0c_create_ftp(self):
        """Test case for n0c_create_ftp

        Add  # noqa: E501
        """
        pass

    def test_n0c_ftp_update_path(self):
        """Test case for n0c_ftp_update_path

        Update path  # noqa: E501
        """
        pass

    def test_n0c_get_ftp(self):
        """Test case for n0c_get_ftp

        FTP accounts  # noqa: E501
        """
        pass

    def test_n0c_list_ftp_connections(self):
        """Test case for n0c_list_ftp_connections

        List connections  # noqa: E501
        """
        pass

    def test_n0c_remove_ftp(self):
        """Test case for n0c_remove_ftp

        Remove  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
