# OrderFeatureFlags

The featureFlag JSON object containing an order's feature related information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_accepted_type** | **str** | The acceptance type for the order. Refer to FAQs for more details about [orderAcceptedType](#section/Order/How-do-I-identify-if-a-particular-order-is-auto-or-manual-acceptance).  | 
**order_type** | **str** | The type of order.  | 
**is_mex_edit_order** | **bool** | A boolean value that indicates if the order is edited.  | [optional] 

## Example

```python
from grabfood.models.order_feature_flags import OrderFeatureFlags

# TODO update the JSON string below
json = "{}"
# create an instance of OrderFeatureFlags from a JSON string
order_feature_flags_instance = OrderFeatureFlags.from_json(json)
# print the JSON string representation of the object
print(OrderFeatureFlags.to_json())

# convert the object into a dict
order_feature_flags_dict = order_feature_flags_instance.to_dict()
# create an instance of OrderFeatureFlags from a dict
order_feature_flags_from_dict = OrderFeatureFlags.from_dict(order_feature_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


