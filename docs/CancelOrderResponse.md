# CancelOrderResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit_type** | [**CancelOrderLimitType**](CancelOrderLimitType.md) |  | [optional] 
**limit_times** | **int** | The remaining cancellation quota for the merchant. A value is only returned when the nearest remaining cancellation limit is approaching, else it returns 0. | [optional] 

## Example

```python
from grabfood.models.cancel_order_response import CancelOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelOrderResponse from a JSON string
cancel_order_response_instance = CancelOrderResponse.from_json(json)
# print the JSON string representation of the object
print(CancelOrderResponse.to_json())

# convert the object into a dict
cancel_order_response_dict = cancel_order_response_instance.to_dict()
# create an instance of CancelOrderResponse from a dict
cancel_order_response_from_dict = CancelOrderResponse.from_dict(cancel_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


