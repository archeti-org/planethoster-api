# planethoster.WordpressApi

All URIs are relative to *https://api.planethoster.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**n0c_get_wp**](WordpressApi.md#n0c_get_wp) | **GET** /n0c-api/wordpress | Get installed wordpress
[**n0c_wp_install**](WordpressApi.md#n0c_wp_install) | **POST** /n0c-api/wordpress/add | Wordpress installation
[**n0c_wp_remove**](WordpressApi.md#n0c_wp_remove) | **POST** /n0c-api/wordpress/remove | Delete wordpress installation

# **n0c_get_wp**
> InlineResponse20072 n0c_get_wp(body, x_api_user, x_api_key)

Get installed wordpress

Get Wordpress paths installed.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.WordpressApi()
body = planethoster.DomainRedirectionsBody() # DomainRedirectionsBody | World account ID parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Get installed wordpress
    api_response = api_instance.n0c_get_wp(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordpressApi->n0c_get_wp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRedirectionsBody**](DomainRedirectionsBody.md)| World account ID parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_wp_install**
> InlineResponse20073 n0c_wp_install(body, x_api_user, x_api_key)

Wordpress installation

Wordpress installation

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.WordpressApi()
body = planethoster.WordpressAddBody() # WordpressAddBody | World account settings credentials.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Wordpress installation
    api_response = api_instance.n0c_wp_install(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordpressApi->n0c_wp_install: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WordpressAddBody**](WordpressAddBody.md)| World account settings credentials. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20073**](InlineResponse20073.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_wp_remove**
> InlineResponse20073 n0c_wp_remove(body, x_api_user, x_api_key)

Delete wordpress installation

Removing a wordpress installation

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.WordpressApi()
body = planethoster.WordpressRemoveBody() # WordpressRemoveBody | World account settings credentials.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Delete wordpress installation
    api_response = api_instance.n0c_wp_remove(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordpressApi->n0c_wp_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WordpressRemoveBody**](WordpressRemoveBody.md)| World account settings credentials. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20073**](InlineResponse20073.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

