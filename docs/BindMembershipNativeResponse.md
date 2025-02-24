# BindMembershipNativeResponse

This response returns membershipID after membership binding is successful. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | The unique member ID on the partner&#39;s database. | 

## Example

```python
from grabfood.models.bind_membership_native_response import BindMembershipNativeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BindMembershipNativeResponse from a JSON string
bind_membership_native_response_instance = BindMembershipNativeResponse.from_json(json)
# print the JSON string representation of the object
print(BindMembershipNativeResponse.to_json())

# convert the object into a dict
bind_membership_native_response_dict = bind_membership_native_response_instance.to_dict()
# create an instance of BindMembershipNativeResponse from a dict
bind_membership_native_response_from_dict = BindMembershipNativeResponse.from_dict(bind_membership_native_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


