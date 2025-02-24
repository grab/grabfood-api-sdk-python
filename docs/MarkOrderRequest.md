# MarkOrderRequest

This request marks an order as ready for delivery or completed on GrabFood. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The order&#39;s ID that is returned from GrabFood. Refer to FAQs for more details about [orderID and shortOrderNumber](#section/Order/What&#39;s-the-difference-between-orderID-and-shortOrderNumber). | 
**mark_status** | **int** | The status to be marked accordingly.  * &#x60;1&#x60; - mark order as ready  * &#x60;2&#x60; - mark order as completed and only applicable to **dine-in** orders  | 

## Example

```python
from grabfood.models.mark_order_request import MarkOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MarkOrderRequest from a JSON string
mark_order_request_instance = MarkOrderRequest.from_json(json)
# print the JSON string representation of the object
print(MarkOrderRequest.to_json())

# convert the object into a dict
mark_order_request_dict = mark_order_request_instance.to_dict()
# create an instance of MarkOrderRequest from a dict
mark_order_request_from_dict = MarkOrderRequest.from_dict(mark_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


