# WorkingHourDay

A JSON object for workingHour for a day.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periods** | [**List[OpenPeriod]**](OpenPeriod.md) | An array of open periods. &#x60;null&#x60; if the campaign period is closed all day. | [optional] 

## Example

```python
from grabfood.models.working_hour_day import WorkingHourDay

# TODO update the JSON string below
json = "{}"
# create an instance of WorkingHourDay from a JSON string
working_hour_day_instance = WorkingHourDay.from_json(json)
# print the JSON string representation of the object
print(WorkingHourDay.to_json())

# convert the object into a dict
working_hour_day_dict = working_hour_day_instance.to_dict()
# create an instance of WorkingHourDay from a dict
working_hour_day_from_dict = WorkingHourDay.from_dict(working_hour_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


