# planethoster.StatsApi

All URIs are relative to *https://api.planethoster.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**n0c_apache_stats**](StatsApi.md#n0c_apache_stats) | **POST** /n0c-api/stats/apache | Stats apache
[**n0c_apache_unique_stats**](StatsApi.md#n0c_apache_unique_stats) | **POST** /n0c-api/stats/apache/unique | Stats apache (Unique Visitor)
[**n0c_disk_usage**](StatsApi.md#n0c_disk_usage) | **GET** /n0c-api/stats/disk-usage | Disk usage
[**n0c_stats_performance**](StatsApi.md#n0c_stats_performance) | **POST** /n0c-api/stats/performance | Performance

# **n0c_apache_stats**
> InlineResponse20080 n0c_apache_stats(body, x_api_user, x_api_key)

Stats apache

Web server statistics (Visits)

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.StatsApi()
body = planethoster.StatsApacheBody() # StatsApacheBody | World account settings credentials.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Stats apache
    api_response = api_instance.n0c_apache_stats(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->n0c_apache_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatsApacheBody**](StatsApacheBody.md)| World account settings credentials. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20080**](InlineResponse20080.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_apache_unique_stats**
> InlineResponse20081 n0c_apache_unique_stats(body, x_api_user, x_api_key)

Stats apache (Unique Visitor)

Web server statistics (Visits)

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.StatsApi()
body = planethoster.ApacheUniqueBody() # ApacheUniqueBody | World account settings credentials.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Stats apache (Unique Visitor)
    api_response = api_instance.n0c_apache_unique_stats(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->n0c_apache_unique_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApacheUniqueBody**](ApacheUniqueBody.md)| World account settings credentials. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20081**](InlineResponse20081.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_disk_usage**
> InlineResponse20079 n0c_disk_usage(body, x_api_user, x_api_key)

Disk usage

Returns disk space usage (response always in BYTE)

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.StatsApi()
body = planethoster.StatsDiskusageBody() # StatsDiskusageBody | World account settings credentials.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Disk usage
    api_response = api_instance.n0c_disk_usage(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->n0c_disk_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatsDiskusageBody**](StatsDiskusageBody.md)| World account settings credentials. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20079**](InlineResponse20079.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_stats_performance**
> InlineResponse20078 n0c_stats_performance(body, x_api_user, x_api_key)

Performance

Retrieve performance data

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.StatsApi()
body = planethoster.StatsPerformanceBody() # StatsPerformanceBody | World account settings credentials.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Performance
    api_response = api_instance.n0c_stats_performance(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->n0c_stats_performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatsPerformanceBody**](StatsPerformanceBody.md)| World account settings credentials. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20078**](InlineResponse20078.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

