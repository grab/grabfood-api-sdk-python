# CancelOrderRequest

This request cancels an order on GrabFood. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The order&#39;s ID that is returned from GrabFood. Refer to FAQs for more details about [orderID and shortOrderNumber](#section/Order/What&#39;s-the-difference-between-orderID-and-shortOrderNumber). | 
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | 
**cancel_code** | [**CancelCode**](CancelCode.md) |  | 

## Example

```python
from grabfood.models.cancel_order_request import CancelOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelOrderRequest from a JSON string
cancel_order_request_instance = CancelOrderRequest.from_json(json)
# print the JSON string representation of the object
print(CancelOrderRequest.to_json())

# convert the object into a dict
cancel_order_request_dict = cancel_order_request_instance.to_dict()
# create an instance of CancelOrderRequest from a dict
cancel_order_request_from_dict = CancelOrderRequest.from_dict(cancel_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


