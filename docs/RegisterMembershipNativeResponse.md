# RegisterMembershipNativeResponse

This response returns membershipID after membership binding is successful. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | The unique member ID on the partner&#39;s database. | 

## Example

```python
from grabfood.models.register_membership_native_response import RegisterMembershipNativeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterMembershipNativeResponse from a JSON string
register_membership_native_response_instance = RegisterMembershipNativeResponse.from_json(json)
# print the JSON string representation of the object
print(RegisterMembershipNativeResponse.to_json())

# convert the object into a dict
register_membership_native_response_dict = register_membership_native_response_instance.to_dict()
# create an instance of RegisterMembershipNativeResponse from a dict
register_membership_native_response_from_dict = RegisterMembershipNativeResponse.from_dict(register_membership_native_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


