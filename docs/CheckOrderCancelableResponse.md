# CheckOrderCancelableResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_able** | **bool** | The boolean value to indicate whether an order can be cancelled. | [optional] 
**non_cancellation_reason** | **str** | The reason for the order to be non-cancelable. | [optional] 
**limit_type** | [**CancelOrderLimitType**](CancelOrderLimitType.md) |  | [optional] 
**limit_times** | **int** | The remaining cancellation quota for the merchant. A value is only returned when the nearest remaining cancellation limit is approaching, else it returns 0. | [optional] 
**cancel_reasons** | [**List[CancelReason]**](CancelReason.md) | An array of cancel order reasons JSON objects. | [optional] 

## Example

```python
from grabfood.models.check_order_cancelable_response import CheckOrderCancelableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckOrderCancelableResponse from a JSON string
check_order_cancelable_response_instance = CheckOrderCancelableResponse.from_json(json)
# print the JSON string representation of the object
print(CheckOrderCancelableResponse.to_json())

# convert the object into a dict
check_order_cancelable_response_dict = check_order_cancelable_response_instance.to_dict()
# create an instance of CheckOrderCancelableResponse from a dict
check_order_cancelable_response_from_dict = CheckOrderCancelableResponse.from_dict(check_order_cancelable_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


