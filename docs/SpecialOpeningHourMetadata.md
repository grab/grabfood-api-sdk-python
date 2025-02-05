# SpecialOpeningHourMetadata

Contains special opening hour info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the special opening hour. | [optional] 

## Example

```python
from grabfood.models.special_opening_hour_metadata import SpecialOpeningHourMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialOpeningHourMetadata from a JSON string
special_opening_hour_metadata_instance = SpecialOpeningHourMetadata.from_json(json)
# print the JSON string representation of the object
print(SpecialOpeningHourMetadata.to_json())

# convert the object into a dict
special_opening_hour_metadata_dict = special_opening_hour_metadata_instance.to_dict()
# create an instance of SpecialOpeningHourMetadata from a dict
special_opening_hour_metadata_from_dict = SpecialOpeningHourMetadata.from_dict(special_opening_hour_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


