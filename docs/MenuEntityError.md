# MenuEntityError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | The itemID. | [optional] 
**err_msg** | **str** | The error message. | [optional] 

## Example

```python
from grabfood.models.menu_entity_error import MenuEntityError

# TODO update the JSON string below
json = "{}"
# create an instance of MenuEntityError from a JSON string
menu_entity_error_instance = MenuEntityError.from_json(json)
# print the JSON string representation of the object
print(MenuEntityError.to_json())

# convert the object into a dict
menu_entity_error_dict = menu_entity_error_instance.to_dict()
# create an instance of MenuEntityError from a dict
menu_entity_error_from_dict = MenuEntityError.from_dict(menu_entity_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


