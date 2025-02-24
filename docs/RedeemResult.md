# RedeemResult

A JSON object containing dine-in voucher details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | To indicate whether the dine-in voucher redemption succeeded. | [optional] 
**code** | **str** | The code for the reason of failed redemption. Empty if the &#x60;success&#x60; is true.  * &#x60;VOUCHER_REDEEMED&#x60; - The voucher has already been redeemed. * &#x60;INVALID_STATE&#x60; - The current status of voucher is EXPIRED or REFUNDED. * &#x60;REDEEM_FAILED&#x60; - Internal service error. * &#x60;INVALID_MERCHANT&#x60; - Voucher not applicable for this merchant. * &#x60;INVALID_ID&#x60; - Invalid certificateID.  | [optional] 

## Example

```python
from grabfood.models.redeem_result import RedeemResult

# TODO update the JSON string below
json = "{}"
# create an instance of RedeemResult from a JSON string
redeem_result_instance = RedeemResult.from_json(json)
# print the JSON string representation of the object
print(RedeemResult.to_json())

# convert the object into a dict
redeem_result_dict = redeem_result_instance.to_dict()
# create an instance of RedeemResult from a dict
redeem_result_from_dict = RedeemResult.from_dict(redeem_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


