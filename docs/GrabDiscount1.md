# GrabDiscount1

A JSON object reflects the discount in grab app paybill flow that eater has used. Only applicable for Dine out STO case. `null` if not applicable. Only present in submitOrder webhook. Not present in [ListOrder](#tag/list-order/operation/list-orders) response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | discount code. | [optional] 
**id** | **str** | discount id. | [optional] 
**name** | **str** | discount name. | [optional] 
**deduct_amount_in_min** | **int** | The total discount amount in minor unit. | [optional] 
**level** | **str** | discount level, eg, order / item level. | [optional] 
**type** | **str** | discount type, eg, Promo / DineOutVoucher / DineOutDiscount. | [optional] 
**mex_funded_amount_in_min** | **int** | The mexFundDiscount in minor unit. | [optional] 
**applied_item_ids** | **List[str]** | An array of item IDs that get discount under this grabDiscount. &#x60;null&#x60; if no item applied in this grabDiscount. | [optional] 

## Example

```python
from grabfood.models.grab_discount1 import GrabDiscount1

# TODO update the JSON string below
json = "{}"
# create an instance of GrabDiscount1 from a JSON string
grab_discount1_instance = GrabDiscount1.from_json(json)
# print the JSON string representation of the object
print(GrabDiscount1.to_json())

# convert the object into a dict
grab_discount1_dict = grab_discount1_instance.to_dict()
# create an instance of GrabDiscount1 from a dict
grab_discount1_from_dict = GrabDiscount1.from_dict(grab_discount1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


