# GetRewardNativeResponse

This response returns reward points earn for this order. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | **int** | The reward points earned in this purchase. | 

## Example

```python
from grabfood.models.get_reward_native_response import GetRewardNativeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRewardNativeResponse from a JSON string
get_reward_native_response_instance = GetRewardNativeResponse.from_json(json)
# print the JSON string representation of the object
print(GetRewardNativeResponse.to_json())

# convert the object into a dict
get_reward_native_response_dict = get_reward_native_response_instance.to_dict()
# create an instance of GetRewardNativeResponse from a dict
get_reward_native_response_from_dict = GetRewardNativeResponse.from_dict(get_reward_native_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


