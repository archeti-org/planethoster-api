# planethoster
| <a href=\"https://apidoc.planethoster.com/fr\">Version Française</a> ## Description The PlanetHoster API allows actions related to domain management and web hosting. ## Details - SSL only: we require that all requests be done over encrypted TLS/SSL connections. - Supported HTTP verbs are GET and POST. If your client does not support all HTTP verbs, you can override the verb with X-Http-Method-Override HTTP header. - Unless otherwise specified in the method documentation, all successful API calls return an **HTTP code 200** with a JSON object. - Errors are returned with an HTTP code 4XX or 5XX, a JSON object with properties \"error\" (an error message) and an \"error_code\" (optional, an integer). - Every string passed to and from the API needs to be UTF-8 encoded. - The API sends ETag headers and supports the If-None-Match header. - Unless otherwise specified, all API methods require authentication with api_user and api_key.  ## Authentication and whitelist 1. In order to be able to contact the API, you must whitelist your IPs. 2. API user and API key are required in the HTTP header.  Whitelisted IP and credentials can be found in the <a href=\"https://my.planethoster.com/domain-reseller\" target=\"_blank\">PlanetHoster Client Area / Reseller section</a>.  <SecurityDefinitions /> 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import planethoster 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import planethoster
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import planethoster
from planethoster.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = planethoster.CMSApi(planethoster.ApiClient(configuration))
body = planethoster.UserTempdomainBody() # UserTempdomainBody | World account settings credentials.
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # List of CMS available
    api_response = api_instance.cms_list_available(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CMSApi->cms_list_available: %s\n" % e)

# create an instance of the API class
api_instance = planethoster.CMSApi(planethoster.ApiClient(configuration))
body = planethoster.UserTempdomainBody() # UserTempdomainBody | 
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # List the installed CMS
    api_response = api_instance.cms_list_installed(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CMSApi->cms_list_installed: %s\n" % e)

# create an instance of the API class
api_instance = planethoster.CMSApi(planethoster.ApiClient(configuration))
body = planethoster.CmsInstallationsprogressBody() # CmsInstallationsprogressBody | 
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # List installation in progress
    api_response = api_instance.cms_list_progress(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CMSApi->cms_list_progress: %s\n" % e)

# create an instance of the API class
api_instance = planethoster.CMSApi(planethoster.ApiClient(configuration))
body = planethoster.CmsDeleteBody() # CmsDeleteBody | 
x_api_user = NULL # object | API user provided in the client area.
x_api_key = NULL # object | API key provided in the client area.

try:
    # Delete a CMS installation
    api_response = api_instance.delete_cms(body, x_api_user, x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CMSApi->delete_cms: %s\n" % e)

# create an instance of the API class
api_instance = planethoster.CMSApi(planethoster.ApiClient(configuration))
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

## Documentation for API Endpoints

All URIs are relative to *https://api.planethoster.net*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CMSApi* | [**cms_list_available**](docs/CMSApi.md#cms_list_available) | **GET** /n0c-api/cms/list-available | List of CMS available
*CMSApi* | [**cms_list_installed**](docs/CMSApi.md#cms_list_installed) | **GET** /n0c-api/cms/list-installed | List the installed CMS
*CMSApi* | [**cms_list_progress**](docs/CMSApi.md#cms_list_progress) | **GET** /n0c-api/cms/installations-progress | List installation in progress
*CMSApi* | [**delete_cms**](docs/CMSApi.md#delete_cms) | **POST** /n0c-api/cms/delete | Delete a CMS installation
*CMSApi* | [**install_cms**](docs/CMSApi.md#install_cms) | **POST** /n0c-api/cms/install | Installing a CMS
*CronApi* | [**n0c_add_cron**](docs/CronApi.md#n0c_add_cron) | **POST** /n0c-api/cron/add | Add
*CronApi* | [**n0c_add_cron_email**](docs/CronApi.md#n0c_add_cron_email) | **POST** /n0c-api/cron/email/set | Set email
*CronApi* | [**n0c_get_cron**](docs/CronApi.md#n0c_get_cron) | **GET** /n0c-api/crons | Crons
*CronApi* | [**n0c_remove_cron**](docs/CronApi.md#n0c_remove_cron) | **POST** /n0c-api/cron/remove | Remove
*CronApi* | [**n0c_remove_cron_email**](docs/CronApi.md#n0c_remove_cron_email) | **POST** /n0c-api/cron/email/remove | Remove email
*DNSApi* | [**n0c_domain_edit_zone**](docs/DNSApi.md#n0c_domain_edit_zone) | **POST** /n0c-api/dns/edit-zone | Edit / add zone records
*DNSApi* | [**n0c_domain_reset_zone**](docs/DNSApi.md#n0c_domain_reset_zone) | **POST** /n0c-api/dns/reset-zone | Zone create / reset to default value
*DNSApi* | [**n0cdomain_get_zone**](docs/DNSApi.md#n0cdomain_get_zone) | **GET** /n0c-api/dns/get-records | Get DNS zone
*DatabaseApi* | [**n0c_create_database**](docs/DatabaseApi.md#n0c_create_database) | **POST** /n0c-api/database/add | Add
*DatabaseApi* | [**n0c_create_database_user**](docs/DatabaseApi.md#n0c_create_database_user) | **POST** /n0c-api/database/user/add | Add user
*DatabaseApi* | [**n0c_database_grant_permission**](docs/DatabaseApi.md#n0c_database_grant_permission) | **POST** /n0c-api/database/user/grant-access | Grant permission
*DatabaseApi* | [**n0c_database_remove_permission**](docs/DatabaseApi.md#n0c_database_remove_permission) | **POST** /n0c-api/database/user/remove-access | Remove permission
*DatabaseApi* | [**n0c_remove_database**](docs/DatabaseApi.md#n0c_remove_database) | **POST** /n0c-api/database/remove | Remove
*DatabaseApi* | [**n0c_remove_database_user**](docs/DatabaseApi.md#n0c_remove_database_user) | **POST** /n0c-api/database/user/remove | Remove user
*DatabaseApi* | [**n0c_users**](docs/DatabaseApi.md#n0c_users) | **GET** /n0c-api/database/users | Users
*DatabaseApi* | [**noc_databases**](docs/DatabaseApi.md#noc_databases) | **GET** /n0c-api/databases | Databases
*DomainApi* | [**n0c_add_domain**](docs/DomainApi.md#n0c_add_domain) | **POST** /n0c-api/domain/add | Add
*DomainApi* | [**n0c_add_sub_domain**](docs/DomainApi.md#n0c_add_sub_domain) | **POST** /n0c-api/domain/add-sub-domain | Add sub-domain
*DomainApi* | [**n0c_change_doc_root**](docs/DomainApi.md#n0c_change_doc_root) | **POST** /n0c-api/domain/change-doc-root | Change doc-root
*DomainApi* | [**n0c_delete_redirection**](docs/DomainApi.md#n0c_delete_redirection) | **POST** /n0c-api/domain/delete-redirection | Delete redirection
*DomainApi* | [**n0c_domain_waf_logs**](docs/DomainApi.md#n0c_domain_waf_logs) | **GET** /n0c-api/domain/waf-logs | WAF logs
*DomainApi* | [**n0c_domain_waf_rules**](docs/DomainApi.md#n0c_domain_waf_rules) | **GET** /n0c-api/domain/waf-rules | WAF rules
*DomainApi* | [**n0c_domains**](docs/DomainApi.md#n0c_domains) | **GET** /n0c-api/domains | Domains
*DomainApi* | [**n0c_redirections**](docs/DomainApi.md#n0c_redirections) | **GET** /n0c-api/domain/redirections | Redirections
*DomainApi* | [**n0c_remove_domain**](docs/DomainApi.md#n0c_remove_domain) | **POST** /n0c-api/domain/remove | Remove
*DomainApi* | [**n0c_set_external_redirection**](docs/DomainApi.md#n0c_set_external_redirection) | **POST** /n0c-api/domain/external-redirection | External redirection
*DomainApi* | [**n0c_set_rediction**](docs/DomainApi.md#n0c_set_rediction) | **POST** /n0c-api/domain/redirection | Internal redirection
*DomainApi* | [**n0c_suspend_domain**](docs/DomainApi.md#n0c_suspend_domain) | **POST** /n0c-api/domain/suspend | Suspend domains
*DomainApi* | [**n0c_unsuspend_domain**](docs/DomainApi.md#n0c_unsuspend_domain) | **POST** /n0c-api/domain/unsuspend | Unsuspend domains
*DomainApi* | [**n0c_update_waf_rules**](docs/DomainApi.md#n0c_update_waf_rules) | **POST** /n0c-api/domain/update-waf-rules | Update waf rules
*EmailApi* | [**n0c_add_email**](docs/EmailApi.md#n0c_add_email) | **POST** /n0c-api/email/add | Add
*EmailApi* | [**n0c_disable_auth**](docs/EmailApi.md#n0c_disable_auth) | **POST** /n0c-api/email/auth/disable | Disable Authentication
*EmailApi* | [**n0c_email_auth**](docs/EmailApi.md#n0c_email_auth) | **GET** /n0c-api/email/auths | Authentication
*EmailApi* | [**n0c_email_change_password**](docs/EmailApi.md#n0c_email_change_password) | **POST** /n0c-api/email/change-password | Change password
*EmailApi* | [**n0c_email_change_quota**](docs/EmailApi.md#n0c_email_change_quota) | **POST** /n0c-api/email/change-quota | Change quota
*EmailApi* | [**n0c_emails**](docs/EmailApi.md#n0c_emails) | **GET** /n0c-api/emails | Emails
*EmailApi* | [**n0c_enable_auth**](docs/EmailApi.md#n0c_enable_auth) | **POST** /n0c-api/email/auth/enable | Enable Authentication
*EmailApi* | [**n0c_remove_email**](docs/EmailApi.md#n0c_remove_email) | **POST** /n0c-api/email/remove | Remove
*EmailApi* | [**n0c_suspend_emails**](docs/EmailApi.md#n0c_suspend_emails) | **POST** /n0c-api/email/suspend | Suspend emails
*EmailApi* | [**n0c_unsuspend_emails**](docs/EmailApi.md#n0c_unsuspend_emails) | **POST** /n0c-api/email/unsuspend | Unsuspend emails
*FTPApi* | [**n0c_change_ftp_password**](docs/FTPApi.md#n0c_change_ftp_password) | **POST** /n0c-api/ftp-account/password | Change password
*FTPApi* | [**n0c_create_ftp**](docs/FTPApi.md#n0c_create_ftp) | **POST** /n0c-api/ftp-account/add | Add
*FTPApi* | [**n0c_ftp_update_path**](docs/FTPApi.md#n0c_ftp_update_path) | **POST** /n0c-api/ftp-account/update-path | Update path
*FTPApi* | [**n0c_get_ftp**](docs/FTPApi.md#n0c_get_ftp) | **GET** /n0c-api/ftp-accounts | FTP accounts
*FTPApi* | [**n0c_list_ftp_connections**](docs/FTPApi.md#n0c_list_ftp_connections) | **GET** /n0c-api/ftp-account/active-connection | List connections
*FTPApi* | [**n0c_remove_ftp**](docs/FTPApi.md#n0c_remove_ftp) | **POST** /n0c-api/ftp-account/remove | Remove
*ResellerAPIApi* | [**account_info**](docs/ResellerAPIApi.md#account_info) | **GET** /reseller-api/account-info | Account info
*ResellerAPIApi* | [**check_availability**](docs/ResellerAPIApi.md#check_availability) | **GET** /reseller-api/check-availability | Check domain availability
*ResellerAPIApi* | [**delete_ph_dns_zone**](docs/ResellerAPIApi.md#delete_ph_dns_zone) | **POST** /reseller-api/delete-ph-dns-zone | Delete zone
*ResellerAPIApi* | [**domain_info**](docs/ResellerAPIApi.md#domain_info) | **GET** /reseller-api/domain-info | Domain information
*ResellerAPIApi* | [**email_epp_code**](docs/ResellerAPIApi.md#email_epp_code) | **POST** /reseller-api/email-epp-code | Email epp code
*ResellerAPIApi* | [**get_contact_details**](docs/ResellerAPIApi.md#get_contact_details) | **GET** /reseller-api/get-contact-details | Contact details
*ResellerAPIApi* | [**get_nameservers**](docs/ResellerAPIApi.md#get_nameservers) | **GET** /reseller-api/get-nameservers | Get nameservers
*ResellerAPIApi* | [**get_ph_dns_records**](docs/ResellerAPIApi.md#get_ph_dns_records) | **GET** /reseller-api/get-ph-dns-records | Get dns records
*ResellerAPIApi* | [**get_registrar_lock**](docs/ResellerAPIApi.md#get_registrar_lock) | **GET** /reseller-api/get-registrar-lock | Get registrar lock
*ResellerAPIApi* | [**register_domain**](docs/ResellerAPIApi.md#register_domain) | **POST** /reseller-api/register-domain | Register domain
*ResellerAPIApi* | [**renew_domain**](docs/ResellerAPIApi.md#renew_domain) | **POST** /reseller-api/renew-domain | Renew domain
*ResellerAPIApi* | [**save_contact_details**](docs/ResellerAPIApi.md#save_contact_details) | **POST** /reseller-api/save-contact-details | Save contact details
*ResellerAPIApi* | [**save_namervers**](docs/ResellerAPIApi.md#save_namervers) | **POST** /reseller-api/save-nameservers | Save nameservers
*ResellerAPIApi* | [**save_ph_dns_records**](docs/ResellerAPIApi.md#save_ph_dns_records) | **POST** /reseller-api/save-ph-dns-records | Save dns records
*ResellerAPIApi* | [**save_registrar_lock**](docs/ResellerAPIApi.md#save_registrar_lock) | **POST** /reseller-api/save-registrar-lock | Save registrar lock
*ResellerAPIApi* | [**test_connection**](docs/ResellerAPIApi.md#test_connection) | **GET** /reseller-api/test-connection | Tests the connection
*ResellerAPIApi* | [**tld_prices**](docs/ResellerAPIApi.md#tld_prices) | **GET** /reseller-api/tld-prices | Tld prices
*ResellerAPIApi* | [**transfer_domain**](docs/ResellerAPIApi.md#transfer_domain) | **POST** /reseller-api/transfert-domain | Transfer domain
*StatsApi* | [**n0c_apache_stats**](docs/StatsApi.md#n0c_apache_stats) | **POST** /n0c-api/stats/apache | Stats apache
*StatsApi* | [**n0c_apache_unique_stats**](docs/StatsApi.md#n0c_apache_unique_stats) | **POST** /n0c-api/stats/apache/unique | Stats apache (Unique Visitor)
*StatsApi* | [**n0c_disk_usage**](docs/StatsApi.md#n0c_disk_usage) | **GET** /n0c-api/stats/disk-usage | Disk usage
*StatsApi* | [**n0c_stats_performance**](docs/StatsApi.md#n0c_stats_performance) | **POST** /n0c-api/stats/performance | Performance
*UserApi* | [**disable_n0c_temp_domain**](docs/UserApi.md#disable_n0c_temp_domain) | **POST** /n0c-api/user/disable-temp-domain | Disable temporary domain
*UserApi* | [**n0c_add_ssh_key**](docs/UserApi.md#n0c_add_ssh_key) | **POST** /n0c-api/user/add-ssh-key | Add SSH key
*UserApi* | [**n0c_edit_ssh_key**](docs/UserApi.md#n0c_edit_ssh_key) | **POST** /n0c-api/user/edit-ssh-key | Edit SSH key
*UserApi* | [**n0c_remove_ssh_key**](docs/UserApi.md#n0c_remove_ssh_key) | **POST** /n0c-api/user/remove-ssh-key | Remove SSH key
*UserApi* | [**n0c_ssh_keys**](docs/UserApi.md#n0c_ssh_keys) | **GET** /n0c-api/user/ssh-keys | SSH keys
*UserApi* | [**n0c_temp_domain**](docs/UserApi.md#n0c_temp_domain) | **POST** /n0c-api/user/temp-domain | Temporary domain
*WordpressApi* | [**n0c_get_wp**](docs/WordpressApi.md#n0c_get_wp) | **GET** /n0c-api/wordpress | Get installed wordpress
*WordpressApi* | [**n0c_wp_install**](docs/WordpressApi.md#n0c_wp_install) | **POST** /n0c-api/wordpress/add | Wordpress installation
*WordpressApi* | [**n0c_wp_remove**](docs/WordpressApi.md#n0c_wp_remove) | **POST** /n0c-api/wordpress/remove | Delete wordpress installation
*WorldAPIApi* | [**create_account**](docs/WorldAPIApi.md#create_account) | **POST** /world-api/create-account | Create account
*WorldAPIApi* | [**get_accounts**](docs/WorldAPIApi.md#get_accounts) | **GET** /world-api/get-accounts | Get accounts
*WorldAPIApi* | [**modify_resources**](docs/WorldAPIApi.md#modify_resources) | **POST** /world-api/modify-resources | Modify resources
*WorldAPIApi* | [**suspend_acccount**](docs/WorldAPIApi.md#suspend_acccount) | **POST** /world-api/suspend-account | Suspend account
*WorldAPIApi* | [**unsuspend_account**](docs/WorldAPIApi.md#unsuspend_account) | **POST** /world-api/unsuspend-account | Unsuspend account

## Documentation For Models

 - [ApacheUniqueBody](docs/ApacheUniqueBody.md)
 - [AuthDisableBody](docs/AuthDisableBody.md)
 - [AuthEnableBody](docs/AuthEnableBody.md)
 - [CmsDeleteBody](docs/CmsDeleteBody.md)
 - [CmsInstallBody](docs/CmsInstallBody.md)
 - [CmsInstallationsprogressBody](docs/CmsInstallationsprogressBody.md)
 - [CronAddBody](docs/CronAddBody.md)
 - [CronRemoveBody](docs/CronRemoveBody.md)
 - [DatabaseAddBody](docs/DatabaseAddBody.md)
 - [DnsEditzoneBody](docs/DnsEditzoneBody.md)
 - [DnsGetrecordsBody](docs/DnsGetrecordsBody.md)
 - [DomainAddBody](docs/DomainAddBody.md)
 - [DomainAddsubdomainBody](docs/DomainAddsubdomainBody.md)
 - [DomainChangedocrootBody](docs/DomainChangedocrootBody.md)
 - [DomainExternalredirectionBody](docs/DomainExternalredirectionBody.md)
 - [DomainRedirectionBody](docs/DomainRedirectionBody.md)
 - [DomainRedirectionsBody](docs/DomainRedirectionsBody.md)
 - [DomainRemoveBody](docs/DomainRemoveBody.md)
 - [DomainSuspendBody](docs/DomainSuspendBody.md)
 - [DomainUnsuspendBody](docs/DomainUnsuspendBody.md)
 - [DomainUpdatewafrulesBody](docs/DomainUpdatewafrulesBody.md)
 - [EmailAddBody](docs/EmailAddBody.md)
 - [EmailChangepasswordBody](docs/EmailChangepasswordBody.md)
 - [EmailChangequotaBody](docs/EmailChangequotaBody.md)
 - [EmailRemoveBody](docs/EmailRemoveBody.md)
 - [EmailSetBody](docs/EmailSetBody.md)
 - [EmailSuspendBody](docs/EmailSuspendBody.md)
 - [EmailUnsuspendBody](docs/EmailUnsuspendBody.md)
 - [FtpaccountAddBody](docs/FtpaccountAddBody.md)
 - [FtpaccountPasswordBody](docs/FtpaccountPasswordBody.md)
 - [FtpaccountRemoveBody](docs/FtpaccountRemoveBody.md)
 - [FtpaccountUpdatepathBody](docs/FtpaccountUpdatepathBody.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse20019](docs/InlineResponse20019.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse20020](docs/InlineResponse20020.md)
 - [InlineResponse20021](docs/InlineResponse20021.md)
 - [InlineResponse20021TotalAvailableResources](docs/InlineResponse20021TotalAvailableResources.md)
 - [InlineResponse20022](docs/InlineResponse20022.md)
 - [InlineResponse20023](docs/InlineResponse20023.md)
 - [InlineResponse20024](docs/InlineResponse20024.md)
 - [InlineResponse20025](docs/InlineResponse20025.md)
 - [InlineResponse20026](docs/InlineResponse20026.md)
 - [InlineResponse20027](docs/InlineResponse20027.md)
 - [InlineResponse20027Data](docs/InlineResponse20027Data.md)
 - [InlineResponse20028](docs/InlineResponse20028.md)
 - [InlineResponse20028Data](docs/InlineResponse20028Data.md)
 - [InlineResponse20029](docs/InlineResponse20029.md)
 - [InlineResponse20029Data](docs/InlineResponse20029Data.md)
 - [InlineResponse2002Tlds](docs/InlineResponse2002Tlds.md)
 - [InlineResponse2002TldsTld](docs/InlineResponse2002TldsTld.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse20030](docs/InlineResponse20030.md)
 - [InlineResponse20030Data](docs/InlineResponse20030Data.md)
 - [InlineResponse20031](docs/InlineResponse20031.md)
 - [InlineResponse20031Data](docs/InlineResponse20031Data.md)
 - [InlineResponse20032](docs/InlineResponse20032.md)
 - [InlineResponse20033](docs/InlineResponse20033.md)
 - [InlineResponse20033Data](docs/InlineResponse20033Data.md)
 - [InlineResponse20034](docs/InlineResponse20034.md)
 - [InlineResponse20034Data](docs/InlineResponse20034Data.md)
 - [InlineResponse20035](docs/InlineResponse20035.md)
 - [InlineResponse20035Data](docs/InlineResponse20035Data.md)
 - [InlineResponse20036](docs/InlineResponse20036.md)
 - [InlineResponse20036Data](docs/InlineResponse20036Data.md)
 - [InlineResponse20037](docs/InlineResponse20037.md)
 - [InlineResponse20037Data](docs/InlineResponse20037Data.md)
 - [InlineResponse20038](docs/InlineResponse20038.md)
 - [InlineResponse20039](docs/InlineResponse20039.md)
 - [InlineResponse20039Data](docs/InlineResponse20039Data.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse20040](docs/InlineResponse20040.md)
 - [InlineResponse20040Data](docs/InlineResponse20040Data.md)
 - [InlineResponse20041](docs/InlineResponse20041.md)
 - [InlineResponse20041Data](docs/InlineResponse20041Data.md)
 - [InlineResponse20042](docs/InlineResponse20042.md)
 - [InlineResponse20042Data](docs/InlineResponse20042Data.md)
 - [InlineResponse20043](docs/InlineResponse20043.md)
 - [InlineResponse20043Data](docs/InlineResponse20043Data.md)
 - [InlineResponse20044](docs/InlineResponse20044.md)
 - [InlineResponse20045](docs/InlineResponse20045.md)
 - [InlineResponse20045Data](docs/InlineResponse20045Data.md)
 - [InlineResponse20046](docs/InlineResponse20046.md)
 - [InlineResponse20046Data](docs/InlineResponse20046Data.md)
 - [InlineResponse20047](docs/InlineResponse20047.md)
 - [InlineResponse20047Data](docs/InlineResponse20047Data.md)
 - [InlineResponse20048](docs/InlineResponse20048.md)
 - [InlineResponse20048Data](docs/InlineResponse20048Data.md)
 - [InlineResponse20049](docs/InlineResponse20049.md)
 - [InlineResponse20049Data](docs/InlineResponse20049Data.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse20050](docs/InlineResponse20050.md)
 - [InlineResponse20050Data](docs/InlineResponse20050Data.md)
 - [InlineResponse20051](docs/InlineResponse20051.md)
 - [InlineResponse20051Data](docs/InlineResponse20051Data.md)
 - [InlineResponse20052](docs/InlineResponse20052.md)
 - [InlineResponse20052Data](docs/InlineResponse20052Data.md)
 - [InlineResponse20053](docs/InlineResponse20053.md)
 - [InlineResponse20054](docs/InlineResponse20054.md)
 - [InlineResponse20055](docs/InlineResponse20055.md)
 - [InlineResponse20056](docs/InlineResponse20056.md)
 - [InlineResponse20057](docs/InlineResponse20057.md)
 - [InlineResponse20057Data](docs/InlineResponse20057Data.md)
 - [InlineResponse20058](docs/InlineResponse20058.md)
 - [InlineResponse20058Data](docs/InlineResponse20058Data.md)
 - [InlineResponse20059](docs/InlineResponse20059.md)
 - [InlineResponse20059Data](docs/InlineResponse20059Data.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse20060](docs/InlineResponse20060.md)
 - [InlineResponse20060Data](docs/InlineResponse20060Data.md)
 - [InlineResponse20061](docs/InlineResponse20061.md)
 - [InlineResponse20061Data](docs/InlineResponse20061Data.md)
 - [InlineResponse20062](docs/InlineResponse20062.md)
 - [InlineResponse20062Data](docs/InlineResponse20062Data.md)
 - [InlineResponse20063](docs/InlineResponse20063.md)
 - [InlineResponse20063Data](docs/InlineResponse20063Data.md)
 - [InlineResponse20064](docs/InlineResponse20064.md)
 - [InlineResponse20064Data](docs/InlineResponse20064Data.md)
 - [InlineResponse20065](docs/InlineResponse20065.md)
 - [InlineResponse20065Data](docs/InlineResponse20065Data.md)
 - [InlineResponse20066](docs/InlineResponse20066.md)
 - [InlineResponse20067](docs/InlineResponse20067.md)
 - [InlineResponse20067Data](docs/InlineResponse20067Data.md)
 - [InlineResponse20068](docs/InlineResponse20068.md)
 - [InlineResponse20068Data](docs/InlineResponse20068Data.md)
 - [InlineResponse20069](docs/InlineResponse20069.md)
 - [InlineResponse20069Data](docs/InlineResponse20069Data.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse20070](docs/InlineResponse20070.md)
 - [InlineResponse20070Data](docs/InlineResponse20070Data.md)
 - [InlineResponse20071](docs/InlineResponse20071.md)
 - [InlineResponse20072](docs/InlineResponse20072.md)
 - [InlineResponse20073](docs/InlineResponse20073.md)
 - [InlineResponse20074](docs/InlineResponse20074.md)
 - [InlineResponse20075](docs/InlineResponse20075.md)
 - [InlineResponse20076](docs/InlineResponse20076.md)
 - [InlineResponse20077](docs/InlineResponse20077.md)
 - [InlineResponse20078](docs/InlineResponse20078.md)
 - [InlineResponse20079](docs/InlineResponse20079.md)
 - [InlineResponse20079Data](docs/InlineResponse20079Data.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse20080](docs/InlineResponse20080.md)
 - [InlineResponse20081](docs/InlineResponse20081.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [N0capiemailsuspendEmails](docs/N0capiemailsuspendEmails.md)
 - [N0capiemailunsuspendEmails](docs/N0capiemailunsuspendEmails.md)
 - [ResellerapiDeletephdnszoneBody](docs/ResellerapiDeletephdnszoneBody.md)
 - [ResellerapiRegisterdomainBody](docs/ResellerapiRegisterdomainBody.md)
 - [ResellerapiRenewdomainBody](docs/ResellerapiRenewdomainBody.md)
 - [ResellerapiSavecontactdetailsBody](docs/ResellerapiSavecontactdetailsBody.md)
 - [ResellerapiSavenameserversBody](docs/ResellerapiSavenameserversBody.md)
 - [ResellerapiSavephdnsrecordsBody](docs/ResellerapiSavephdnsrecordsBody.md)
 - [ResellerapiSaveregistrarlockBody](docs/ResellerapiSaveregistrarlockBody.md)
 - [ResellerapiTransfertdomainBody](docs/ResellerapiTransfertdomainBody.md)
 - [StatsApacheBody](docs/StatsApacheBody.md)
 - [StatsDiskusageBody](docs/StatsDiskusageBody.md)
 - [StatsPerformanceBody](docs/StatsPerformanceBody.md)
 - [UserAddBody](docs/UserAddBody.md)
 - [UserAddsshkeyBody](docs/UserAddsshkeyBody.md)
 - [UserDisabletempdomainBody](docs/UserDisabletempdomainBody.md)
 - [UserEditsshkeyBody](docs/UserEditsshkeyBody.md)
 - [UserGrantaccessBody](docs/UserGrantaccessBody.md)
 - [UserRemoveBody](docs/UserRemoveBody.md)
 - [UserRemovesshkeyBody](docs/UserRemovesshkeyBody.md)
 - [UserTempdomainBody](docs/UserTempdomainBody.md)
 - [WordpressAddBody](docs/WordpressAddBody.md)
 - [WordpressRemoveBody](docs/WordpressRemoveBody.md)
 - [WorldapiCreateaccountBody](docs/WorldapiCreateaccountBody.md)
 - [WorldapiModifyresourcesBody](docs/WorldapiModifyresourcesBody.md)
 - [WorldapiSuspendaccountBody](docs/WorldapiSuspendaccountBody.md)
 - [WorldapiUnsuspendaccountBody](docs/WorldapiUnsuspendaccountBody.md)

## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header

## api_sandbox

- **Type**: API key
- **API key parameter name**: X-API-SANDBOX
- **Location**: HTTP header

## api_user

- **Type**: API key
- **API key parameter name**: X-API-USER
- **Location**: HTTP header


## Author

tech@support.planethoster.info