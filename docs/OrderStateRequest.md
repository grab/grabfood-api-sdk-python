# OrderStateRequest

This request pushes the state of an order on GrabFood. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | 
**partner_merchant_id** | **str** | The merchant&#39;s ID that is on the partner&#39;s database. | [optional] 
**order_id** | **str** | The order&#39;s ID that is returned from GrabFood. Refer to FAQs for more details about [orderID and shortOrderNumber](#section/Order/What&#39;s-the-difference-between-orderID-and-shortOrderNumber). | 
**state** | **str** | The current order state. For takeaway orders, only &#x60;DELIVERED&#x60; and &#x60;CANCELLED&#x60; states are pushed. | 
**driver_eta** | **int** | The driver&#39;s estimated of arrival (ETA) in seconds when the state is &#x60;DRIVER_ALLOCATED&#x60;. | [optional] 
**code** | **str** | The current order&#39;s sub-state. This is in free text so you should only use for reference. Grab may use this for troubleshooting. If you want some analysis, kindly use &#x60;state&#x60; instead. | [optional] 
**message** | **str** | Additional information to explain the current order state. May be system status or human entered message. | [optional] 

## Example

```python
from grabfood.models.order_state_request import OrderStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStateRequest from a JSON string
order_state_request_instance = OrderStateRequest.from_json(json)
# print the JSON string representation of the object
print(OrderStateRequest.to_json())

# convert the object into a dict
order_state_request_dict = order_state_request_instance.to_dict()
# create an instance of OrderStateRequest from a dict
order_state_request_from_dict = OrderStateRequest.from_dict(order_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


