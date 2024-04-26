# planethoster.DomainApi

All URIs are relative to *https://api.planethoster.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**n0c_add_domain**](DomainApi.md#n0c_add_domain) | **POST** /n0c-api/domain/add | Add
[**n0c_add_sub_domain**](DomainApi.md#n0c_add_sub_domain) | **POST** /n0c-api/domain/add-sub-domain | Add sub-domain
[**n0c_change_doc_root**](DomainApi.md#n0c_change_doc_root) | **POST** /n0c-api/domain/change-doc-root | Change doc-root
[**n0c_delete_redirection**](DomainApi.md#n0c_delete_redirection) | **POST** /n0c-api/domain/delete-redirection | Delete redirection
[**n0c_domain_waf_logs**](DomainApi.md#n0c_domain_waf_logs) | **GET** /n0c-api/domain/waf-logs | WAF logs
[**n0c_domain_waf_rules**](DomainApi.md#n0c_domain_waf_rules) | **GET** /n0c-api/domain/waf-rules | WAF rules
[**n0c_domains**](DomainApi.md#n0c_domains) | **GET** /n0c-api/domains | Domains
[**n0c_redirections**](DomainApi.md#n0c_redirections) | **GET** /n0c-api/domain/redirections | Redirections
[**n0c_remove_domain**](DomainApi.md#n0c_remove_domain) | **POST** /n0c-api/domain/remove | Remove
[**n0c_set_external_redirection**](DomainApi.md#n0c_set_external_redirection) | **POST** /n0c-api/domain/external-redirection | External redirection
[**n0c_set_rediction**](DomainApi.md#n0c_set_rediction) | **POST** /n0c-api/domain/redirection | Internal redirection
[**n0c_suspend_domain**](DomainApi.md#n0c_suspend_domain) | **POST** /n0c-api/domain/suspend | Suspend domains
[**n0c_unsuspend_domain**](DomainApi.md#n0c_unsuspend_domain) | **POST** /n0c-api/domain/unsuspend | Unsuspend domains
[**n0c_update_waf_rules**](DomainApi.md#n0c_update_waf_rules) | **POST** /n0c-api/domain/update-waf-rules | Update waf rules

# **n0c_add_domain**
> InlineResponse20033 n0c_add_domain(body, x_api_user, x_api_key)

Add

Add a domain to the World account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DomainApi()
body = planethoster.DomainAddBody() # DomainAddBody | Add domain parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Add
    api_response = api_instance.n0c_add_domain(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->n0c_add_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainAddBody**](DomainAddBody.md)| Add domain parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_add_sub_domain**
> InlineResponse20035 n0c_add_sub_domain(body, x_api_user, x_api_key)

Add sub-domain

Add a sub-domain to the World account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DomainApi()
body = planethoster.DomainAddsubdomainBody() # DomainAddsubdomainBody | Add sub-domain parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Add sub-domain
    api_response = api_instance.n0c_add_sub_domain(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->n0c_add_sub_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainAddsubdomainBody**](DomainAddsubdomainBody.md)| Add sub-domain parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_change_doc_root**
> InlineResponse20035 n0c_change_doc_root(body, x_api_user, x_api_key)

Change doc-root

Unsuspend one or multiple domains.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DomainApi()
body = planethoster.DomainChangedocrootBody() # DomainChangedocrootBody | Unsuspend domains parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Change doc-root
    api_response = api_instance.n0c_change_doc_root(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->n0c_change_doc_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainChangedocrootBody**](DomainChangedocrootBody.md)| Unsuspend domains parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_delete_redirection**
> InlineResponse20040 n0c_delete_redirection(x_api_user, x_api_key, body=body)

Delete redirection

Delete redirection for a domain.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DomainApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
body = planethoster.DomainRemoveBody() # DomainRemoveBody | Delete redirection parameters. (optional)

try:
    # Delete redirection
    api_response = api_instance.n0c_delete_redirection(x_api_user, x_api_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->n0c_delete_redirection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **body** | [**DomainRemoveBody**](DomainRemoveBody.md)| Delete redirection parameters. | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_domain_waf_logs**
> InlineResponse20041 n0c_domain_waf_logs(body, x_api_user, x_api_key)

WAF logs

Get domain WAF logs. What is a [Web App Firewall](https://kb.n0c.com/en/knowledge-base/activating-and-deactivating-the-waf-with-n0c/)? 

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DomainApi()
body = planethoster.DomainRemoveBody() # DomainRemoveBody | Get WAF logs parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # WAF logs
    api_response = api_instance.n0c_domain_waf_logs(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->n0c_domain_waf_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRemoveBody**](DomainRemoveBody.md)| Get WAF logs parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_domain_waf_rules**
> InlineResponse20042 n0c_domain_waf_rules(body, x_api_user, x_api_key)

WAF rules

Get the domain WAF rules.   What is a [Web App Firewall](https://kb.n0c.com/en/knowledge-base/activating-and-deactivating-the-waf-with-n0c/)? 

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DomainApi()
body = planethoster.DomainRemoveBody() # DomainRemoveBody | Get WAF rules parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # WAF rules
    api_response = api_instance.n0c_domain_waf_rules(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->n0c_domain_waf_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRemoveBody**](DomainRemoveBody.md)| Get WAF rules parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_domains**
> InlineResponse20032 n0c_domains(body, x_api_user, x_api_key)

Domains

Get all domains of the account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DomainApi()
body = planethoster.UserTempdomainBody() # UserTempdomainBody | World account ID parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Domains
    api_response = api_instance.n0c_domains(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->n0c_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserTempdomainBody**](UserTempdomainBody.md)| World account ID parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_redirections**
> InlineResponse20038 n0c_redirections(body, x_api_user, x_api_key)

Redirections

Get domain redirections.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DomainApi()
body = planethoster.DomainRedirectionsBody() # DomainRedirectionsBody | World account ID parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Redirections
    api_response = api_instance.n0c_redirections(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->n0c_redirections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRedirectionsBody**](DomainRedirectionsBody.md)| World account ID parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_remove_domain**
> InlineResponse20034 n0c_remove_domain(x_api_user, x_api_key, body=body)

Remove

Remove the domain from the World account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DomainApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
body = planethoster.DomainRemoveBody() # DomainRemoveBody | Remove domain parameters. (optional)

try:
    # Remove
    api_response = api_instance.n0c_remove_domain(x_api_user, x_api_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->n0c_remove_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **body** | [**DomainRemoveBody**](DomainRemoveBody.md)| Remove domain parameters. | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_set_external_redirection**
> InlineResponse20039 n0c_set_external_redirection(body, x_api_user, x_api_key)

External redirection

Redirection that will force HTTPS or www, for example.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DomainApi()
body = planethoster.DomainExternalredirectionBody() # DomainExternalredirectionBody | External redirection parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # External redirection
    api_response = api_instance.n0c_set_external_redirection(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->n0c_set_external_redirection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainExternalredirectionBody**](DomainExternalredirectionBody.md)| External redirection parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_set_rediction**
> InlineResponse20039 n0c_set_rediction(body, x_api_user, x_api_key)

Internal redirection

Redirection that will force HTTPS or www, for example.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DomainApi()
body = planethoster.DomainRedirectionBody() # DomainRedirectionBody | Internal redirection parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Internal redirection
    api_response = api_instance.n0c_set_rediction(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->n0c_set_rediction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainRedirectionBody**](DomainRedirectionBody.md)| Internal redirection parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_suspend_domain**
> InlineResponse20036 n0c_suspend_domain(body, x_api_user, x_api_key)

Suspend domains

Suspend one or multiple domains.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DomainApi()
body = planethoster.DomainSuspendBody() # DomainSuspendBody | Suspend domains parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Suspend domains
    api_response = api_instance.n0c_suspend_domain(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->n0c_suspend_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainSuspendBody**](DomainSuspendBody.md)| Suspend domains parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_unsuspend_domain**
> InlineResponse20037 n0c_unsuspend_domain(body, x_api_user, x_api_key)

Unsuspend domains

Unsuspend one or multiple domains.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DomainApi()
body = planethoster.DomainUnsuspendBody() # DomainUnsuspendBody | Unsuspend domains parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Unsuspend domains
    api_response = api_instance.n0c_unsuspend_domain(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->n0c_unsuspend_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainUnsuspendBody**](DomainUnsuspendBody.md)| Unsuspend domains parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **n0c_update_waf_rules**
> InlineResponse20043 n0c_update_waf_rules(body, x_api_user, x_api_key)

Update waf rules

Update WAF rules for the domain.   What is a [Web App Firewall](https://kb.n0c.com/en/knowledge-base/activating-and-deactivating-the-waf-with-n0c/)? 

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.DomainApi()
body = planethoster.DomainUpdatewafrulesBody() # DomainUpdatewafrulesBody | Get WAF rules parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Update waf rules
    api_response = api_instance.n0c_update_waf_rules(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->n0c_update_waf_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainUpdatewafrulesBody**](DomainUpdatewafrulesBody.md)| Get WAF rules parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

