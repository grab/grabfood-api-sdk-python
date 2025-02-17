# ServiceHours

A JSON object with serviceHours for each day of the week.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mon** | [**ServiceHour**](ServiceHour.md) |  | 
**tue** | [**ServiceHour**](ServiceHour.md) |  | 
**wed** | [**ServiceHour**](ServiceHour.md) |  | 
**thu** | [**ServiceHour**](ServiceHour.md) |  | 
**fri** | [**ServiceHour**](ServiceHour.md) |  | 
**sat** | [**ServiceHour**](ServiceHour.md) |  | 
**sun** | [**ServiceHour**](ServiceHour.md) |  | 

## Example

```python
from grabfood.models.service_hours import ServiceHours

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceHours from a JSON string
service_hours_instance = ServiceHours.from_json(json)
# print the JSON string representation of the object
print(ServiceHours.to_json())

# convert the object into a dict
service_hours_dict = service_hours_instance.to_dict()
# create an instance of ServiceHours from a dict
service_hours_from_dict = ServiceHours.from_dict(service_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


