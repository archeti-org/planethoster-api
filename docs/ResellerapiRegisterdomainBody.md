# ResellerapiRegisterdomainBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sld** | **object** | Domain name without the Top-Level Domain. | 
**tld** | **object** | TLD without the leading period. | 
**period** | **object** | Number of years to register the domain name.   See [Tld prices](#operation/tldPrices)  | 
**ns1** | **object** | Existing nameserver to use for DNS lookup of the registered domain. | 
**ns2** | **object** | Existing nameserver to use for DNS lookup of the registered domain. | 
**ns3** | **object** | Existing nameserver to use for DNS lookup of the registered domain. | [optional] 
**ns4** | **object** | Existing nameserver to use for DNS lookup of the registered domain. | [optional] 
**ns5** | **object** | Existing nameserver to use for DNS lookup of the registered domain. | [optional] 
**id_protection** | **object** | Whether or not to order WHOIS ID protection for this domain name.   *Note that not all TLDs support ID protection.*   See [Tld prices](#operation/tldPrices)  | 
**register_if_premium** | **object** | Register the domain name even if it is a Premium domain, which could be much more expensive. | 
**use_planethoster_nameservers** | **object** | Only set this to true when using &#x27;nsa.n0c.com&#x27;, &#x27;nsb.n0c.com&#x27;, and &#x27;nsc.n0c.com&#x27; as your ns1, ns2 and ns3 values (ns4 and ns5 should be empty strings in this case). This option creates a DNS zone for the domain name on the nameservers after successful registration.  | 
**addtl_field** | **object** | Object that represent additional fields specific for the TLD that is being registered.   See the index of [available additional fields](#) for each TLD.  *Note that some additional fields are required!*  | [optional] 
**registrant_first_name** | **object** | First name of the domain name registrant contact. | 
**registrant_last_name** | **object** | Last name of the domain name registrant contact. | 
**registrant_email** | **object** | Email address of the domain name registrant contact. | 
**registrant_company_name** | **object** | Name of company or organization for which the registrant contact is registering the domain name. *Can be empty if it is for personal use.*  | [optional] 
**registrant_address1** | **object** | Civic number and street name of company or registrant contact&#x27;s primary residence. | 
**registrant_address2** | **object** | Civic number and street name of registrant contact&#x27;s secondary residence.   *Can be empty.*  | [optional] 
**registrant_city** | **object** | Name of the city in which registrant contact resides. | 
**registrant_postal_code** | **object** | Postal code or ZIP code of registrant contact&#x27;s residence. | 
**registrant_state** | **object** | State or province of registrant contact&#x27;s residence. | 
**registrant_country_code** | **object** | Two letters code of registrant contact&#x27;s residence country.   &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\&quot; target&#x3D;\&quot;_blank\&quot;&gt;See country code list&lt;/a&gt;  | 
**registrant_phone** | **object** | Phone number, including area code: &#x27;+1.&#x27; for Canada or &#x27;+33.&#x27; for France.   *With international calling code at the beginning.*  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

