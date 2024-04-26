# planethoster.FTPApi

All URIs are relative to *https://api.planethoster.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**n0c_change_ftp_password**](FTPApi.md#n0c_change_ftp_password) | **POST** /n0c-api/ftp-account/password | Change password
[**n0c_create_ftp**](FTPApi.md#n0c_create_ftp) | **POST** /n0c-api/ftp-account/add | Add
[**n0c_ftp_update_path**](FTPApi.md#n0c_ftp_update_path) | **POST** /n0c-api/ftp-account/update-path | Update path
[**n0c_get_ftp**](FTPApi.md#n0c_get_ftp) | **GET** /n0c-api/ftp-accounts | FTP accounts
[**n0c_list_ftp_connections**](FTPApi.md#n0c_list_ftp_connections) | **GET** /n0c-api/ftp-account/active-connection | List connections
[**n0c_remove_ftp**](FTPApi.md#n0c_remove_ftp) | **POST** /n0c-api/ftp-account/remove | Remove

# **n0c_change_ftp_password**
> InlineResponse20069 n0c_change_ftp_password(body, x_api_user, x_api_key)

Change password

Change the password of the FTP account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.FTPApi()
body = planethoster.FtpaccountPasswordBody() # FtpaccountPasswordBody | FTP change password parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Change password
    api_response = api_instance.n0c_change_ftp_password(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FTPApi->n0c_change_ftp_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FtpaccountPasswordBody**](FtpaccountPasswordBody.md)| FTP change password parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_create_ftp**
> InlineResponse20067 n0c_create_ftp(body, x_api_user, x_api_key)

Add

Create an FTP account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.FTPApi()
body = planethoster.FtpaccountAddBody() # FtpaccountAddBody | FTP account creation parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Add
    api_response = api_instance.n0c_create_ftp(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FTPApi->n0c_create_ftp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FtpaccountAddBody**](FtpaccountAddBody.md)| FTP account creation parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20067**](InlineResponse20067.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_ftp_update_path**
> InlineResponse20070 n0c_ftp_update_path(body, x_api_user, x_api_key)

Update path

Update the path of the FTP account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.FTPApi()
body = planethoster.FtpaccountUpdatepathBody() # FtpaccountUpdatepathBody | Parameters for changing FTP account path.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Update path
    api_response = api_instance.n0c_ftp_update_path(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FTPApi->n0c_ftp_update_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FtpaccountUpdatepathBody**](FtpaccountUpdatepathBody.md)| Parameters for changing FTP account path. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20070**](InlineResponse20070.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_get_ftp**
> InlineResponse20066 n0c_get_ftp(body, x_api_user, x_api_key)

FTP accounts

Get all FTP accounts.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.FTPApi()
body = planethoster.DomainRedirectionsBody() # DomainRedirectionsBody | World account ID parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # FTP accounts
    api_response = api_instance.n0c_get_ftp(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FTPApi->n0c_get_ftp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRedirectionsBody**](DomainRedirectionsBody.md)| World account ID parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20066**](InlineResponse20066.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_list_ftp_connections**
> InlineResponse20071 n0c_list_ftp_connections(body, x_api_user, x_api_key)

List connections

List all active connections.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.FTPApi()
body = planethoster.DomainRedirectionsBody() # DomainRedirectionsBody | World account ID parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # List connections
    api_response = api_instance.n0c_list_ftp_connections(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FTPApi->n0c_list_ftp_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRedirectionsBody**](DomainRedirectionsBody.md)| World account ID parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_remove_ftp**
> InlineResponse20068 n0c_remove_ftp(body, x_api_user, x_api_key)

Remove

Remove an FTP account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.FTPApi()
body = planethoster.FtpaccountRemoveBody() # FtpaccountRemoveBody | Remove FTP account creation parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Remove
    api_response = api_instance.n0c_remove_ftp(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FTPApi->n0c_remove_ftp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FtpaccountRemoveBody**](FtpaccountRemoveBody.md)| Remove FTP account creation parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20068**](InlineResponse20068.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

