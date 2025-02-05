# OrderItemModifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The modifier&#39;s ID that is on the partner&#39;s system. | [optional] 
**price** | **int** | The modifier&#39;s price (tax-inclusive) in minor format.  &#x60;&#x60;&#x60; price &#x3D; round(165 * (1 + 0.06)) &#x3D; 175  | [optional] 
**tax** | **int** | Tax in minor format for 1 modifier. Refer to FAQs for more details about [tax](#section/Order/How-is-tax-calculated). &#x60;&#x60;&#x60; tax &#x3D; 165*0.06&#x3D;10  | [optional] 
**quantity** | **int** | The number of modifiers present. The value is always 1. | [optional] 

## Example

```python
from grabfood.models.order_item_modifier import OrderItemModifier

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemModifier from a JSON string
order_item_modifier_instance = OrderItemModifier.from_json(json)
# print the JSON string representation of the object
print(OrderItemModifier.to_json())

# convert the object into a dict
order_item_modifier_dict = order_item_modifier_instance.to_dict()
# create an instance of OrderItemModifier from a dict
order_item_modifier_from_dict = OrderItemModifier.from_dict(order_item_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


