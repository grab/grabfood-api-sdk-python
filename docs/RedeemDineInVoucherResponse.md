# RedeemDineInVoucherResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_id** | **str** | This certificateID is decoded from scanning the QR code, and 1:1 mapping with &#x60;voucherCode&#x60;. | [optional] 
**voucher_code** | **str** | A short code for the dine-in voucher purchased by the user. | [optional] 
**voucher** | [**Voucher**](Voucher.md) |  | [optional] 
**redeem_result** | [**RedeemResult**](RedeemResult.md) |  | [optional] 
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | [optional] 
**campaign_id** | **str** | The dine-in voucher campaign&#39;s ID in GrabFood&#39;s database. | [optional] 

## Example

```python
from grabfood.models.redeem_dine_in_voucher_response import RedeemDineInVoucherResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RedeemDineInVoucherResponse from a JSON string
redeem_dine_in_voucher_response_instance = RedeemDineInVoucherResponse.from_json(json)
# print the JSON string representation of the object
print(RedeemDineInVoucherResponse.to_json())

# convert the object into a dict
redeem_dine_in_voucher_response_dict = redeem_dine_in_voucher_response_instance.to_dict()
# create an instance of RedeemDineInVoucherResponse from a dict
redeem_dine_in_voucher_response_from_dict = RedeemDineInVoucherResponse.from_dict(redeem_dine_in_voucher_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


