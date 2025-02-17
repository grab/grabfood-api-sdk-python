# GetMenuNewResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | [optional] 
**partner_merchant_id** | **str** | The merchant&#39;s ID that is on the partner&#39;s database. | [optional] 
**currency** | [**Currency**](Currency.md) |  | 
**selling_times** | [**List[SellingTime]**](SellingTime.md) | An array of sellingTimes JSON objects. Max 20 allowed. Refer to [Selling Times](#selling-times) for more information. | 
**categories** | [**List[MenuCategory]**](MenuCategory.md) | An array of category JSON objects. Max 100 allowed. Refer to [Categories](#categories) for more information. | 

## Example

```python
from grabfood.models.get_menu_new_response import GetMenuNewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMenuNewResponse from a JSON string
get_menu_new_response_instance = GetMenuNewResponse.from_json(json)
# print the JSON string representation of the object
print(GetMenuNewResponse.to_json())

# convert the object into a dict
get_menu_new_response_dict = get_menu_new_response_instance.to_dict()
# create an instance of GetMenuNewResponse from a dict
get_menu_new_response_from_dict = GetMenuNewResponse.from_dict(get_menu_new_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


