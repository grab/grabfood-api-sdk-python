# MerchantEarning

A JSON object reflects the real money the merchant receives. Only applicable for Dine out STO case. `null` if not applicable. Only present in submitOrder webhook. Not present in [ListOrder](#tag/list-order/operation/list-orders) response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revenue** | **int** | The revenue of merchant should receive. revenue &#x3D; price.eaterpayment - mexfunddiscount | [optional] 
**net_earning** | **int** | The netEarning of merchant should receive. netEarning &#x3D; revenue - commission | [optional] 
**mex_fund_discount** | **int** | The mexFundDiscount that user applied from grab app in this payment | [optional] 
**commission** | **int** | The commission that grab need charge from this pay merchant transaction. | [optional] 

## Example

```python
from grabfood.models.merchant_earning import MerchantEarning

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantEarning from a JSON string
merchant_earning_instance = MerchantEarning.from_json(json)
# print the JSON string representation of the object
print(MerchantEarning.to_json())

# convert the object into a dict
merchant_earning_dict = merchant_earning_instance.to_dict()
# create an instance of MerchantEarning from a dict
merchant_earning_from_dict = MerchantEarning.from_dict(merchant_earning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


