# SyncPOSOrderResponse

The Sync POS Order response, include grab order ID and paybill QR deeplink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The orderID in grab system. | [optional] 
**paybill_qr_code** | **str** | The paybill QR Code. | [optional] 

## Example

```python
from grabfood.models.sync_pos_order_response import SyncPOSOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyncPOSOrderResponse from a JSON string
sync_pos_order_response_instance = SyncPOSOrderResponse.from_json(json)
# print the JSON string representation of the object
print(SyncPOSOrderResponse.to_json())

# convert the object into a dict
sync_pos_order_response_dict = sync_pos_order_response_instance.to_dict()
# create an instance of SyncPOSOrderResponse from a dict
sync_pos_order_response_from_dict = SyncPOSOrderResponse.from_dict(sync_pos_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


