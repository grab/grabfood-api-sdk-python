# AdvancedPricing

Price configuration (in minor unit) for different service, order type and channel combination. If a service type does not have a specified price, it will utilize the default price of the item. Refer [Service Based Menu](#section/Service-Based-Menu). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_on_demand_grab_app** | **int** | Service type: &#x60;Delivery&#x60;, Order type: &#x60;Instant&#x60;, Channel: &#x60;Grab App&#x60;  | [optional] 
**delivery_scheduled_grab_app** | **int** | Service type: &#x60;Delivery&#x60;, Order type: &#x60;Scheduled&#x60;, Channel: &#x60;Grab App&#x60;  | [optional] 
**self_pick_up_on_demand_grab_app** | **int** | Service type: &#x60;Self Pick Up&#x60;, Order type: &#x60;Instant&#x60;, Channel: &#x60;Grab App&#x60;  | [optional] 
**dine_in_on_demand_grab_app** | **int** | Service type: &#x60;Dine In&#x60;, Order type: &#x60;Instant&#x60;, Channel: &#x60;Grab App&#x60;  | [optional] 
**delivery_on_demand_store_front** | **int** | Service type: &#x60;Delivery&#x60;, Order type: &#x60;Instant&#x60;, Channel: &#x60;Store Front&#x60;  | [optional] 
**delivery_scheduled_store_front** | **int** | Service type: &#x60;Delivery&#x60;, Order type: &#x60;Scheduled&#x60;, Channel: &#x60;Store Front&#x60;  | [optional] 
**self_pick_up_on_demand_store_front** | **int** | Service type: &#x60;Self Pick Up&#x60;, Order type: &#x60;Instant&#x60;, Channel: &#x60;Store Front&#x60;  | [optional] 

## Example

```python
from grabfood.models.advanced_pricing import AdvancedPricing

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedPricing from a JSON string
advanced_pricing_instance = AdvancedPricing.from_json(json)
# print the JSON string representation of the object
print(AdvancedPricing.to_json())

# convert the object into a dict
advanced_pricing_dict = advanced_pricing_instance.to_dict()
# create an instance of AdvancedPricing from a dict
advanced_pricing_from_dict = AdvancedPricing.from_dict(advanced_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


