# RedeemDineInVoucherRequest

Dine in voucher redemption 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_id** | **str** | This certificateID is decoded from scanning the QR code, and 1:1 mapping with &#x60;voucherCode&#x60;. | 
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | 

## Example

```python
from grabfood.models.redeem_dine_in_voucher_request import RedeemDineInVoucherRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedeemDineInVoucherRequest from a JSON string
redeem_dine_in_voucher_request_instance = RedeemDineInVoucherRequest.from_json(json)
# print the JSON string representation of the object
print(RedeemDineInVoucherRequest.to_json())

# convert the object into a dict
redeem_dine_in_voucher_request_dict = redeem_dine_in_voucher_request_instance.to_dict()
# create an instance of RedeemDineInVoucherRequest from a dict
redeem_dine_in_voucher_request_from_dict = RedeemDineInVoucherRequest.from_dict(redeem_dine_in_voucher_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


