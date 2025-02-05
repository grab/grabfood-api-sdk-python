# OrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The item&#39;s externalID in the partner system.  | 
**grab_item_id** | **str** | The item&#39;s ID in Grab system. Partner can use this field in the &#x60;EditOrder&#x60; endpoint. | 
**quantity** | **int** | The number of the item ordered. | 
**price** | **int** | The price for a single item along with its associated modifiers in minor unit and tax-inclusive.  &#x60;&#x60;&#x60; price &#x3D; Item price(tax inclusive) + Modifier price(tax inclusive) | (2241*1.06)+(165*1.06)&#x3D;2550  | 
**tax** | **int** | Tax in minor format for a single item along with its associated modifiers. &#x60;0&#x60; if tax configuration is absent. Refer to FAQs for more details about [tax](#section/Order/How-is-tax-calculated). &#x60;&#x60;&#x60; tax &#x3D; Item tax + Modifier tax | (2241*0.06)+(165*0.06)&#x3D;144  | [optional] 
**specifications** | **str** | An extra note for the merchant. Empty if no note from consumer.  | [optional] 
**out_of_stock_instruction** | [**OutOfStockInstruction**](OutOfStockInstruction.md) |  | [optional] 
**modifiers** | [**List[OrderItemModifier]**](OrderItemModifier.md) | An array of JSON objects modifiers. | [optional] 

## Example

```python
from grabfood.models.order_item import OrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItem from a JSON string
order_item_instance = OrderItem.from_json(json)
# print the JSON string representation of the object
print(OrderItem.to_json())

# convert the object into a dict
order_item_dict = order_item_instance.to_dict()
# create an instance of OrderItem from a dict
order_item_from_dict = OrderItem.from_dict(order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


