# RefundOrderRequest

The API is to refund a STO order in dineout flow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | This order ID in grab system. | 
**merchant_id** | **str** | This merchant ID in grab system. | 
**is_full_refund** | **bool** | currently we only support fully refund. | [optional] 
**refund_amount_in_min** | **int** | The total amount the POS want to refund for STO order. | [optional] 

## Example

```python
from grabfood.models.refund_order_request import RefundOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefundOrderRequest from a JSON string
refund_order_request_instance = RefundOrderRequest.from_json(json)
# print the JSON string representation of the object
print(RefundOrderRequest.to_json())

# convert the object into a dict
refund_order_request_dict = refund_order_request_instance.to_dict()
# create an instance of RefundOrderRequest from a dict
refund_order_request_from_dict = RefundOrderRequest.from_dict(refund_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


