# SpecialOpeningHour


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | The start date of store special opening hours. | [optional] 
**end_date** | **str** | The end date of store special opening hours. | [optional] 
**metadata** | [**SpecialOpeningHourMetadata**](SpecialOpeningHourMetadata.md) |  | [optional] 
**opening_hours** | [**SpecialOpeningHourOpeningHours**](SpecialOpeningHourOpeningHours.md) |  | [optional] 

## Example

```python
from grabfood.models.special_opening_hour import SpecialOpeningHour

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialOpeningHour from a JSON string
special_opening_hour_instance = SpecialOpeningHour.from_json(json)
# print the JSON string representation of the object
print(SpecialOpeningHour.to_json())

# convert the object into a dict
special_opening_hour_dict = special_opening_hour_instance.to_dict()
# create an instance of SpecialOpeningHour from a dict
special_opening_hour_from_dict = SpecialOpeningHour.from_dict(special_opening_hour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


