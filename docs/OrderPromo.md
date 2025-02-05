# OrderPromo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Promo code applied in the order. | [optional] 
**description** | **str** | Promo description. | [optional] 
**name** | **str** | Name of the promotion. | [optional] 
**promo_amount** | **int** | Promo amount applied in the order, in local currency. This amount is rounded into whole number. | [optional] 
**mex_funded_ratio** | **int** | The merchant&#39;s funded ratio of the promo in percentage. | [optional] 
**mex_funded_amount** | **int** | The merchant&#39;s promo fund in the minor unit. Calculated based on merchant funded ratio. | [optional] 
**targeted_price** | **int** | The subtotal of the order basket in minor unit. | [optional] 
**promo_amount_in_min** | **int** | Promo amount applied in the order in minor unit. | [optional] 

## Example

```python
from grabfood.models.order_promo import OrderPromo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderPromo from a JSON string
order_promo_instance = OrderPromo.from_json(json)
# print the JSON string representation of the object
print(OrderPromo.to_json())

# convert the object into a dict
order_promo_dict = order_promo_instance.to_dict()
# create an instance of OrderPromo from a dict
order_promo_from_dict = OrderPromo.from_dict(order_promo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


