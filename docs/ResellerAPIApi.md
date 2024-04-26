# planethoster.ResellerAPIApi

All URIs are relative to *https://api.planethoster.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_info**](ResellerAPIApi.md#account_info) | **GET** /reseller-api/account-info | Account info
[**check_availability**](ResellerAPIApi.md#check_availability) | **GET** /reseller-api/check-availability | Check domain availability
[**delete_ph_dns_zone**](ResellerAPIApi.md#delete_ph_dns_zone) | **POST** /reseller-api/delete-ph-dns-zone | Delete zone
[**domain_info**](ResellerAPIApi.md#domain_info) | **GET** /reseller-api/domain-info | Domain information
[**email_epp_code**](ResellerAPIApi.md#email_epp_code) | **POST** /reseller-api/email-epp-code | Email epp code
[**get_contact_details**](ResellerAPIApi.md#get_contact_details) | **GET** /reseller-api/get-contact-details | Contact details
[**get_nameservers**](ResellerAPIApi.md#get_nameservers) | **GET** /reseller-api/get-nameservers | Get nameservers
[**get_ph_dns_records**](ResellerAPIApi.md#get_ph_dns_records) | **GET** /reseller-api/get-ph-dns-records | Get dns records
[**get_registrar_lock**](ResellerAPIApi.md#get_registrar_lock) | **GET** /reseller-api/get-registrar-lock | Get registrar lock
[**register_domain**](ResellerAPIApi.md#register_domain) | **POST** /reseller-api/register-domain | Register domain
[**renew_domain**](ResellerAPIApi.md#renew_domain) | **POST** /reseller-api/renew-domain | Renew domain
[**save_contact_details**](ResellerAPIApi.md#save_contact_details) | **POST** /reseller-api/save-contact-details | Save contact details
[**save_namervers**](ResellerAPIApi.md#save_namervers) | **POST** /reseller-api/save-nameservers | Save nameservers
[**save_ph_dns_records**](ResellerAPIApi.md#save_ph_dns_records) | **POST** /reseller-api/save-ph-dns-records | Save dns records
[**save_registrar_lock**](ResellerAPIApi.md#save_registrar_lock) | **POST** /reseller-api/save-registrar-lock | Save registrar lock
[**test_connection**](ResellerAPIApi.md#test_connection) | **GET** /reseller-api/test-connection | Tests the connection
[**tld_prices**](ResellerAPIApi.md#tld_prices) | **GET** /reseller-api/tld-prices | Tld prices
[**transfer_domain**](ResellerAPIApi.md#transfer_domain) | **POST** /reseller-api/transfert-domain | Transfer domain

# **account_info**
> InlineResponse2001 account_info(x_api_user, x_api_key)

Account info

Return information pertinent to your reseller account.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Account info
    api_response = api_instance.account_info(x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->account_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_availability**
> InlineResponse2003 check_availability(x_api_user, x_api_key, sld, tld)

Check domain availability

Checks whether a domain name is available to register or not.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
sld = NULL # object | Domain name without the Top-Level Domain (TLD).
tld = NULL # object | TLD without the leading period.

try:
    # Check domain availability
    api_response = api_instance.check_availability(x_api_user, x_api_key, sld, tld)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->check_availability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **sld** | [**object**](.md)| Domain name without the Top-Level Domain (TLD). | 
 **tld** | [**object**](.md)| TLD without the leading period. | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ph_dns_zone**
> InlineResponse20013 delete_ph_dns_zone(body, x_api_user, x_api_key)

Delete zone

Deletes the DNS zone on the PlanetHoster DNS servers for the given domain.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
body = planethoster.ResellerapiDeletephdnszoneBody() # ResellerapiDeletephdnszoneBody | Delete zone parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Delete zone
    api_response = api_instance.delete_ph_dns_zone(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->delete_ph_dns_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResellerapiDeletephdnszoneBody**](ResellerapiDeletephdnszoneBody.md)| Delete zone parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_info**
> InlineResponse2004 domain_info(x_api_user, x_api_key, sld, tld)

Domain information

Retrieve information for a domain you successfully registered or for which you created a transfer order.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
sld = NULL # object | Domain name without the Top-Level Domain (TLD).
tld = NULL # object | TLD without the leading period.

try:
    # Domain information
    api_response = api_instance.domain_info(x_api_user, x_api_key, sld, tld)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->domain_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **sld** | [**object**](.md)| Domain name without the Top-Level Domain (TLD). | 
 **tld** | [**object**](.md)| TLD without the leading period. | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_epp_code**
> InlineResponse20014 email_epp_code(body, x_api_user, x_api_key)

Email epp code

Email to the domain name registrant the EPP code (also called Auth Info) for the given domain.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
body = planethoster.ResellerapiDeletephdnszoneBody() # ResellerapiDeletephdnszoneBody | EPP code request parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Email epp code
    api_response = api_instance.email_epp_code(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->email_epp_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResellerapiDeletephdnszoneBody**](ResellerapiDeletephdnszoneBody.md)| EPP code request parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_details**
> InlineResponse2005 get_contact_details(x_api_user, x_api_key, sld, tld)

Contact details

Returns the contact information (WHOIS information) for the active domain name.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
sld = NULL # object | Domain name without the Top-Level Domain (TLD).
tld = NULL # object | TLD without the leading period.

try:
    # Contact details
    api_response = api_instance.get_contact_details(x_api_user, x_api_key, sld, tld)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->get_contact_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **sld** | [**object**](.md)| Domain name without the Top-Level Domain (TLD). | 
 **tld** | [**object**](.md)| TLD without the leading period. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nameservers**
> InlineResponse2009 get_nameservers(x_api_user, x_api_key, sld, tld)

Get nameservers

Returns the nameservers for a registered domain name.   *There must be at least two existing nameservers associated with a domain name.* 

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
sld = NULL # object | Domain name without the Top-Level Domain (TLD).
tld = NULL # object | TLD without the leading period.

try:
    # Get nameservers
    api_response = api_instance.get_nameservers(x_api_user, x_api_key, sld, tld)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->get_nameservers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **sld** | [**object**](.md)| Domain name without the Top-Level Domain (TLD). | 
 **tld** | [**object**](.md)| TLD without the leading period. | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ph_dns_records**
> InlineResponse20011 get_ph_dns_records(x_api_user, x_api_key, sld, tld)

Get dns records

Retrieves the DNS records for the active domain name registered with PlanetHoster that has at least one PlanetHoster nameserver.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
sld = NULL # object | Domain name without the Top-Level Domain (TLD).
tld = NULL # object | TLD without the leading period.

try:
    # Get dns records
    api_response = api_instance.get_ph_dns_records(x_api_user, x_api_key, sld, tld)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->get_ph_dns_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **sld** | [**object**](.md)| Domain name without the Top-Level Domain (TLD). | 
 **tld** | [**object**](.md)| TLD without the leading period. | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registrar_lock**
> InlineResponse2007 get_registrar_lock(x_api_user, x_api_key, sld, tld)

Get registrar lock

Get the lock status of a registered domain name.   *If a domain is locked, it means that it cannot be transferred.*   See [/save-registrar-lock](#operation/saveRegistrarLock) for more info. 

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
sld = NULL # object | Domain name without the Top-Level Domain (TLD).
tld = NULL # object | TLD without the leading period.

try:
    # Get registrar lock
    api_response = api_instance.get_registrar_lock(x_api_user, x_api_key, sld, tld)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->get_registrar_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **sld** | [**object**](.md)| Domain name without the Top-Level Domain (TLD). | 
 **tld** | [**object**](.md)| TLD without the leading period. | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_domain**
> InlineResponse20015 register_domain(body, x_api_user, x_api_key, x_api_sandbox=x_api_sandbox)

Register domain

Attempts to register a domain name for 1 to 10 years.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
body = planethoster.ResellerapiRegisterdomainBody() # ResellerapiRegisterdomainBody | Register parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.
x_api_sandbox = NULL # object | Sandbox Environments set 1 to activate. (optional)

try:
    # Register domain
    api_response = api_instance.register_domain(body, x_api_user, x_api_key, x_api_sandbox=x_api_sandbox)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->register_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResellerapiRegisterdomainBody**](ResellerapiRegisterdomainBody.md)| Register parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 
 **x_api_sandbox** | [**object**](.md)| Sandbox Environments set 1 to activate. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_domain**
> InlineResponse20016 renew_domain(body, x_api_user, x_api_key)

Renew domain

Renew an already active domain name for 1-10 years.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
body = planethoster.ResellerapiRenewdomainBody() # ResellerapiRenewdomainBody | Renewal parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Renew domain
    api_response = api_instance.renew_domain(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->renew_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResellerapiRenewdomainBody**](ResellerapiRenewdomainBody.md)| Renewal parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_contact_details**
> InlineResponse2006 save_contact_details(body, x_api_user, x_api_key)

Save contact details

Saves the contact information (WHOIS information) for the given active domain name.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
body = planethoster.ResellerapiSavecontactdetailsBody() # ResellerapiSavecontactdetailsBody | Contact parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Save contact details
    api_response = api_instance.save_contact_details(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->save_contact_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResellerapiSavecontactdetailsBody**](ResellerapiSavecontactdetailsBody.md)| Contact parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_namervers**
> InlineResponse20010 save_namervers(body, x_api_user, x_api_key)

Save nameservers

Update the nameservers associated with your domain.   *The nameservers must exist and be valid nameservers.* 

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
body = planethoster.ResellerapiSavenameserversBody() # ResellerapiSavenameserversBody | Nameservers parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Save nameservers
    api_response = api_instance.save_namervers(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->save_namervers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResellerapiSavenameserversBody**](ResellerapiSavenameserversBody.md)| Nameservers parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_ph_dns_records**
> InlineResponse20012 save_ph_dns_records(body, x_api_user, x_api_key)

Save dns records

Saves the DNS records for the active domain name registered with PlanetHoster that has at least one PlanetHoster nameserver.   If the DNS zone does not yet exist on PlanetHoster nameservers, it is created.  **Note that this call only work for domain that use PlanetHoster DNS. nsa.n0c.com, nsb.n0c.com, nsc.n0c.com** 

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
body = planethoster.ResellerapiSavephdnsrecordsBody() # ResellerapiSavephdnsrecordsBody | Records parameters.  
**You can add more records by incrementing the number at the end of the parameters key.**

x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Save dns records
    api_response = api_instance.save_ph_dns_records(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->save_ph_dns_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResellerapiSavephdnsrecordsBody**](ResellerapiSavephdnsrecordsBody.md)| Records parameters.  
**You can add more records by incrementing the number at the end of the parameters key.**
 | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_registrar_lock**
> InlineResponse2008 save_registrar_lock(body, x_api_user, x_api_key)

Save registrar lock

Lock or unlock a registered and active domain name. 

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
body = planethoster.ResellerapiSaveregistrarlockBody() # ResellerapiSaveregistrarlockBody | Nameservers parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Save registrar lock
    api_response = api_instance.save_registrar_lock(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->save_registrar_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResellerapiSaveregistrarlockBody**](ResellerapiSaveregistrarlockBody.md)| Nameservers parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_connection**
> InlineResponse200 test_connection(x_api_user, x_api_key)

Tests the connection

Tests the connection to the domain reseller API.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Tests the connection
    api_response = api_instance.test_connection(x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->test_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tld_prices**
> InlineResponse2002 tld_prices(x_api_user, x_api_key)

Tld prices

Returns domain name prices for registration, renewal and transfer. It also returns whether or not each TLD sold by PlanetHoster supports WHOIS ID protection, and whether it requires an EPP code for domain transfer or not.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Tld prices
    api_response = api_instance.tld_prices(x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->tld_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_domain**
> InlineResponse20017 transfer_domain(body, x_api_user, x_api_key)

Transfer domain

Transfer a domain name from your current registrar to PlanetHoster.

### Example
```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.ResellerAPIApi()
body = planethoster.ResellerapiTransfertdomainBody() # ResellerapiTransfertdomainBody | Transfer parameters.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Transfer domain
    api_response = api_instance.transfer_domain(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResellerAPIApi->transfer_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResellerapiTransfertdomainBody**](ResellerapiTransfertdomainBody.md)| Transfer parameters. | 
 **x_api_user** | [**object**](.md)| API user provided in the client area. | 
 **x_api_key** | [**object**](.md)| API key provided in the client area. | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

