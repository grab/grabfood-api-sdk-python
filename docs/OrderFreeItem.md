# OrderFreeItem

Free item information for `freeItem` campaign.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The free item&#39;s externalID in the partner system. Empty if not applicable. | [optional] 
**name** | **str** | The name of the free item. Empty if not applicable.  | [optional] 
**quantity** | **int** | The item&#39;s quantity. Maximum is **1**. | [optional] 
**price** | **int** | The item&#39;s price in minor unit format. | [optional] 

## Example

```python
from grabfood.models.order_free_item import OrderFreeItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrderFreeItem from a JSON string
order_free_item_instance = OrderFreeItem.from_json(json)
# print the JSON string representation of the object
print(OrderFreeItem.to_json())

# convert the object into a dict
order_free_item_dict = order_free_item_instance.to_dict()
# create an instance of OrderFreeItem from a dict
order_free_item_from_dict = OrderFreeItem.from_dict(order_free_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


