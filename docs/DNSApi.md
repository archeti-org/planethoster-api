# planethoster.DNSApi

All URIs are relative to *https://api.planethoster.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**n0c_domain_edit_zone**](DNSApi.md#n0c_domain_edit_zone) | **POST** /n0c-api/dns/edit-zone | Edit / add zone records
[**n0c_domain_reset_zone**](DNSApi.md#n0c_domain_reset_zone) | **POST** /n0c-api/dns/reset-zone | Zone create / reset to default value
[**n0cdomain_get_zone**](DNSApi.md#n0cdomain_get_zone) | **GET** /n0c-api/dns/get-records | Get DNS zone

# **n0c_domain_edit_zone**
> InlineResponse20020 n0c_domain_edit_zone(body, x_api_user, x_api_key)

Edit / add zone records

Allows you to add or modify records on the DNS zone

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DNSApi()
body = planethoster.DnsEditzoneBody() # DnsEditzoneBody | 
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Edit / add zone records
    api_response = api_instance.n0c_domain_edit_zone(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DNSApi->n0c_domain_edit_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DnsEditzoneBody**](DnsEditzoneBody.md)|  | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_domain_reset_zone**
> InlineResponse20019 n0c_domain_reset_zone(body, x_api_user, x_api_key)

Zone create / reset to default value

Will add the default values of the dns zone.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DNSApi()
body = planethoster.DnsGetrecordsBody() # DnsGetrecordsBody | 
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Zone create / reset to default value
    api_response = api_instance.n0c_domain_reset_zone(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DNSApi->n0c_domain_reset_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DnsGetrecordsBody**](DnsGetrecordsBody.md)|  | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0cdomain_get_zone**
> InlineResponse20018 n0cdomain_get_zone(body, x_api_user, x_api_key)

Get DNS zone

Find the complete dns zone.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DNSApi()
body = planethoster.DnsGetrecordsBody() # DnsGetrecordsBody | Find the complete dns zone.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Get DNS zone
    api_response = api_instance.n0cdomain_get_zone(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DNSApi->n0cdomain_get_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DnsGetrecordsBody**](DnsGetrecordsBody.md)| Find the complete dns zone. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

