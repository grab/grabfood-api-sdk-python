# PosPriceDetails

A JSON object containing order's price in the minor unit format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtotal** | **int** | Total item and modifier price  in minor units and tax-inclusive. | [optional] 
**tax** | **int** | Total tax in the minor unit. &#x60;&#x60;&#x60; Formula Tax &#x3D; total item/modifier tax  | [optional] 
**merchant_charge_fee_in_min** | **int** | Any additional fee charged by the merchant  in minor units and tax-inclusive, which is 100% paid out to the merchant. Eg. service charge | [optional] 
**deposit_amount_in_min** | **int** | This field represents the reservation depositAmount, which is the amount paid upfront by the diner during the reservation process. It can be applied towards the final payment when the order is completed. It’s in minor units and tax-inclusive. | [optional] 
**offline_pos_discount_in_min** | **int** | Offline discount that is provided to the diner in minor units and tax-inclusive. | [optional] 
**bill_rounding_in_min** | **int** | The rounding amount in minor units.  &#x60;&#x60;&#x60; Round down should be in negative value Round up should be in positive value &#x60;&#x60;&#x60;  | [optional] 
**eater_payment** | **int** | The total bill value in minor units and tax-inclusive. &#x60;&#x60;&#x60; Formula:   eaterPayment &#x3D;   + subtotal   + merchantChargeFeeInMin   - depositAmountInMin   - offlinePOSDiscountInMin  | [optional] 

## Example

```python
from grabfood.models.pos_price_details import PosPriceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PosPriceDetails from a JSON string
pos_price_details_instance = PosPriceDetails.from_json(json)
# print the JSON string representation of the object
print(PosPriceDetails.to_json())

# convert the object into a dict
pos_price_details_dict = pos_price_details_instance.to_dict()
# create an instance of PosPriceDetails from a dict
pos_price_details_from_dict = PosPriceDetails.from_dict(pos_price_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


