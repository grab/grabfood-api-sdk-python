# MenuSyncResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **datetime** | The Unix time the specified menu was created in GrabFood&#39;s database. | 
**updated_time** | **datetime** | The Unix time the specified menu was created in GrabFood&#39;s database. | 
**code** | **str** | The status code for this request. See [Menu sync response statuses](#section/Menu-sync-response-statuses) for more information. | 
**errors** | **List[str]** | An array of strings of error message. | [optional] 
**sections** | [**List[MenuSyncFail]**](MenuSyncFail.md) |  | [optional] 

## Example

```python
from grabfood.models.menu_sync_response import MenuSyncResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MenuSyncResponse from a JSON string
menu_sync_response_instance = MenuSyncResponse.from_json(json)
# print the JSON string representation of the object
print(MenuSyncResponse.to_json())

# convert the object into a dict
menu_sync_response_dict = menu_sync_response_instance.to_dict()
# create an instance of MenuSyncResponse from a dict
menu_sync_response_from_dict = MenuSyncResponse.from_dict(menu_sync_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


