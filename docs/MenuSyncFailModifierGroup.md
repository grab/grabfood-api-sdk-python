# MenuSyncFailModifierGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**errors** | **List[str]** | An array of strings of error message. | [optional] 
**modifiers** | [**List[MenuSyncFailModifier]**](MenuSyncFailModifier.md) |  | [optional] 

## Example

```python
from grabfood.models.menu_sync_fail_modifier_group import MenuSyncFailModifierGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MenuSyncFailModifierGroup from a JSON string
menu_sync_fail_modifier_group_instance = MenuSyncFailModifierGroup.from_json(json)
# print the JSON string representation of the object
print(MenuSyncFailModifierGroup.to_json())

# convert the object into a dict
menu_sync_fail_modifier_group_dict = menu_sync_fail_modifier_group_instance.to_dict()
# create an instance of MenuSyncFailModifierGroup from a dict
menu_sync_fail_modifier_group_from_dict = MenuSyncFailModifierGroup.from_dict(menu_sync_fail_modifier_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


