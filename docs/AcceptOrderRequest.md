# AcceptOrderRequest

The manual acceptance or rejection of an order on GrabFood. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The order&#39;s ID that is returned from GrabFood. Refer to FAQs for more details about [orderID and shortOrderNumber](#section/Order/What&#39;s-the-difference-between-orderID-and-shortOrderNumber). | 
**to_state** | **str** | The order&#39;s updated state. | 

## Example

```python
from grabfood.models.accept_order_request import AcceptOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptOrderRequest from a JSON string
accept_order_request_instance = AcceptOrderRequest.from_json(json)
# print the JSON string representation of the object
print(AcceptOrderRequest.to_json())

# convert the object into a dict
accept_order_request_dict = accept_order_request_instance.to_dict()
# create an instance of AcceptOrderRequest from a dict
accept_order_request_from_dict = AcceptOrderRequest.from_dict(accept_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


