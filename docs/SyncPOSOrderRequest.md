# SyncPOSOrderRequest

The syncPOSOrder API allows POS to sync its order data with Grab and generate a PayBill QR.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | This action indicates the target action POS wants to do, eg, BILL_GENERATED, COMPLETED. | 
**order** | [**PosOrder**](PosOrder.md) |  | 

## Example

```python
from grabfood.models.sync_pos_order_request import SyncPOSOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncPOSOrderRequest from a JSON string
sync_pos_order_request_instance = SyncPOSOrderRequest.from_json(json)
# print the JSON string representation of the object
print(SyncPOSOrderRequest.to_json())

# convert the object into a dict
sync_pos_order_request_dict = sync_pos_order_request_instance.to_dict()
# create an instance of SyncPOSOrderRequest from a dict
sync_pos_order_request_from_dict = SyncPOSOrderRequest.from_dict(sync_pos_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


