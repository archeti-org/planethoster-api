# ResellerapiSavephdnsrecordsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sld** | **object** | Domain name without the Top-Level Domain. | 
**tld** | **object** | TLD without the leading period. | 
**type1** | **object** | Record types. | 
**hostname1** | **object** | Hostname with which to associate the DNS record. | 
**address1** | **object** | Value depends on &#x60;type&#x60; given.   *For A and AAAA records, this is the IP address.*   *For CNAME records, this is the canonical name itself.*   *For MX and MXE records, this is the exchange.*   *For TXT records, this is the TXT data.*  | 
**ttl1** | **object** | DNS TTL (time to live) represents the time each step takes for DNS to cache a record | [optional] 
**priority1** | **object** | Priority is for MX and MXE records only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

