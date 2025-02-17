# UnbindMembershipNativeRequest

This request submits membership unbind request to partner. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | The unique member ID on the partner&#39;s database. | 

## Example

```python
from grabfood.models.unbind_membership_native_request import UnbindMembershipNativeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnbindMembershipNativeRequest from a JSON string
unbind_membership_native_request_instance = UnbindMembershipNativeRequest.from_json(json)
# print the JSON string representation of the object
print(UnbindMembershipNativeRequest.to_json())

# convert the object into a dict
unbind_membership_native_request_dict = unbind_membership_native_request_instance.to_dict()
# create an instance of UnbindMembershipNativeRequest from a dict
unbind_membership_native_request_from_dict = UnbindMembershipNativeRequest.from_dict(unbind_membership_native_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


