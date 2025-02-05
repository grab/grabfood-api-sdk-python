# MenuSyncFailServiceHours


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** | An array of strings of error message. | [optional] 

## Example

```python
from grabfood.models.menu_sync_fail_service_hours import MenuSyncFailServiceHours

# TODO update the JSON string below
json = "{}"
# create an instance of MenuSyncFailServiceHours from a JSON string
menu_sync_fail_service_hours_instance = MenuSyncFailServiceHours.from_json(json)
# print the JSON string representation of the object
print(MenuSyncFailServiceHours.to_json())

# convert the object into a dict
menu_sync_fail_service_hours_dict = menu_sync_fail_service_hours_instance.to_dict()
# create an instance of MenuSyncFailServiceHours from a dict
menu_sync_fail_service_hours_from_dict = MenuSyncFailServiceHours.from_dict(menu_sync_fail_service_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


