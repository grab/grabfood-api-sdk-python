# GetMembershipNativeResponse

This response returns membership detail. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_status** | **str** | Status of the memberID. | [optional] 
**point_info** | [**GetMembershipNativeResponsePointInfo**](GetMembershipNativeResponsePointInfo.md) |  | [optional] 
**points_expire_date** | **str** | Earliest points expiry date. In &#x60;yyyy-mm-dd&#x60; format | [optional] 

## Example

```python
from grabfood.models.get_membership_native_response import GetMembershipNativeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMembershipNativeResponse from a JSON string
get_membership_native_response_instance = GetMembershipNativeResponse.from_json(json)
# print the JSON string representation of the object
print(GetMembershipNativeResponse.to_json())

# convert the object into a dict
get_membership_native_response_dict = get_membership_native_response_instance.to_dict()
# create an instance of GetMembershipNativeResponse from a dict
get_membership_native_response_from_dict = GetMembershipNativeResponse.from_dict(get_membership_native_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


