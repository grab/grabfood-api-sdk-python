# UpdateSpecialHourResponse

Object contain update store special hour response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_reasons** | **List[str]** | Error message when updating store delivery hour. &#x60;null&#x60; indicates no error. | [optional] 
**order_count** | **int** | Total active order for the day. | 
**scheduled_order_count** | **int** | Total scheduled order during store close period. | 
**close_immediately** | **bool** | Indicate the store status after updating special hours. | 

## Example

```python
from grabfood.models.update_special_hour_response import UpdateSpecialHourResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSpecialHourResponse from a JSON string
update_special_hour_response_instance = UpdateSpecialHourResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateSpecialHourResponse.to_json())

# convert the object into a dict
update_special_hour_response_dict = update_special_hour_response_instance.to_dict()
# create an instance of UpdateSpecialHourResponse from a dict
update_special_hour_response_from_dict = UpdateSpecialHourResponse.from_dict(update_special_hour_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


