# MenuCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The category&#39;s ID that is on the partner system. This ID should be unique. | 
**name** | **str** | The name of the category. | 
**name_translation** | **Dict[str, str]** | Translation of the category name. Only support up to 1 translated language. Refer [Menu Translation](#section/Menu-Translation). | [optional] 
**available_status** | **str** | The status for the category. Refer to FAQs for more details about [availableStatus](#section/Menu/What-is-availableStatus). | 
**selling_time_id** | **str** | The selling time&#39;s ID for the category. All items within the category will apply the same selling time unless there is another selling time specified for the item. | 
**sequence** | **int** | The sort or display order of the category within the menu. | [optional] 
**items** | [**List[MenuItem]**](MenuItem.md) | An array of item JSON objects. Max 300 allowed per category. Refer to [Items](#items) for more information. | 

## Example

```python
from grabfood.models.menu_category import MenuCategory

# TODO update the JSON string below
json = "{}"
# create an instance of MenuCategory from a JSON string
menu_category_instance = MenuCategory.from_json(json)
# print the JSON string representation of the object
print(MenuCategory.to_json())

# convert the object into a dict
menu_category_dict = menu_category_instance.to_dict()
# create an instance of MenuCategory from a dict
menu_category_from_dict = MenuCategory.from_dict(menu_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


