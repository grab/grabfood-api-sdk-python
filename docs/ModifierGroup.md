# ModifierGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The modifier group&#39;s ID that is on the partner system. This ID should be unique. | 
**name** | **str** | The name of the modifier group. | 
**name_translation** | **Dict[str, str]** | Translation of the modifier group name. Only support up to 1 translated language. Refer [Menu Translation](#section/Menu-Translation). | [optional] 
**available_status** | **str** | The status for the modifier group.   &gt; The item may be marked as &#x60;\&quot;UNAVAILABLE\&quot;&#x60; if no available modifier to be selected within the required modifier group where &#x60;\&quot;selectionRangeMin\&quot;: 1&#x60;.  | 
**selection_range_min** | **int** | The minimum quantity of the modifiers to be selected. Refer to FAQs for more details about [selection range](#section/Menu/What-does-the-selection-range-do). | [optional] 
**selection_range_max** | **int** | The maximum quantity of the modifiers to be selected. Refer to FAQs for more details about [selection range](#section/Menu/What-does-the-selection-range-do). | 
**sequence** | **int** | The sort or display order of the modifier group within the menu. | [optional] 
**modifiers** | [**List[MenuModifier]**](MenuModifier.md) | An array of modifier JSON objects. Max 100 per modifierGroup. Refer to [Modifiers](#modifiers) for more information. | [optional] 

## Example

```python
from grabfood.models.modifier_group import ModifierGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierGroup from a JSON string
modifier_group_instance = ModifierGroup.from_json(json)
# print the JSON string representation of the object
print(ModifierGroup.to_json())

# convert the object into a dict
modifier_group_dict = modifier_group_instance.to_dict()
# create an instance of ModifierGroup from a dict
modifier_group_from_dict = ModifierGroup.from_dict(modifier_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


