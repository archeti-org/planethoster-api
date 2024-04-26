# planethoster.DatabaseApi

All URIs are relative to *https://api.planethoster.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**n0c_create_database**](DatabaseApi.md#n0c_create_database) | **POST** /n0c-api/database/add | Add
[**n0c_create_database_user**](DatabaseApi.md#n0c_create_database_user) | **POST** /n0c-api/database/user/add | Add user
[**n0c_database_grant_permission**](DatabaseApi.md#n0c_database_grant_permission) | **POST** /n0c-api/database/user/grant-access | Grant permission
[**n0c_database_remove_permission**](DatabaseApi.md#n0c_database_remove_permission) | **POST** /n0c-api/database/user/remove-access | Remove permission
[**n0c_remove_database**](DatabaseApi.md#n0c_remove_database) | **POST** /n0c-api/database/remove | Remove
[**n0c_remove_database_user**](DatabaseApi.md#n0c_remove_database_user) | **POST** /n0c-api/database/user/remove | Remove user
[**n0c_users**](DatabaseApi.md#n0c_users) | **GET** /n0c-api/database/users | Users
[**noc_databases**](DatabaseApi.md#noc_databases) | **GET** /n0c-api/databases | Databases

# **n0c_create_database**
> InlineResponse20054 n0c_create_database(body, x_api_user, x_api_key)

Add

Create a new database.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DatabaseApi()
body = planethoster.DatabaseAddBody() # DatabaseAddBody | Create database parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Add
    api_response = api_instance.n0c_create_database(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->n0c_create_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DatabaseAddBody**](DatabaseAddBody.md)| Create database parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_create_database_user**
> InlineResponse20057 n0c_create_database_user(body, x_api_user, x_api_key)

Add user

Create a new database user.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DatabaseApi()
body = planethoster.UserAddBody() # UserAddBody | Create the database user parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Add user
    api_response = api_instance.n0c_create_database_user(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->n0c_create_database_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAddBody**](UserAddBody.md)| Create the database user parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_database_grant_permission**
> InlineResponse20059 n0c_database_grant_permission(body, x_api_user, x_api_key)

Grant permission

Grant access to a database for a user.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DatabaseApi()
body = planethoster.UserGrantaccessBody() # UserGrantaccessBody | Grant permission parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Grant permission
    api_response = api_instance.n0c_database_grant_permission(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->n0c_database_grant_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGrantaccessBody**](UserGrantaccessBody.md)| Grant permission parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_database_remove_permission**
> InlineResponse20060 n0c_database_remove_permission(body, x_api_user, x_api_key)

Remove permission

Remove access to a database for an user.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DatabaseApi()
body = planethoster.UserGrantaccessBody() # UserGrantaccessBody | Remove permission parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Remove permission
    api_response = api_instance.n0c_database_remove_permission(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->n0c_database_remove_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGrantaccessBody**](UserGrantaccessBody.md)| Remove permission parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_remove_database**
> InlineResponse20055 n0c_remove_database(body, x_api_user, x_api_key)

Remove

Remove database.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DatabaseApi()
body = planethoster.DatabaseAddBody() # DatabaseAddBody | Remove database parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Remove
    api_response = api_instance.n0c_remove_database(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->n0c_remove_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DatabaseAddBody**](DatabaseAddBody.md)| Remove database parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_remove_database_user**
> InlineResponse20058 n0c_remove_database_user(body, x_api_user, x_api_key)

Remove user

Remove a database user.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DatabaseApi()
body = planethoster.UserRemoveBody() # UserRemoveBody | Remove database user parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Remove user
    api_response = api_instance.n0c_remove_database_user(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->n0c_remove_database_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserRemoveBody**](UserRemoveBody.md)| Remove database user parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_users**
> InlineResponse20056 n0c_users(body, x_api_user, x_api_key)

Users

Get World account database users.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DatabaseApi()
body = planethoster.DomainRedirectionsBody() # DomainRedirectionsBody | World account ID parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Users
    api_response = api_instance.n0c_users(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->n0c_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRedirectionsBody**](DomainRedirectionsBody.md)| World account ID parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **noc_databases**
> InlineResponse20053 noc_databases(body, x_api_user, x_api_key)

Databases

Get World account databases.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DatabaseApi()
body = planethoster.DomainRedirectionsBody() # DomainRedirectionsBody | World account ID parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Databases
    api_response = api_instance.noc_databases(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->noc_databases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRedirectionsBody**](DomainRedirectionsBody.md)| World account ID parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

