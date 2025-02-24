# MenuSectionCategoryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The item&#39;s ID in the partner system.  | 
**name** | **str** | The name of the item. | 
**name_translation** | **Dict[str, str]** | Translation of the item name. Only support up to 1 translated language. Refer [Menu Translation](#section/Menu-Translation). | [optional] 
**available_status** | **str** | The status for the item that is in the category. Refer to FAQs for more details about [availableStatus](#section/Menu/What-is-availableStatus).  Note: In order to set an item as \&quot;UNAVAILABLE\&quot;, it is required to update both the &#x60;availableStatus&#x60; and &#x60;maxStock&#x60; fields, whereby the &#x60;maxStock&#x60; value should be set to 0.  | 
**description** | **str** | The description of the item. There is a custom length limit of 2000 for &#x60;VN&#x60;.  | [optional] 
**description_translation** | **Dict[str, str]** | Translation of the item description. Only support up to 1 translated language. Refer [Menu Translation](#section/Menu-Translation). | [optional] 
**price** | **int** | The item&#39;s price (excluding tax) in minor format. For example: 1900 means $19 with &#x60;currency.exponent&#x60; as 2. Refer to [FAQ](#section/Menu/Is-the-item-price-with-or-without-tax) for more details.  | 
**photos** | **List[str]** | An array string for the item’s image URL links. Refer to FAQs for more details about [images](#section/Menu/What-are-the-recommended-formats-for-an-item-image).  | [optional] 
**special_type** | **str** | The item&#39;s special Tag. Refer to FAQs for more details about [specialType](#section/Menu/What&#39;s-specialType).  | [optional] 
**taxable** | **bool** | **For Indonesia only.** This field allows the configuration for an item to be marked as tax applicable, and marked item would then be included in a commercial invoice to consumers as per the government&#39;s regulations.  | [optional] 
**barcode** | **str** | The barcode Number (GTIN). Max 64 allowed. GTIN must be 8, 12, 13, 14 numeric digits.  | [optional] 
**max_stock** | **int** | Available stocks under inventory for this item. Auto reduce when there is order placed for this item. Empty value implies no limit.  Note: It is necessary to set &#x60;maxStock&#x60; to 0 if the &#x60;availableStatus&#x60; of the item is \&quot;UNAVAILABLE\&quot;. Item will be set to \&quot;AVAILABLE\&quot; if &#x60;maxStock&#x60; &gt; 0.  | [optional] 
**advanced_pricing** | [**AdvancedPricing**](AdvancedPricing.md) |  | [optional] 
**purchasability** | [**Purchasability**](Purchasability.md) |  | [optional] 
**modifier_groups** | [**List[ModifierGroup]**](ModifierGroup.md) | An array of the modifierGroup JSON objects. Max 30 allowed per item. Refer to [Modifier groups](#modifier-groups) for more information. | [optional] 

## Example

```python
from grabfood.models.menu_section_category_item import MenuSectionCategoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of MenuSectionCategoryItem from a JSON string
menu_section_category_item_instance = MenuSectionCategoryItem.from_json(json)
# print the JSON string representation of the object
print(MenuSectionCategoryItem.to_json())

# convert the object into a dict
menu_section_category_item_dict = menu_section_category_item_instance.to_dict()
# create an instance of MenuSectionCategoryItem from a dict
menu_section_category_item_from_dict = MenuSectionCategoryItem.from_dict(menu_section_category_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


