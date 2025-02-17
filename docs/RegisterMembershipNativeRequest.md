# RegisterMembershipNativeRequest

This request submits membership registration request to partner. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grab_id** | **str** | The id used to identify an unique grab user. | 
**phone_number** | **str** | Grab user&#39;s phone number for registration. | [optional] 
**name** | **str** | Grab user&#39;s name for registration. | [optional] 
**email** | **str** | Grab user&#39;s email address for registration. | [optional] 

## Example

```python
from grabfood.models.register_membership_native_request import RegisterMembershipNativeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterMembershipNativeRequest from a JSON string
register_membership_native_request_instance = RegisterMembershipNativeRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterMembershipNativeRequest.to_json())

# convert the object into a dict
register_membership_native_request_dict = register_membership_native_request_instance.to_dict()
# create an instance of RegisterMembershipNativeRequest from a dict
register_membership_native_request_from_dict = RegisterMembershipNativeRequest.from_dict(register_membership_native_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


