# ServiceHour

A JSON object serviceHour for each day. An empty JSON object indicates the menu item is not available on the day.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_period_type** | **str** | Defines the specific time period during which the menu is available  - OpenPeriod &#x3D; open only in given periods - OpenAllDay &#x3D; open 24 hours - CloseAllDay &#x3D; closed 24 hours  | 
**periods** | [**List[OpenPeriod]**](OpenPeriod.md) | An array of open periods. Only required when &#x60;openPeriodType&#x60; is **OpenPeriod** | [optional] 

## Example

```python
from grabfood.models.service_hour import ServiceHour

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceHour from a JSON string
service_hour_instance = ServiceHour.from_json(json)
# print the JSON string representation of the object
print(ServiceHour.to_json())

# convert the object into a dict
service_hour_dict = service_hour_instance.to_dict()
# create an instance of ServiceHour from a dict
service_hour_from_dict = ServiceHour.from_dict(service_hour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


