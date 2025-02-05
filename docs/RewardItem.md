# RewardItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The item&#39;s ID in partner system. | [optional] 
**quantity** | **int** | The item&#39;s quantity. | [optional] 

## Example

```python
from grabfood.models.reward_item import RewardItem

# TODO update the JSON string below
json = "{}"
# create an instance of RewardItem from a JSON string
reward_item_instance = RewardItem.from_json(json)
# print the JSON string representation of the object
print(RewardItem.to_json())

# convert the object into a dict
reward_item_dict = reward_item_instance.to_dict()
# create an instance of RewardItem from a dict
reward_item_from_dict = RewardItem.from_dict(reward_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


