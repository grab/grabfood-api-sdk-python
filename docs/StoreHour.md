# StoreHour

A JSON object that describes the store hour for each day.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mon** | [**List[OpenPeriod]**](OpenPeriod.md) | An array of open periods. Maximum of 3 periods. Blank indicates store close. | 
**tue** | [**List[OpenPeriod]**](OpenPeriod.md) | An array of open periods. Maximum of 3 periods. Blank indicates store close. | 
**wed** | [**List[OpenPeriod]**](OpenPeriod.md) | An array of open periods. Maximum of 3 periods. Blank indicates store close. | 
**thu** | [**List[OpenPeriod]**](OpenPeriod.md) | An array of open periods. Maximum of 3 periods. Blank indicates store close. | 
**fri** | [**List[OpenPeriod]**](OpenPeriod.md) | An array of open periods. Maximum of 3 periods. Blank indicates store close. | 
**sat** | [**List[OpenPeriod]**](OpenPeriod.md) | An array of open periods. Maximum of 3 periods. Blank indicates store close. | 
**sun** | [**List[OpenPeriod]**](OpenPeriod.md) | An array of open periods. Maximum of 3 periods. Blank indicates store close. | 

## Example

```python
from grabfood.models.store_hour import StoreHour

# TODO update the JSON string below
json = "{}"
# create an instance of StoreHour from a JSON string
store_hour_instance = StoreHour.from_json(json)
# print the JSON string representation of the object
print(StoreHour.to_json())

# convert the object into a dict
store_hour_dict = store_hour_instance.to_dict()
# create an instance of StoreHour from a dict
store_hour_from_dict = StoreHour.from_dict(store_hour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


