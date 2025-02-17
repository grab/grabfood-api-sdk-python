# UpdateDineInHourRequest

Object contains store dine-in hours.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dine_in_hour** | [**StoreHour**](StoreHour.md) |  | 

## Example

```python
from grabfood.models.update_dine_in_hour_request import UpdateDineInHourRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDineInHourRequest from a JSON string
update_dine_in_hour_request_instance = UpdateDineInHourRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDineInHourRequest.to_json())

# convert the object into a dict
update_dine_in_hour_request_dict = update_dine_in_hour_request_instance.to_dict()
# create an instance of UpdateDineInHourRequest from a dict
update_dine_in_hour_request_from_dict = UpdateDineInHourRequest.from_dict(update_dine_in_hour_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


