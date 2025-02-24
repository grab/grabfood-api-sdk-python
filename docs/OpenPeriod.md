# OpenPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** | The open start time in 24h format. Local time format is expected. | 
**end_time** | **str** | The open end time in 24h format. Local time format is expected. | 

## Example

```python
from grabfood.models.open_period import OpenPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPeriod from a JSON string
open_period_instance = OpenPeriod.from_json(json)
# print the JSON string representation of the object
print(OpenPeriod.to_json())

# convert the object into a dict
open_period_dict = open_period_instance.to_dict()
# create an instance of OpenPeriod from a dict
open_period_from_dict = OpenPeriod.from_dict(open_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


