# NewOrderTimeRequest

This request updates an order with a new ready time on GrabFood. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The order&#39;s ID that is returned from GrabFood. Refer to FAQs for more details about [orderID and shortOrderNumber](#section/Order/What&#39;s-the-difference-between-orderID-and-shortOrderNumber). | 
**new_order_ready_time** | **datetime** | The new order ready time for this order, based on ISO_8601/RFC3339. | 

## Example

```python
from grabfood.models.new_order_time_request import NewOrderTimeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NewOrderTimeRequest from a JSON string
new_order_time_request_instance = NewOrderTimeRequest.from_json(json)
# print the JSON string representation of the object
print(NewOrderTimeRequest.to_json())

# convert the object into a dict
new_order_time_request_dict = new_order_time_request_instance.to_dict()
# create an instance of NewOrderTimeRequest from a dict
new_order_time_request_from_dict = NewOrderTimeRequest.from_dict(new_order_time_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


