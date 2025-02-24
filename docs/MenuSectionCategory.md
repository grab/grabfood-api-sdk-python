# MenuSectionCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The category&#39;s ID that is on the partner system. This ID should be unique with a min length of 1 and max of 64. | 
**name** | **str** | The name of the category. | 
**name_translation** | **Dict[str, str]** | Translation of the category name. Only support up to 1 translated language. Refer [Menu Translation](#section/Menu-Translation). | [optional] 
**available_status** | **str** | The status for the category. Refer to FAQs for more details about [availableStatus](#section/Menu/What-is-availableStatus). | 
**items** | [**List[MenuSectionCategoryItem]**](MenuSectionCategoryItem.md) | An array of item JSON objects. Max 300 allowed per category. Refer to [Items](#items) for more information. | 

## Example

```python
from grabfood.models.menu_section_category import MenuSectionCategory

# TODO update the JSON string below
json = "{}"
# create an instance of MenuSectionCategory from a JSON string
menu_section_category_instance = MenuSectionCategory.from_json(json)
# print the JSON string representation of the object
print(MenuSectionCategory.to_json())

# convert the object into a dict
menu_section_category_dict = menu_section_category_instance.to_dict()
# create an instance of MenuSectionCategory from a dict
menu_section_category_from_dict = MenuSectionCategory.from_dict(menu_section_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


