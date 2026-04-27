# POSItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The item&#39;s externalID in the partner system.  | [optional] 
**grab_item_id** | **str** | The item&#39;s ID in Grab system. Partner can use this field in the &#x60;EditOrder&#x60; endpoint. Note: The index number (after &#x60;#&#x60;) is different for the same item with different modifiers. This helps identify items when editing complex orders. This is currently controlled by feature flag until full rollout, for non whitelisted partners, the &#39;#&#39; and index number will not be included.  | [optional] 
**name** | **str** | The name of the item. | [optional] 
**quantity** | **int** | The number of the item ordered. | [optional] 
**modifiers** | [**List[PosItemModifier]**](PosItemModifier.md) | The ordered items in an array of JSON Object.  | [optional] 
**price** | **int** | The price for a single item along with its associated modifiers in minor unit and tax-inclusive.  &#x60;&#x60;&#x60; price &#x3D; Item price(tax inclusive) + Modifier price(tax inclusive) | (2241*1.06)+(165*1.06)&#x3D;2550  | [optional] 
**tax** | **int** | Tax in minor format for a single item along with its associated modifiers. &#x60;0&#x60; if tax configuration is absent. Refer to FAQs for more details about [tax](#section/Order/How-is-tax-calculated). &#x60;&#x60;&#x60; tax &#x3D; Item tax + Modifier tax | (2241*0.06)+(165*0.06)&#x3D;144  | [optional] 

## Example

```python
from grabfood.models.pos_item import POSItem

# TODO update the JSON string below
json = "{}"
# create an instance of POSItem from a JSON string
pos_item_instance = POSItem.from_json(json)
# print the JSON string representation of the object
print(POSItem.to_json())

# convert the object into a dict
pos_item_dict = pos_item_instance.to_dict()
# create an instance of POSItem from a dict
pos_item_from_dict = POSItem.from_dict(pos_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


