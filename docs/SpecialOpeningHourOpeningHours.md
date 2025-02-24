# SpecialOpeningHourOpeningHours

Store special opening hour period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_period_type** | **str** | The period type for when the outlet is open. | [optional] 
**periods** | [**List[OpenPeriod]**](OpenPeriod.md) | An array of open periods. Maximum of 3 periods. | [optional] 

## Example

```python
from grabfood.models.special_opening_hour_opening_hours import SpecialOpeningHourOpeningHours

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialOpeningHourOpeningHours from a JSON string
special_opening_hour_opening_hours_instance = SpecialOpeningHourOpeningHours.from_json(json)
# print the JSON string representation of the object
print(SpecialOpeningHourOpeningHours.to_json())

# convert the object into a dict
special_opening_hour_opening_hours_dict = special_opening_hour_opening_hours_instance.to_dict()
# create an instance of SpecialOpeningHourOpeningHours from a dict
special_opening_hour_opening_hours_from_dict = SpecialOpeningHourOpeningHours.from_dict(special_opening_hour_opening_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


