# BatchUpdateMenuItem

Information about the GrabFood client updating their food menu. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | 
**var_field** | **str** | The record type that you want to update. | 
**menu_entities** | [**List[MenuEntity]**](MenuEntity.md) | The items in an array of JSON Object.  | [optional] 

## Example

```python
from grabfood.models.batch_update_menu_item import BatchUpdateMenuItem

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdateMenuItem from a JSON string
batch_update_menu_item_instance = BatchUpdateMenuItem.from_json(json)
# print the JSON string representation of the object
print(BatchUpdateMenuItem.to_json())

# convert the object into a dict
batch_update_menu_item_dict = batch_update_menu_item_instance.to_dict()
# create an instance of BatchUpdateMenuItem from a dict
batch_update_menu_item_from_dict = BatchUpdateMenuItem.from_dict(batch_update_menu_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


