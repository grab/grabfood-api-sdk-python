# EditOrderRequest

Information about editing an existing order on GrabFood. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The order&#39;s ID that is returned from GrabFood. Refer to FAQs for more details about [orderID and shortOrderNumber](#section/Order/What&#39;s-the-difference-between-orderID-and-shortOrderNumber). | 
**items** | [**List[EditOrderItem]**](EditOrderItem.md) | Specify the array of all items in the order, including deleted, added, updated and unchanged items. | 
**only_recalculate** | **bool** | This parameter specifies whether to recalculate the edited order without submitting it. It is intended for testing purposes only. This parameter is set to false by default, which means the edited order will be recalculated and re-submitted to partners.  | [optional] 

## Example

```python
from grabfood.models.edit_order_request import EditOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditOrderRequest from a JSON string
edit_order_request_instance = EditOrderRequest.from_json(json)
# print the JSON string representation of the object
print(EditOrderRequest.to_json())

# convert the object into a dict
edit_order_request_dict = edit_order_request_instance.to_dict()
# create an instance of EditOrderRequest from a dict
edit_order_request_from_dict = EditOrderRequest.from_dict(edit_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


