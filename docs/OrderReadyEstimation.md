# OrderReadyEstimation

Information related to the order ready time estimation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_change** | **bool** | A boolean value indicating if the order ready time can be changed. | 
**estimated_order_ready_time** | **datetime** | The order ready time for this order estimated by GrabFood, based on ISO_8601/RFC3339. | 
**max_order_ready_time** | **datetime** | The max allowed order ready time for this order, based on ISO_8601/RFC3339. | 
**new_order_ready_time** | **datetime** | The new order ready time for this order. Only present after a new order ready time is set (default will be null), based on ISO_8601/RFC3339. | [optional] 

## Example

```python
from grabfood.models.order_ready_estimation import OrderReadyEstimation

# TODO update the JSON string below
json = "{}"
# create an instance of OrderReadyEstimation from a JSON string
order_ready_estimation_instance = OrderReadyEstimation.from_json(json)
# print the JSON string representation of the object
print(OrderReadyEstimation.to_json())

# convert the object into a dict
order_ready_estimation_dict = order_ready_estimation_instance.to_dict()
# create an instance of OrderReadyEstimation from a dict
order_ready_estimation_from_dict = OrderReadyEstimation.from_dict(order_ready_estimation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


