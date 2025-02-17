# EditOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The item&#39;s ID in Grab system that can be obtained from the [Submit Order Webhook](#tag/submit-order-webhook/operation/submit-order-webhook) request payload parameters under &#x60;items[].grabItemID&#x60;, or &#x60;items[].outOfStockInstruction.replacementGrabItemID&#x60; for item replacement. External item ID from Partner system is only supported when &#x60;ADDED&#x60; status and &#x60;isExternalItemID: true&#x60;. | 
**status** | **str** | The item&#39;s edited status. Leave empty string if there is no change to the item. | 
**quantity** | **int** | The item&#39;s quantity. If the item is not being updated or deleted, use the original quantity. | [optional] 
**is_external_item_id** | **bool** | Only applicable for &#x60;ADDED&#x60;status. Indicate if the &#x60;itemID&#x60; is an external item ID. Grab checks for the items that are mapped to the provided item ID, considering their availability. If multiple Grab items are found to be mapped to the provided external item ID, the last updated item will be chosen. If no suitable record is found, an 400 error will be returned to the partner, indicating that the submitted external item ID cannot be edited. | [optional] 

## Example

```python
from grabfood.models.edit_order_item import EditOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of EditOrderItem from a JSON string
edit_order_item_instance = EditOrderItem.from_json(json)
# print the JSON string representation of the object
print(EditOrderItem.to_json())

# convert the object into a dict
edit_order_item_dict = edit_order_item_instance.to_dict()
# create an instance of EditOrderItem from a dict
edit_order_item_from_dict = EditOrderItem.from_dict(edit_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


