# MenuSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The section&#39;s ID in the partner system.  | 
**name** | **str** | The name of the section. | 
**service_hours** | [**ServiceHours**](ServiceHours.md) |  | 
**categories** | [**List[MenuSectionCategory]**](MenuSectionCategory.md) | An array of category JSON objects. Max 100 allowed per section. Refer to [Categories](#categories) for more information. | 

## Example

```python
from grabfood.models.menu_section import MenuSection

# TODO update the JSON string below
json = "{}"
# create an instance of MenuSection from a JSON string
menu_section_instance = MenuSection.from_json(json)
# print the JSON string representation of the object
print(MenuSection.to_json())

# convert the object into a dict
menu_section_dict = menu_section_instance.to_dict()
# create an instance of MenuSection from a dict
menu_section_from_dict = MenuSection.from_dict(menu_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


