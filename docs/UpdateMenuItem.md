# UpdateMenuItem

Information about the GrabFood client updating their food menu. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | 
**var_field** | **str** | The record type that you want to update. | 
**id** | **str** | The record&#39;s ID on the partner system. For example, the item id in case type is ITEM. | 
**price** | **int** | The record&#39;s price in minor unit format. | [optional] 
**available_status** | **str** | The record&#39;s availableStatus.   Note: In order to set an item as \&quot;UNAVAILABLE\&quot;, it is required to update both the &#x60;availableStatus&#x60; and &#x60;maxStock&#x60; fields, whereby the &#x60;maxStock&#x60; value should be set to 0.  | [optional] 
**max_stock** | **int** | Available stocks under inventory for this item. Auto reduce when there is order placed for this item.  Note: It is necessary to set &#x60;maxStock&#x60; to 0 if the &#x60;availableStatus&#x60; of the item is \&quot;UNAVAILABLE\&quot;. Item will be set to \&quot;AVAILABLE\&quot; if &#x60;maxStock&#x60; &gt; 0.  | [optional] 
**advanced_pricings** | [**List[UpdateAdvancedPricing]**](UpdateAdvancedPricing.md) | Price configuration (in minor unit) for different service, order type and channel combination. If a service type does not have a specified price, it will utilize the default price of the item.  | [optional] 
**purchasabilities** | [**List[UpdatePurchasability]**](UpdatePurchasability.md) | Purchasability is set to true by default for all service type, unless it is explicitly set to false. Modifier will reuse it’s item’s purchasability.  | [optional] 

## Example

```python
from grabfood.models.update_menu_item import UpdateMenuItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMenuItem from a JSON string
update_menu_item_instance = UpdateMenuItem.from_json(json)
# print the JSON string representation of the object
print(UpdateMenuItem.to_json())

# convert the object into a dict
update_menu_item_dict = update_menu_item_instance.to_dict()
# create an instance of UpdateMenuItem from a dict
update_menu_item_from_dict = UpdateMenuItem.from_dict(update_menu_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


