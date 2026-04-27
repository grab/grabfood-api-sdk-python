# VirtualContact

A JSON object containing the virtual contact information, where the validity period is 6 hours. Refer [FAQ](#section/Order/How-to-contact-customer-using-the-virtual-contact) on how the virtual contact works.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | The generated virtual phone number that will forward calls to the customer&#39;s actual phone number. Will be omitted if the &#x60;status&#x60; is not &#x60;ACTIVE&#x60;. | [optional] 
**pin** | **str** | A unique PIN required when forwarding calls to the customer for verification and security. Will be omitted if the &#x60;status&#x60; is not &#x60;ACTIVE&#x60;. | [optional] 
**expired_at** | **str** | The expiry time of the virtual contact in UTC based on ISO_8601/RFC3339. Will be omitted if the &#x60;status&#x60; is not &#x60;ACTIVE&#x60;. | [optional] 
**status** | **str** | Indicates the current status and validity of the virtual contact. * &#x60;ACTIVE&#x60; - The virtual contact is valid. * &#x60;EXPIRED&#x60; - The virtual contact has expired and is no longer valid. * &#x60;UNAVAILABLE&#x60; - An internal error occurred while generating or retrieving the virtual contact.  | [optional] 

## Example

```python
from grabfood.models.virtual_contact import VirtualContact

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualContact from a JSON string
virtual_contact_instance = VirtualContact.from_json(json)
# print the JSON string representation of the object
print(VirtualContact.to_json())

# convert the object into a dict
virtual_contact_dict = virtual_contact_instance.to_dict()
# create an instance of VirtualContact from a dict
virtual_contact_from_dict = VirtualContact.from_dict(virtual_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


