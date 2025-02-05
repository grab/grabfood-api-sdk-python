# StoreHourResponse

Object contain store hour info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dine_in_hour** | [**StoreHour**](StoreHour.md) |  | [optional] 
**opening_hour** | [**StoreHour**](StoreHour.md) |  | [optional] 
**special_opening_hours** | [**List[SpecialOpeningHour]**](SpecialOpeningHour.md) | The store&#39;s special opening hours. | [optional] 

## Example

```python
from grabfood.models.store_hour_response import StoreHourResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StoreHourResponse from a JSON string
store_hour_response_instance = StoreHourResponse.from_json(json)
# print the JSON string representation of the object
print(StoreHourResponse.to_json())

# convert the object into a dict
store_hour_response_dict = store_hour_response_instance.to_dict()
# create an instance of StoreHourResponse from a dict
store_hour_response_from_dict = StoreHourResponse.from_dict(store_hour_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


