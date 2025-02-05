# GetMenuOldResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | [optional] 
**partner_merchant_id** | **str** | The merchant&#39;s ID that is on the partner&#39;s database. | [optional] 
**currency** | [**Currency**](Currency.md) |  | 
**sections** | [**List[MenuSection]**](MenuSection.md) | An array of section JSON objects. Max 7 allowed. Refer to [Sections](#sections) for more information. | 

## Example

```python
from grabfood.models.get_menu_old_response import GetMenuOldResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMenuOldResponse from a JSON string
get_menu_old_response_instance = GetMenuOldResponse.from_json(json)
# print the JSON string representation of the object
print(GetMenuOldResponse.to_json())

# convert the object into a dict
get_menu_old_response_dict = get_menu_old_response_instance.to_dict()
# create an instance of GetMenuOldResponse from a dict
get_menu_old_response_from_dict = GetMenuOldResponse.from_dict(get_menu_old_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


