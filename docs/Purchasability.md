# Purchasability

Purchasability is set to true by default for all service type, unless it is explicitly set to false. Modifier will reuse it’s item’s purchasability. Refer [Service Based Menu](#section/Service-Based-Menu). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_on_demand_grab_app** | **bool** |  | [optional] 
**delivery_scheduled_grab_app** | **bool** |  | [optional] 
**self_pick_up_on_demand_grab_app** | **bool** |  | [optional] 
**dine_in_on_demand_grab_app** | **bool** |  | [optional] 
**delivery_on_demand_store_front** | **bool** |  | [optional] 
**delivery_scheduled_store_front** | **bool** |  | [optional] 
**self_pick_up_on_demand_store_front** | **bool** |  | [optional] 

## Example

```python
from grabfood.models.purchasability import Purchasability

# TODO update the JSON string below
json = "{}"
# create an instance of Purchasability from a JSON string
purchasability_instance = Purchasability.from_json(json)
# print the JSON string representation of the object
print(Purchasability.to_json())

# convert the object into a dict
purchasability_dict = purchasability_instance.to_dict()
# create an instance of Purchasability from a dict
purchasability_from_dict = Purchasability.from_dict(purchasability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


