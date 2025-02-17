# WorkingHour

A JSON object that describes the workingHour for each day.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sun** | [**WorkingHourDay**](WorkingHourDay.md) |  | [optional] 
**mon** | [**WorkingHourDay**](WorkingHourDay.md) |  | [optional] 
**tue** | [**WorkingHourDay**](WorkingHourDay.md) |  | [optional] 
**wed** | [**WorkingHourDay**](WorkingHourDay.md) |  | [optional] 
**thu** | [**WorkingHourDay**](WorkingHourDay.md) |  | [optional] 
**fri** | [**WorkingHourDay**](WorkingHourDay.md) |  | [optional] 
**sat** | [**WorkingHourDay**](WorkingHourDay.md) |  | [optional] 

## Example

```python
from grabfood.models.working_hour import WorkingHour

# TODO update the JSON string below
json = "{}"
# create an instance of WorkingHour from a JSON string
working_hour_instance = WorkingHour.from_json(json)
# print the JSON string representation of the object
print(WorkingHour.to_json())

# convert the object into a dict
working_hour_dict = working_hour_instance.to_dict()
# create an instance of WorkingHour from a dict
working_hour_from_dict = WorkingHour.from_dict(working_hour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


