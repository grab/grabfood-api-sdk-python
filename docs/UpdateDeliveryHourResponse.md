# UpdateDeliveryHourResponse

Object contain update store delivery hour response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_reasons** | **List[str]** | Error message when updating store delivery hour. &#x60;null&#x60; indicates no error. | [optional] 
**order_count** | **int** | Total active order for the day. | 
**scheduled_order_count** | **int** | Total scheduled order during store close period. | 
**close_immediately** | **bool** | Indicate the store status after updating delivery hours. | 

## Example

```python
from grabfood.models.update_delivery_hour_response import UpdateDeliveryHourResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDeliveryHourResponse from a JSON string
update_delivery_hour_response_instance = UpdateDeliveryHourResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateDeliveryHourResponse.to_json())

# convert the object into a dict
update_delivery_hour_response_dict = update_delivery_hour_response_instance.to_dict()
# create an instance of UpdateDeliveryHourResponse from a dict
update_delivery_hour_response_from_dict = UpdateDeliveryHourResponse.from_dict(update_delivery_hour_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


