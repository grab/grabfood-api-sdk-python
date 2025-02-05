# UpdateDineInHourResponse

Object contain update store dine-in hour response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_reasons** | **List[str]** | Error message when updating store dine-in hour. &#x60;null&#x60; indicates no error. | [optional] 

## Example

```python
from grabfood.models.update_dine_in_hour_response import UpdateDineInHourResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDineInHourResponse from a JSON string
update_dine_in_hour_response_instance = UpdateDineInHourResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateDineInHourResponse.to_json())

# convert the object into a dict
update_dine_in_hour_response_dict = update_dine_in_hour_response_instance.to_dict()
# create an instance of UpdateDineInHourResponse from a dict
update_dine_in_hour_response_from_dict = UpdateDineInHourResponse.from_dict(update_dine_in_hour_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


