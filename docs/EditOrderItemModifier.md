# EditOrderItemModifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The modifier&#39;s external ID in partner system. | [optional] 
**quantity** | **int** | The modifier&#39;s quantity. 0 to remove the modifier, 1 to add or keep the modifier. | [optional] 

## Example

```python
from grabfood.models.edit_order_item_modifier import EditOrderItemModifier

# TODO update the JSON string below
json = "{}"
# create an instance of EditOrderItemModifier from a JSON string
edit_order_item_modifier_instance = EditOrderItemModifier.from_json(json)
# print the JSON string representation of the object
print(EditOrderItemModifier.to_json())

# convert the object into a dict
edit_order_item_modifier_dict = edit_order_item_modifier_instance.to_dict()
# create an instance of EditOrderItemModifier from a dict
edit_order_item_modifier_from_dict = EditOrderItemModifier.from_dict(edit_order_item_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


