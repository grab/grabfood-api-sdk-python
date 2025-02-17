# OrderPrice

A JSON object containing order's price in the minor unit format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtotal** | **int** | Total item and modifier price (tax-inclusive) in the minor unit. &#x60;&#x60;&#x60; subtotal &#x3D; Sum of all (item price * quantity) | 2550*1&#x3D;2550  | 
**tax** | **int** | GrabFood&#39;s tax in the minor unit. Refer to FAQs for more details about [tax](#section/Order/How-is-tax-calculated). &#x60;&#x60;&#x60; tax &#x3D; (subtotal + merchantChargeFee - merchantFundPromo) * Tax / (1+Tax) | (2550-475)*0.06/1.06&#x3D;117  | [optional] 
**merchant_charge_fee** | **int** | Any additional fee charged by merchant (tax-inclusive), which is 100% paid out to the merchant. Eg. Takeaway, packaging costs, dine-in charge.  | [optional] 
**grab_fund_promo** | **int** | GrabFood&#39;s promo fund in the minor unit. Calculated based on funded ratio. Only present when &#x60;paymentType:CASH&#x60; or &#x60;orderType:DeliveredByRestaurant&#x60;. Otherwise, it will be set to &#x60;0&#x60;. | [optional] 
**merchant_fund_promo** | **int** | The merchant&#39;s promo fund in the minor unit. Calculated based on funded ratio. | [optional] 
**basket_promo** | **int** | The total amount promo applied to the basket items only (item level/order level) in the minor unit, excluding delivery fee. Only present when &#x60;paymentType: CASH&#x60; or &#x60;orderType: DeliveredByRestaurant&#x60;. Otherwise, it will be set to &#x60;0&#x60;.  &#x60;&#x60;&#x60; basketPromo &#x3D; (grabFundPromo + merchantFundPromo) | 300 + 475 &#x3D; 775  | [optional] 
**delivery_fee** | **int** | The delivery fee in the minor unit. Only present when &#x60;paymentType:CASH&#x60; or &#x60;orderType:DeliveredByRestaurant&#x60;. Otherwise, it will be set to &#x60;0&#x60;. | [optional] 
**small_order_fee** | **int** | The fee charged by GrabFood for order that does not meet a certain minimum order value. Only present when &#x60;paymentType:CASH&#x60; and &#x60;orderType:DeliveredByRestaurant&#x60;. | [optional] 
**eater_payment** | **int** | The total amount paid by the consumer in the minor unit, excluding some additional fees charged by GrabFood. Only present when &#x60;paymentType:CASH&#x60; or &#x60;orderType:DeliveredByRestaurant&#x60;. Otherwise, it will be set to &#x60;0&#x60;.  &#x60;&#x60;&#x60; eaterPayment &#x3D; (subtotal + merchantChargeFee + deliveryFee) - (sum of all promo) | (2550+400)-775&#x3D;2175  | [optional] 

## Example

```python
from grabfood.models.order_price import OrderPrice

# TODO update the JSON string below
json = "{}"
# create an instance of OrderPrice from a JSON string
order_price_instance = OrderPrice.from_json(json)
# print the JSON string representation of the object
print(OrderPrice.to_json())

# convert the object into a dict
order_price_dict = order_price_instance.to_dict()
# create an instance of OrderPrice from a dict
order_price_from_dict = OrderPrice.from_dict(order_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


