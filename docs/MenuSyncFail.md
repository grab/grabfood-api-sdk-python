# MenuSyncFail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**errors** | **List[str]** | An array of strings of error message. | [optional] 
**service_hours** | [**MenuSyncFailServiceHours**](MenuSyncFailServiceHours.md) |  | [optional] 
**categories** | [**List[MenuSyncFailCategory]**](MenuSyncFailCategory.md) |  | [optional] 

## Example

```python
from grabfood.models.menu_sync_fail import MenuSyncFail

# TODO update the JSON string below
json = "{}"
# create an instance of MenuSyncFail from a JSON string
menu_sync_fail_instance = MenuSyncFail.from_json(json)
# print the JSON string representation of the object
print(MenuSyncFail.to_json())

# convert the object into a dict
menu_sync_fail_dict = menu_sync_fail_instance.to_dict()
# create an instance of MenuSyncFail from a dict
menu_sync_fail_from_dict = MenuSyncFail.from_dict(menu_sync_fail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


