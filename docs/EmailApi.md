# planethoster.EmailApi

All URIs are relative to *https://api.planethoster.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**n0c_add_email**](EmailApi.md#n0c_add_email) | **POST** /n0c-api/email/add | Add
[**n0c_disable_auth**](EmailApi.md#n0c_disable_auth) | **POST** /n0c-api/email/auth/disable | Disable Authentication
[**n0c_email_auth**](EmailApi.md#n0c_email_auth) | **GET** /n0c-api/email/auths | Authentication
[**n0c_email_change_password**](EmailApi.md#n0c_email_change_password) | **POST** /n0c-api/email/change-password | Change password
[**n0c_email_change_quota**](EmailApi.md#n0c_email_change_quota) | **POST** /n0c-api/email/change-quota | Change quota
[**n0c_emails**](EmailApi.md#n0c_emails) | **GET** /n0c-api/emails | Emails
[**n0c_enable_auth**](EmailApi.md#n0c_enable_auth) | **POST** /n0c-api/email/auth/enable | Enable Authentication
[**n0c_remove_email**](EmailApi.md#n0c_remove_email) | **POST** /n0c-api/email/remove | Remove
[**n0c_suspend_emails**](EmailApi.md#n0c_suspend_emails) | **POST** /n0c-api/email/suspend | Suspend emails
[**n0c_unsuspend_emails**](EmailApi.md#n0c_unsuspend_emails) | **POST** /n0c-api/email/unsuspend | Unsuspend emails

# **n0c_add_email**
> InlineResponse20045 n0c_add_email(x_api_user, x_api_key, body=body)

Add

Create a new email address.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.EmailApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
body = planethoster.EmailAddBody() # EmailAddBody | Add email parameters. (optional)

try:
    # Add
    api_response = api_instance.n0c_add_email(x_api_user, x_api_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->n0c_add_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **body** | [**EmailAddBody**](EmailAddBody.md)| Add email parameters. | [optional] 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_disable_auth**
> InlineResponse20052 n0c_disable_auth(x_api_user, x_api_key, body=body)

Disable Authentication

Disable email authentication.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.EmailApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
body = planethoster.AuthDisableBody() # AuthDisableBody | Email authentication parameters. (optional)

try:
    # Disable Authentication
    api_response = api_instance.n0c_disable_auth(x_api_user, x_api_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->n0c_disable_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **body** | [**AuthDisableBody**](AuthDisableBody.md)| Email authentication parameters. | [optional] 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_email_auth**
> InlineResponse20050 n0c_email_auth(x_api_user, x_api_key, body=body)

Authentication

List email authentication.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.EmailApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
body = planethoster.EmailRemoveBody() # EmailRemoveBody | Email authentication parameters. (optional)

try:
    # Authentication
    api_response = api_instance.n0c_email_auth(x_api_user, x_api_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->n0c_email_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **body** | [**EmailRemoveBody**](EmailRemoveBody.md)| Email authentication parameters. | [optional] 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_email_change_password**
> InlineResponse20047 n0c_email_change_password(x_api_user, x_api_key, body=body)

Change password

Change the password of an email account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.EmailApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
body = planethoster.EmailChangepasswordBody() # EmailChangepasswordBody | Change the parameters of the password. (optional)

try:
    # Change password
    api_response = api_instance.n0c_email_change_password(x_api_user, x_api_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->n0c_email_change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **body** | [**EmailChangepasswordBody**](EmailChangepasswordBody.md)| Change the parameters of the password. | [optional] 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_email_change_quota**
> InlineResponse20047 n0c_email_change_quota(x_api_user, x_api_key, body=body)

Change quota

Change quota of an email account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.EmailApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
body = planethoster.EmailChangequotaBody() # EmailChangequotaBody | Change quota parameters. (optional)

try:
    # Change quota
    api_response = api_instance.n0c_email_change_quota(x_api_user, x_api_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->n0c_email_change_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **body** | [**EmailChangequotaBody**](EmailChangequotaBody.md)| Change quota parameters. | [optional] 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_emails**
> InlineResponse20044 n0c_emails(body, x_api_user, x_api_key)

Emails

Get all account emails.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.EmailApi()
body = planethoster.DomainRedirectionsBody() # DomainRedirectionsBody | World account ID parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Emails
    api_response = api_instance.n0c_emails(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->n0c_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRedirectionsBody**](DomainRedirectionsBody.md)| World account ID parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_enable_auth**
> InlineResponse20051 n0c_enable_auth(x_api_user, x_api_key, body=body)

Enable Authentication

Enable email authentication.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.EmailApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
body = planethoster.AuthEnableBody() # AuthEnableBody | Email authentication parameters. (optional)

try:
    # Enable Authentication
    api_response = api_instance.n0c_enable_auth(x_api_user, x_api_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->n0c_enable_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **body** | [**AuthEnableBody**](AuthEnableBody.md)| Email authentication parameters. | [optional] 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_remove_email**
> InlineResponse20046 n0c_remove_email(x_api_user, x_api_key, body=body)

Remove

Remove an email address.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.EmailApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
body = planethoster.EmailRemoveBody() # EmailRemoveBody | Remove email parameters. (optional)

try:
    # Remove
    api_response = api_instance.n0c_remove_email(x_api_user, x_api_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->n0c_remove_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **body** | [**EmailRemoveBody**](EmailRemoveBody.md)| Remove email parameters. | [optional] 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_suspend_emails**
> InlineResponse20048 n0c_suspend_emails(x_api_user, x_api_key, body=body)

Suspend emails

Suspend multiple email addresses.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.EmailApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
body = planethoster.EmailSuspendBody() # EmailSuspendBody | Suspend emails parameters. (optional)

try:
    # Suspend emails
    api_response = api_instance.n0c_suspend_emails(x_api_user, x_api_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->n0c_suspend_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **body** | [**EmailSuspendBody**](EmailSuspendBody.md)| Suspend emails parameters. | [optional] 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_unsuspend_emails**
> InlineResponse20049 n0c_unsuspend_emails(x_api_user, x_api_key, body=body)

Unsuspend emails

Unsuspend multiple email addresses.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.EmailApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
body = planethoster.EmailUnsuspendBody() # EmailUnsuspendBody | Unsuspend emails parameters. (optional)

try:
    # Unsuspend emails
    api_response = api_instance.n0c_unsuspend_emails(x_api_user, x_api_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->n0c_unsuspend_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **body** | [**EmailUnsuspendBody**](EmailUnsuspendBody.md)| Unsuspend emails parameters. | [optional] 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

