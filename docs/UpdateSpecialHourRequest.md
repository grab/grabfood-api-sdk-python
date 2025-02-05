# UpdateSpecialHourRequest

Object contains store special hours.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**special_opening_hours** | [**List[SpecialOpeningHour]**](SpecialOpeningHour.md) | An array of objects contain store special hours. Max. 3 array elements. | 

## Example

```python
from grabfood.models.update_special_hour_request import UpdateSpecialHourRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSpecialHourRequest from a JSON string
update_special_hour_request_instance = UpdateSpecialHourRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSpecialHourRequest.to_json())

# convert the object into a dict
update_special_hour_request_dict = update_special_hour_request_instance.to_dict()
# create an instance of UpdateSpecialHourRequest from a dict
update_special_hour_request_from_dict = UpdateSpecialHourRequest.from_dict(update_special_hour_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


