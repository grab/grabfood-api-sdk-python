# PauseStoreRequest

This request pauses a store temporarily for (30 minutes/1 hour/24 hours) or unpauses a store on GrabFood. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | 
**is_pause** | **bool** | Boolean value to pause or unpause store. | 
**duration** | **str** | The duration to pause the store. Only required when &#x60;isPause&#x3D;true&#x60;. | [optional] 

## Example

```python
from grabfood.models.pause_store_request import PauseStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PauseStoreRequest from a JSON string
pause_store_request_instance = PauseStoreRequest.from_json(json)
# print the JSON string representation of the object
print(PauseStoreRequest.to_json())

# convert the object into a dict
pause_store_request_dict = pause_store_request_instance.to_dict()
# create an instance of PauseStoreRequest from a dict
pause_store_request_from_dict = PauseStoreRequest.from_dict(pause_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


