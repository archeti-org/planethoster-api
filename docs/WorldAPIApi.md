# planethoster.WorldAPIApi

All URIs are relative to *https://api.planethoster.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account**](WorldAPIApi.md#create_account) | **POST** /world-api/create-account | Create account
[**get_accounts**](WorldAPIApi.md#get_accounts) | **GET** /world-api/get-accounts | Get accounts
[**modify_resources**](WorldAPIApi.md#modify_resources) | **POST** /world-api/modify-resources | Modify resources
[**suspend_acccount**](WorldAPIApi.md#suspend_acccount) | **POST** /world-api/suspend-account | Suspend account
[**unsuspend_account**](WorldAPIApi.md#unsuspend_account) | **POST** /world-api/unsuspend-account | Unsuspend account

# **create_account**
> InlineResponse20022 create_account(body, x_api_user, x_api_key)

Create account

Creates a World hosting and assigns the requested resources.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.WorldAPIApi()
body = planethoster.WorldapiCreateaccountBody() # WorldapiCreateaccountBody | Create account parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Create account
    api_response = api_instance.create_account(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldAPIApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorldapiCreateaccountBody**](WorldapiCreateaccountBody.md)| Create account parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> InlineResponse20021 get_accounts(x_api_user, x_api_key)

Get accounts

Displays the World account and all World sub-accounts informations.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.WorldAPIApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Get accounts
    api_response = api_instance.get_accounts(x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldAPIApi->get_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_resources**
> InlineResponse20025 modify_resources(body, x_api_user, x_api_key)

Modify resources

Proceed to the activation of a suspended World account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.WorldAPIApi()
body = planethoster.WorldapiModifyresourcesBody() # WorldapiModifyresourcesBody | Modify resources parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Modify resources
    api_response = api_instance.modify_resources(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldAPIApi->modify_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorldapiModifyresourcesBody**](WorldapiModifyresourcesBody.md)| Modify resources parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_acccount**
> InlineResponse20023 suspend_acccount(body, x_api_user, x_api_key)

Suspend account

Proceed to the suspension of a World account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.WorldAPIApi()
body = planethoster.WorldapiSuspendaccountBody() # WorldapiSuspendaccountBody | Suspend account parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Suspend account
    api_response = api_instance.suspend_acccount(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldAPIApi->suspend_acccount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorldapiSuspendaccountBody**](WorldapiSuspendaccountBody.md)| Suspend account parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsuspend_account**
> InlineResponse20024 unsuspend_account(body, x_api_user, x_api_key)

Unsuspend account

Proceed to the activation of a suspended World account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.WorldAPIApi()
body = planethoster.WorldapiUnsuspendaccountBody() # WorldapiUnsuspendaccountBody | Unsuspend account parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Unsuspend account
    api_response = api_instance.unsuspend_account(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorldAPIApi->unsuspend_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorldapiUnsuspendaccountBody**](WorldapiUnsuspendaccountBody.md)| Unsuspend account parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

