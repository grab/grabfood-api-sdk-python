# UpdatePurchasability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Available service type. | [optional] 
**purchasable** | **bool** |  | [optional] 

## Example

```python
from grabfood.models.update_purchasability import UpdatePurchasability

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePurchasability from a JSON string
update_purchasability_instance = UpdatePurchasability.from_json(json)
# print the JSON string representation of the object
print(UpdatePurchasability.to_json())

# convert the object into a dict
update_purchasability_dict = update_purchasability_instance.to_dict()
# create an instance of UpdatePurchasability from a dict
update_purchasability_from_dict = UpdatePurchasability.from_dict(update_purchasability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


