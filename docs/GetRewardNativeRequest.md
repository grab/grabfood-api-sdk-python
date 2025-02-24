# GetRewardNativeRequest

This request submits membership detail and order value to get reward calculation. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | The unique member ID on the partner&#39;s database. | [optional] 
**merchant_id** | **str** | Grab merchant&#39;s ID. | [optional] 
**items** | [**List[RewardItem]**](RewardItem.md) |  | [optional] 
**order_value** | **int** | The post-discount order value. | [optional] 

## Example

```python
from grabfood.models.get_reward_native_request import GetRewardNativeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetRewardNativeRequest from a JSON string
get_reward_native_request_instance = GetRewardNativeRequest.from_json(json)
# print the JSON string representation of the object
print(GetRewardNativeRequest.to_json())

# convert the object into a dict
get_reward_native_request_dict = get_reward_native_request_instance.to_dict()
# create an instance of GetRewardNativeRequest from a dict
get_reward_native_request_from_dict = GetRewardNativeRequest.from_dict(get_reward_native_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


