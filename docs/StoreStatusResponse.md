# StoreStatusResponse

Object contains store status info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_reason** | **str** | The code of store close reason. Blank indicates store is currently open. | 
**is_in_special_opening_hour_range** | **bool** | Indicate whether the store is in special opening hour range. | 
**is_open** | **bool** | Indicate whether the store is open. | 

## Example

```python
from grabfood.models.store_status_response import StoreStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StoreStatusResponse from a JSON string
store_status_response_instance = StoreStatusResponse.from_json(json)
# print the JSON string representation of the object
print(StoreStatusResponse.to_json())

# convert the object into a dict
store_status_response_dict = store_status_response_instance.to_dict()
# create an instance of StoreStatusResponse from a dict
store_status_response_from_dict = StoreStatusResponse.from_dict(store_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


