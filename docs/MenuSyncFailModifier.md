# MenuSyncFailModifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**errors** | **List[str]** | An array of strings of error message. | [optional] 

## Example

```python
from grabfood.models.menu_sync_fail_modifier import MenuSyncFailModifier

# TODO update the JSON string below
json = "{}"
# create an instance of MenuSyncFailModifier from a JSON string
menu_sync_fail_modifier_instance = MenuSyncFailModifier.from_json(json)
# print the JSON string representation of the object
print(MenuSyncFailModifier.to_json())

# convert the object into a dict
menu_sync_fail_modifier_dict = menu_sync_fail_modifier_instance.to_dict()
# create an instance of MenuSyncFailModifier from a dict
menu_sync_fail_modifier_from_dict = MenuSyncFailModifier.from_dict(menu_sync_fail_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


