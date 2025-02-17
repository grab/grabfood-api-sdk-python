# MenuSyncFailCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The category&#39;s ID that is on the partner system. This ID should be unique with a min length of 1 and max of 64. | [optional] 
**errors** | **List[str]** | An array of strings of error message. | [optional] 
**items** | [**List[MenuSyncFailItem]**](MenuSyncFailItem.md) | An array of item JSON objects. Max 300 allowed per category. Refer to [Items](#items) for more information. | [optional] 

## Example

```python
from grabfood.models.menu_sync_fail_category import MenuSyncFailCategory

# TODO update the JSON string below
json = "{}"
# create an instance of MenuSyncFailCategory from a JSON string
menu_sync_fail_category_instance = MenuSyncFailCategory.from_json(json)
# print the JSON string representation of the object
print(MenuSyncFailCategory.to_json())

# convert the object into a dict
menu_sync_fail_category_dict = menu_sync_fail_category_instance.to_dict()
# create an instance of MenuSyncFailCategory from a dict
menu_sync_fail_category_from_dict = MenuSyncFailCategory.from_dict(menu_sync_fail_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


