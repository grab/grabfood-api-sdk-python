# PosItemModifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The modifier’s ID in the partner system.  | [optional] 
**name** | **str** | The name of the modifier. | [optional] 
**quantity** | **int** | The number of the modifier ordered. | [optional] 
**price** | **int** | The modifier’s price in minor units and tax-inclusive in the partner system.  | [optional] 
**tax** | **int** | This is the tax amount on the modifier. If grab needs to show modifier excl-tax price, we’ll use this value to calculate. &#x60;&#x60;&#x60; Price excl-tax &#x3D; price - tax  | [optional] 

## Example

```python
from grabfood.models.pos_item_modifier import PosItemModifier

# TODO update the JSON string below
json = "{}"
# create an instance of PosItemModifier from a JSON string
pos_item_modifier_instance = PosItemModifier.from_json(json)
# print the JSON string representation of the object
print(PosItemModifier.to_json())

# convert the object into a dict
pos_item_modifier_dict = pos_item_modifier_instance.to_dict()
# create an instance of PosItemModifier from a dict
pos_item_modifier_from_dict = PosItemModifier.from_dict(pos_item_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


