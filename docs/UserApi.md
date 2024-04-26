# planethoster.UserApi

All URIs are relative to *https://api.planethoster.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_n0c_temp_domain**](UserApi.md#disable_n0c_temp_domain) | **POST** /n0c-api/user/disable-temp-domain | Disable temporary domain
[**n0c_add_ssh_key**](UserApi.md#n0c_add_ssh_key) | **POST** /n0c-api/user/add-ssh-key | Add SSH key
[**n0c_edit_ssh_key**](UserApi.md#n0c_edit_ssh_key) | **POST** /n0c-api/user/edit-ssh-key | Edit SSH key
[**n0c_remove_ssh_key**](UserApi.md#n0c_remove_ssh_key) | **POST** /n0c-api/user/remove-ssh-key | Remove SSH key
[**n0c_ssh_keys**](UserApi.md#n0c_ssh_keys) | **GET** /n0c-api/user/ssh-keys | SSH keys
[**n0c_temp_domain**](UserApi.md#n0c_temp_domain) | **POST** /n0c-api/user/temp-domain | Temporary domain

# **disable_n0c_temp_domain**
> InlineResponse20027 disable_n0c_temp_domain(body, x_api_user, x_api_key)

Disable temporary domain

Disable the temporary domain.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.UserApi()
body = planethoster.UserDisabletempdomainBody() # UserDisabletempdomainBody | Temporary domain parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Disable temporary domain
    api_response = api_instance.disable_n0c_temp_domain(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->disable_n0c_temp_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserDisabletempdomainBody**](UserDisabletempdomainBody.md)| Temporary domain parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_add_ssh_key**
> InlineResponse20029 n0c_add_ssh_key(x_api_user, x_api_key, body=body)

Add SSH key

Add a SSH key to the World account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.UserApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
body = planethoster.UserAddsshkeyBody() # UserAddsshkeyBody | SSH key parameters. (optional)

try:
    # Add SSH key
    api_response = api_instance.n0c_add_ssh_key(x_api_user, x_api_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->n0c_add_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **body** | [**UserAddsshkeyBody**](UserAddsshkeyBody.md)| SSH key parameters. | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_edit_ssh_key**
> InlineResponse20030 n0c_edit_ssh_key(x_api_user, x_api_key, body=body)

Edit SSH key

Edit an existing SSH key.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.UserApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
body = planethoster.UserEditsshkeyBody() # UserEditsshkeyBody | SSH key parameters. (optional)

try:
    # Edit SSH key
    api_response = api_instance.n0c_edit_ssh_key(x_api_user, x_api_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->n0c_edit_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **body** | [**UserEditsshkeyBody**](UserEditsshkeyBody.md)| SSH key parameters. | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_remove_ssh_key**
> InlineResponse20031 n0c_remove_ssh_key(x_api_user, x_api_key, body=body)

Remove SSH key

Remove an existing SSH key.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.UserApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
body = planethoster.UserRemovesshkeyBody() # UserRemovesshkeyBody | SSH key parameters. (optional)

try:
    # Remove SSH key
    api_response = api_instance.n0c_remove_ssh_key(x_api_user, x_api_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->n0c_remove_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **body** | [**UserRemovesshkeyBody**](UserRemovesshkeyBody.md)| SSH key parameters. | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_ssh_keys**
> InlineResponse20028 n0c_ssh_keys(body, x_api_user, x_api_key)

SSH keys

Get SSH keys installed for an account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.UserApi()
body = planethoster.UserTempdomainBody() # UserTempdomainBody | SSH keys parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # SSH keys
    api_response = api_instance.n0c_ssh_keys(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->n0c_ssh_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserTempdomainBody**](UserTempdomainBody.md)| SSH keys parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_temp_domain**
> InlineResponse20026 n0c_temp_domain(body, x_api_user, x_api_key)

Temporary domain

Generate a free temporary domain to access your main website.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.UserApi()
body = planethoster.UserTempdomainBody() # UserTempdomainBody | Temporary domain parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Temporary domain
    api_response = api_instance.n0c_temp_domain(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->n0c_temp_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserTempdomainBody**](UserTempdomainBody.md)| Temporary domain parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

