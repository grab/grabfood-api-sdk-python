# BindMembershipNativeRequest

This request submits membership binding request to partner. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grab_id** | **str** | The id used to identify an unique grab user. | 
**phone_number** | **str** | Grab user phone number used to login. | [optional] 

## Example

```python
from grabfood.models.bind_membership_native_request import BindMembershipNativeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BindMembershipNativeRequest from a JSON string
bind_membership_native_request_instance = BindMembershipNativeRequest.from_json(json)
# print the JSON string representation of the object
print(BindMembershipNativeRequest.to_json())

# convert the object into a dict
bind_membership_native_request_dict = bind_membership_native_request_instance.to_dict()
# create an instance of BindMembershipNativeRequest from a dict
bind_membership_native_request_from_dict = BindMembershipNativeRequest.from_dict(bind_membership_native_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


