# UpdateAdvancedPricing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Available service type. | [optional] 
**price** | **int** | Price in minor unit. | [optional] 

## Example

```python
from grabfood.models.update_advanced_pricing import UpdateAdvancedPricing

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdvancedPricing from a JSON string
update_advanced_pricing_instance = UpdateAdvancedPricing.from_json(json)
# print the JSON string representation of the object
print(UpdateAdvancedPricing.to_json())

# convert the object into a dict
update_advanced_pricing_dict = update_advanced_pricing_instance.to_dict()
# create an instance of UpdateAdvancedPricing from a dict
update_advanced_pricing_from_dict = UpdateAdvancedPricing.from_dict(update_advanced_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


