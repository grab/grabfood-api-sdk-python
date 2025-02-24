# GetMembershipNativeResponsePointInfo

Obtain contains user's point details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_points** | **int** | Point that user currently obtained. | [optional] 
**max_points** | **int** | Maximum point that user can obtain. | [optional] 
**expire_points** | **int** | Points that would get expired in future. | [optional] 

## Example

```python
from grabfood.models.get_membership_native_response_point_info import GetMembershipNativeResponsePointInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetMembershipNativeResponsePointInfo from a JSON string
get_membership_native_response_point_info_instance = GetMembershipNativeResponsePointInfo.from_json(json)
# print the JSON string representation of the object
print(GetMembershipNativeResponsePointInfo.to_json())

# convert the object into a dict
get_membership_native_response_point_info_dict = get_membership_native_response_point_info_instance.to_dict()
# create an instance of GetMembershipNativeResponsePointInfo from a dict
get_membership_native_response_point_info_from_dict = GetMembershipNativeResponsePointInfo.from_dict(get_membership_native_response_point_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


