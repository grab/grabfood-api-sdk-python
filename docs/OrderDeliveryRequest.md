# OrderDeliveryRequest

This request marks an order as delivered on GrabFood. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The order&#39;s ID that is returned from GrabFood. Refer to FAQs for more details about [orderID and shortOrderNumber](#section/Order/What&#39;s-the-difference-between-orderID-and-shortOrderNumber). | 
**from_state** | **str** | Specify the order&#39;s initial state. | 
**to_state** | **str** | Specify the order&#39;s new state. | 

## Example

```python
from grabfood.models.order_delivery_request import OrderDeliveryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDeliveryRequest from a JSON string
order_delivery_request_instance = OrderDeliveryRequest.from_json(json)
# print the JSON string representation of the object
print(OrderDeliveryRequest.to_json())

# convert the object into a dict
order_delivery_request_dict = order_delivery_request_instance.to_dict()
# create an instance of OrderDeliveryRequest from a dict
order_delivery_request_from_dict = OrderDeliveryRequest.from_dict(order_delivery_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


