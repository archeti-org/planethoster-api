# planethoster.CronApi

All URIs are relative to *https://api.planethoster.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**n0c_add_cron**](CronApi.md#n0c_add_cron) | **POST** /n0c-api/cron/add | Add
[**n0c_add_cron_email**](CronApi.md#n0c_add_cron_email) | **POST** /n0c-api/cron/email/set | Set email
[**n0c_get_cron**](CronApi.md#n0c_get_cron) | **GET** /n0c-api/crons | Crons
[**n0c_remove_cron**](CronApi.md#n0c_remove_cron) | **POST** /n0c-api/cron/remove | Remove
[**n0c_remove_cron_email**](CronApi.md#n0c_remove_cron_email) | **POST** /n0c-api/cron/email/remove | Remove email

# **n0c_add_cron**
> InlineResponse20062 n0c_add_cron(body, x_api_user, x_api_key)

Add

Add cron to the World account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.CronApi()
body = planethoster.CronAddBody() # CronAddBody | Add cron parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Add
    api_response = api_instance.n0c_add_cron(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CronApi->n0c_add_cron: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CronAddBody**](CronAddBody.md)| Add cron parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_add_cron_email**
> InlineResponse20064 n0c_add_cron_email(body, x_api_user, x_api_key)

Set email

Set cron email.   This email will receive the stdout of the command. 

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.CronApi()
body = planethoster.EmailSetBody() # EmailSetBody | Set cron email parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Set email
    api_response = api_instance.n0c_add_cron_email(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CronApi->n0c_add_cron_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailSetBody**](EmailSetBody.md)| Set cron email parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_get_cron**
> InlineResponse20061 n0c_get_cron(body, x_api_user, x_api_key)

Crons

Get world the cron jobs of the World account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.CronApi()
body = planethoster.DomainRedirectionsBody() # DomainRedirectionsBody | World account ID parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Crons
    api_response = api_instance.n0c_get_cron(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CronApi->n0c_get_cron: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRedirectionsBody**](DomainRedirectionsBody.md)| World account ID parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_remove_cron**
> InlineResponse20063 n0c_remove_cron(body, x_api_user, x_api_key)

Remove

Remove an existing cron job.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.CronApi()
body = planethoster.CronRemoveBody() # CronRemoveBody | Remove cron parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Remove
    api_response = api_instance.n0c_remove_cron(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CronApi->n0c_remove_cron: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CronRemoveBody**](CronRemoveBody.md)| Remove cron parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_remove_cron_email**
> InlineResponse20065 n0c_remove_cron_email(body, x_api_user, x_api_key)

Remove email

Remove cron email. 

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.CronApi()
body = planethoster.DomainRedirectionsBody() # DomainRedirectionsBody | World account ID parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Remove email
    api_response = api_instance.n0c_remove_cron_email(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CronApi->n0c_remove_cron_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRedirectionsBody**](DomainRedirectionsBody.md)| World account ID parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

