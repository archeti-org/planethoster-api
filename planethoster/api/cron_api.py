# coding: utf-8

"""
    PlanetHoster API

    | <a href=\"https://apidoc.planethoster.com/fr\">Version Française</a> ## Description The PlanetHoster API allows actions related to domain management and web hosting. ## Details - SSL only: we require that all requests be done over encrypted TLS/SSL connections. - Supported HTTP verbs are GET and POST. If your client does not support all HTTP verbs, you can override the verb with X-Http-Method-Override HTTP header. - Unless otherwise specified in the method documentation, all successful API calls return an **HTTP code 200** with a JSON object. - Errors are returned with an HTTP code 4XX or 5XX, a JSON object with properties \"error\" (an error message) and an \"error_code\" (optional, an integer). - Every string passed to and from the API needs to be UTF-8 encoded. - The API sends ETag headers and supports the If-None-Match header. - Unless otherwise specified, all API methods require authentication with api_user and api_key.  ## Authentication and whitelist 1. In order to be able to contact the API, you must whitelist your IPs. 2. API user and API key are required in the HTTP header.  Whitelisted IP and credentials can be found in the <a href=\"https://my.planethoster.com/domain-reseller\" target=\"_blank\">PlanetHoster Client Area / Reseller section</a>.  <SecurityDefinitions />   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: tech@support.planethoster.info
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from planethoster.api_client import ApiClient


class CronApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def n0c_add_cron(self, body, x_api_user, x_api_key, **kwargs):  # noqa: E501
        """Add  # noqa: E501

        Add cron to the World account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.n0c_add_cron(body, x_api_user, x_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CronAddBody body: Add cron parameters. (required)
        :param object x_api_user: API user provided in the client area. (required)
        :param object x_api_key: API key provided in the client area. (required)
        :return: InlineResponse20062
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.n0c_add_cron_with_http_info(body, x_api_user, x_api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.n0c_add_cron_with_http_info(body, x_api_user, x_api_key, **kwargs)  # noqa: E501
            return data

    def n0c_add_cron_with_http_info(self, body, x_api_user, x_api_key, **kwargs):  # noqa: E501
        """Add  # noqa: E501

        Add cron to the World account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.n0c_add_cron_with_http_info(body, x_api_user, x_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CronAddBody body: Add cron parameters. (required)
        :param object x_api_user: API user provided in the client area. (required)
        :param object x_api_key: API key provided in the client area. (required)
        :return: InlineResponse20062
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_api_user', 'x_api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method n0c_add_cron" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `n0c_add_cron`")  # noqa: E501
        # verify the required parameter 'x_api_user' is set
        if ('x_api_user' not in params or
                params['x_api_user'] is None):
            raise ValueError("Missing the required parameter `x_api_user` when calling `n0c_add_cron`")  # noqa: E501
        # verify the required parameter 'x_api_key' is set
        if ('x_api_key' not in params or
                params['x_api_key'] is None):
            raise ValueError("Missing the required parameter `x_api_key` when calling `n0c_add_cron`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_api_user' in params:
            header_params['X-API-USER'] = params['x_api_user']  # noqa: E501
        if 'x_api_key' in params:
            header_params['X-API-KEY'] = params['x_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/n0c-api/cron/add', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20062',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def n0c_add_cron_email(self, body, x_api_user, x_api_key, **kwargs):  # noqa: E501
        """Set email  # noqa: E501

        Set cron email.   This email will receive the stdout of the command.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.n0c_add_cron_email(body, x_api_user, x_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmailSetBody body: Set cron email parameters. (required)
        :param object x_api_user: API user provided in the client area. (required)
        :param object x_api_key: API key provided in the client area. (required)
        :return: InlineResponse20064
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.n0c_add_cron_email_with_http_info(body, x_api_user, x_api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.n0c_add_cron_email_with_http_info(body, x_api_user, x_api_key, **kwargs)  # noqa: E501
            return data

    def n0c_add_cron_email_with_http_info(self, body, x_api_user, x_api_key, **kwargs):  # noqa: E501
        """Set email  # noqa: E501

        Set cron email.   This email will receive the stdout of the command.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.n0c_add_cron_email_with_http_info(body, x_api_user, x_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmailSetBody body: Set cron email parameters. (required)
        :param object x_api_user: API user provided in the client area. (required)
        :param object x_api_key: API key provided in the client area. (required)
        :return: InlineResponse20064
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_api_user', 'x_api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method n0c_add_cron_email" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `n0c_add_cron_email`")  # noqa: E501
        # verify the required parameter 'x_api_user' is set
        if ('x_api_user' not in params or
                params['x_api_user'] is None):
            raise ValueError("Missing the required parameter `x_api_user` when calling `n0c_add_cron_email`")  # noqa: E501
        # verify the required parameter 'x_api_key' is set
        if ('x_api_key' not in params or
                params['x_api_key'] is None):
            raise ValueError("Missing the required parameter `x_api_key` when calling `n0c_add_cron_email`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_api_user' in params:
            header_params['X-API-USER'] = params['x_api_user']  # noqa: E501
        if 'x_api_key' in params:
            header_params['X-API-KEY'] = params['x_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/n0c-api/cron/email/set', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20064',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def n0c_get_cron(self, body, x_api_user, x_api_key, **kwargs):  # noqa: E501
        """Crons  # noqa: E501

        Get world the cron jobs of the World account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.n0c_get_cron(body, x_api_user, x_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DomainRedirectionsBody body: World account ID parameters. (required)
        :param object x_api_user: API user provided in the client area. (required)
        :param object x_api_key: API key provided in the client area. (required)
        :return: InlineResponse20061
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.n0c_get_cron_with_http_info(body, x_api_user, x_api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.n0c_get_cron_with_http_info(body, x_api_user, x_api_key, **kwargs)  # noqa: E501
            return data

    def n0c_get_cron_with_http_info(self, body, x_api_user, x_api_key, **kwargs):  # noqa: E501
        """Crons  # noqa: E501

        Get world the cron jobs of the World account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.n0c_get_cron_with_http_info(body, x_api_user, x_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DomainRedirectionsBody body: World account ID parameters. (required)
        :param object x_api_user: API user provided in the client area. (required)
        :param object x_api_key: API key provided in the client area. (required)
        :return: InlineResponse20061
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_api_user', 'x_api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method n0c_get_cron" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `n0c_get_cron`")  # noqa: E501
        # verify the required parameter 'x_api_user' is set
        if ('x_api_user' not in params or
                params['x_api_user'] is None):
            raise ValueError("Missing the required parameter `x_api_user` when calling `n0c_get_cron`")  # noqa: E501
        # verify the required parameter 'x_api_key' is set
        if ('x_api_key' not in params or
                params['x_api_key'] is None):
            raise ValueError("Missing the required parameter `x_api_key` when calling `n0c_get_cron`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_api_user' in params:
            header_params['X-API-USER'] = params['x_api_user']  # noqa: E501
        if 'x_api_key' in params:
            header_params['X-API-KEY'] = params['x_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/n0c-api/crons', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20061',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def n0c_remove_cron(self, body, x_api_user, x_api_key, **kwargs):  # noqa: E501
        """Remove  # noqa: E501

        Remove an existing cron job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.n0c_remove_cron(body, x_api_user, x_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CronRemoveBody body: Remove cron parameters. (required)
        :param object x_api_user: API user provided in the client area. (required)
        :param object x_api_key: API key provided in the client area. (required)
        :return: InlineResponse20063
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.n0c_remove_cron_with_http_info(body, x_api_user, x_api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.n0c_remove_cron_with_http_info(body, x_api_user, x_api_key, **kwargs)  # noqa: E501
            return data

    def n0c_remove_cron_with_http_info(self, body, x_api_user, x_api_key, **kwargs):  # noqa: E501
        """Remove  # noqa: E501

        Remove an existing cron job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.n0c_remove_cron_with_http_info(body, x_api_user, x_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CronRemoveBody body: Remove cron parameters. (required)
        :param object x_api_user: API user provided in the client area. (required)
        :param object x_api_key: API key provided in the client area. (required)
        :return: InlineResponse20063
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_api_user', 'x_api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method n0c_remove_cron" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `n0c_remove_cron`")  # noqa: E501
        # verify the required parameter 'x_api_user' is set
        if ('x_api_user' not in params or
                params['x_api_user'] is None):
            raise ValueError("Missing the required parameter `x_api_user` when calling `n0c_remove_cron`")  # noqa: E501
        # verify the required parameter 'x_api_key' is set
        if ('x_api_key' not in params or
                params['x_api_key'] is None):
            raise ValueError("Missing the required parameter `x_api_key` when calling `n0c_remove_cron`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_api_user' in params:
            header_params['X-API-USER'] = params['x_api_user']  # noqa: E501
        if 'x_api_key' in params:
            header_params['X-API-KEY'] = params['x_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/n0c-api/cron/remove', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20063',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def n0c_remove_cron_email(self, body, x_api_user, x_api_key, **kwargs):  # noqa: E501
        """Remove email  # noqa: E501

        Remove cron email.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.n0c_remove_cron_email(body, x_api_user, x_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DomainRedirectionsBody body: World account ID parameters. (required)
        :param object x_api_user: API user provided in the client area. (required)
        :param object x_api_key: API key provided in the client area. (required)
        :return: InlineResponse20065
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.n0c_remove_cron_email_with_http_info(body, x_api_user, x_api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.n0c_remove_cron_email_with_http_info(body, x_api_user, x_api_key, **kwargs)  # noqa: E501
            return data

    def n0c_remove_cron_email_with_http_info(self, body, x_api_user, x_api_key, **kwargs):  # noqa: E501
        """Remove email  # noqa: E501

        Remove cron email.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.n0c_remove_cron_email_with_http_info(body, x_api_user, x_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DomainRedirectionsBody body: World account ID parameters. (required)
        :param object x_api_user: API user provided in the client area. (required)
        :param object x_api_key: API key provided in the client area. (required)
        :return: InlineResponse20065
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_api_user', 'x_api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method n0c_remove_cron_email" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `n0c_remove_cron_email`")  # noqa: E501
        # verify the required parameter 'x_api_user' is set
        if ('x_api_user' not in params or
                params['x_api_user'] is None):
            raise ValueError("Missing the required parameter `x_api_user` when calling `n0c_remove_cron_email`")  # noqa: E501
        # verify the required parameter 'x_api_key' is set
        if ('x_api_key' not in params or
                params['x_api_key'] is None):
            raise ValueError("Missing the required parameter `x_api_key` when calling `n0c_remove_cron_email`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_api_user' in params:
            header_params['X-API-USER'] = params['x_api_user']  # noqa: E501
        if 'x_api_key' in params:
            header_params['X-API-KEY'] = params['x_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/n0c-api/cron/email/remove', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20065',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
