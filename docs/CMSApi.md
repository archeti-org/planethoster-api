# planethoster.CMSApi

All URIs are relative to *https://api.planethoster.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cms_list_available**](CMSApi.md#cms_list_available) | **GET** /n0c-api/cms/list-available | List of CMS available
[**cms_list_installed**](CMSApi.md#cms_list_installed) | **GET** /n0c-api/cms/list-installed | List the installed CMS
[**cms_list_progress**](CMSApi.md#cms_list_progress) | **GET** /n0c-api/cms/installations-progress | List installation in progress
[**delete_cms**](CMSApi.md#delete_cms) | **POST** /n0c-api/cms/delete | Delete a CMS installation
[**install_cms**](CMSApi.md#install_cms) | **POST** /n0c-api/cms/install | Installing a CMS

# **cms_list_available**
> InlineResponse20074 cms_list_available(body, x_api_user, x_api_key)

List of CMS available

List the cms available for installation and their versions.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.CMSApi()
body = planethoster.UserTempdomainBody() # UserTempdomainBody | World account settings credentials.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # List of CMS available
    api_response = api_instance.cms_list_available(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CMSApi->cms_list_available: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserTempdomainBody**](UserTempdomainBody.md)| World account settings credentials. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20074**](InlineResponse20074.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cms_list_installed**
> InlineResponse20076 cms_list_installed(body, x_api_user, x_api_key)

List the installed CMS

List the CMS installed on the hosting

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.CMSApi()
body = planethoster.UserTempdomainBody() # UserTempdomainBody | 
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # List the installed CMS
    api_response = api_instance.cms_list_installed(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CMSApi->cms_list_installed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserTempdomainBody**](UserTempdomainBody.md)|  | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20076**](InlineResponse20076.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cms_list_progress**
> InlineResponse20077 cms_list_progress(body, x_api_user, x_api_key)

List installation in progress

List CMS that have recently been installed or are in the process of being installed

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.CMSApi()
body = planethoster.CmsInstallationsprogressBody() # CmsInstallationsprogressBody | 
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # List installation in progress
    api_response = api_instance.cms_list_progress(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CMSApi->cms_list_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CmsInstallationsprogressBody**](CmsInstallationsprogressBody.md)|  | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cms**
> InlineResponse20073 delete_cms(body, x_api_user, x_api_key)

Delete a CMS installation

Delete a CMS installation

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.CMSApi()
body = planethoster.CmsDeleteBody() # CmsDeleteBody | 
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Delete a CMS installation
    api_response = api_instance.delete_cms(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CMSApi->delete_cms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CmsDeleteBody**](CmsDeleteBody.md)|  | 
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

# **install_cms**
> InlineResponse20075 install_cms(body, x_api_user, x_api_key)

Installing a CMS

Start the installation of a CMS

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.CMSApi()
body = planethoster.CmsInstallBody() # CmsInstallBody | World account settings credentials.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Installing a CMS
    api_response = api_instance.install_cms(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CMSApi->install_cms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CmsInstallBody**](CmsInstallBody.md)| World account settings credentials. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

