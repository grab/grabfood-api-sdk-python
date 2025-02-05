# MenuSyncFailItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The item&#39;s ID in the partner system.  | [optional] 
**errors** | **List[str]** | An array of strings of error message. | [optional] 
**modifier_groups** | [**List[MenuSyncFailModifierGroup]**](MenuSyncFailModifierGroup.md) |  | [optional] 

## Example

```python
from grabfood.models.menu_sync_fail_item import MenuSyncFailItem

# TODO update the JSON string below
json = "{}"
# create an instance of MenuSyncFailItem from a JSON string
menu_sync_fail_item_instance = MenuSyncFailItem.from_json(json)
# print the JSON string representation of the object
print(MenuSyncFailItem.to_json())

# convert the object into a dict
menu_sync_fail_item_dict = menu_sync_fail_item_instance.to_dict()
# create an instance of MenuSyncFailItem from a dict
menu_sync_fail_item_from_dict = MenuSyncFailItem.from_dict(menu_sync_fail_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


