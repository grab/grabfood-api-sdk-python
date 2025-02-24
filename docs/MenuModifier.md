# MenuModifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The modifier&#39;s ID that is on the partner&#39;s system. This ID should be unique. | 
**name** | **str** | The name of the modifier. | 
**name_translation** | **Dict[str, str]** | Translation of the modifier name. Only support up to 1 translated language. Refer [Menu Translation](#section/Menu-Translation). | [optional] 
**available_status** | **str** | The status for the modifier. Refer to FAQs for more details about [availableStatus](#section/Menu/What-is-availableStatus). | 
**price** | **int** | The modifier&#39;s price in minor format. Refer to FAQs for more details about [tax](#section/Menu/Is-the-menu-price-with-or-without-tax). | [optional] 
**barcode** | **str** | The barcode Number (GTIN). GTIN must be 8, 12, 13, 14 numeric digits. | [optional] 
**sequence** | **int** | The sort or display order of the modifier within the menu. | [optional] 
**advanced_pricing** | [**AdvancedPricing**](AdvancedPricing.md) |  | [optional] 

## Example

```python
from grabfood.models.menu_modifier import MenuModifier

# TODO update the JSON string below
json = "{}"
# create an instance of MenuModifier from a JSON string
menu_modifier_instance = MenuModifier.from_json(json)
# print the JSON string representation of the object
print(MenuModifier.to_json())

# convert the object into a dict
menu_modifier_dict = menu_modifier_instance.to_dict()
# create an instance of MenuModifier from a dict
menu_modifier_from_dict = MenuModifier.from_dict(menu_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


