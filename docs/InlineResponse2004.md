# InlineResponse2004

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** | Response message. | [optional] 
**order_id** | **object** | Domain order ID. | [optional] 
**is_transfer** | **object** | Is the domain a transfer? | [optional] 
**is_registration** | **object** | Is the domain a registration? | [optional] 
**registration_date** | **object** | Date format: &#x60;YYYY-MM-DD&#x60;. | [optional] 
**expiry_date** | **object** | Date format: &#x60;YYYY-MM-DD&#x60;. Not present for incomplete domain transfers. | [optional] 
**registration_status** | **object** | Registration status. | [optional] 
**registration_status_info** | **object** | Additional information on why the registration status is the way it is. | [optional] 
**purchase_status** | **object** | Registration order status. | [optional] 
**id_protection** | **object** | Whether or not WHOIS ID protection is enabled for the domain. | [optional] 
**domain_statuses** | **object** | Domain status at the registry. Not always present. | [optional] 
**transfer_request_status** | **object** | Only present for ICANN TLDs domain transfers. | [optional] 
**transfer_request_denied_reason** | **object** | Only present for ICANN TLDs domain transfers and if the transfer was denied. | [optional] 
**transfer_request_denied_at** | **object** | Date format: &#x60;YYYY-MM-DD&#x60;. Only present for ICANN TLDs domain transfers, and if the transfer was denied. | [optional] 
**transfer_request_confirmed_at** | **object** | Date format: &#x60;YYYY-MM-DD&#x60;. Only present for ICANN TLDs domain transfers, and if the transfer was confirmed by an email from the registrant. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

