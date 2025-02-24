# DineIn

A JSON object containing order at table information. Only applicable for dine-in order. `null` if not applicable. Not present in [ListOrder](#tag/list-order/operation/list-orders) response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_id** | **str** | Table number. | [optional] 
**eater_count** | **int** | The number of eaters. | [optional] 

## Example

```python
from grabfood.models.dine_in import DineIn

# TODO update the JSON string below
json = "{}"
# create an instance of DineIn from a JSON string
dine_in_instance = DineIn.from_json(json)
# print the JSON string representation of the object
print(DineIn.to_json())

# convert the object into a dict
dine_in_dict = dine_in_instance.to_dict()
# create an instance of DineIn from a dict
dine_in_from_dict = DineIn.from_dict(dine_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


