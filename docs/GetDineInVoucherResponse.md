# GetDineInVoucherResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_id** | **str** | This certificateID is decoded from scanning the QR code, and 1:1 mapping with &#x60;voucherCode&#x60;. | [optional] 
**voucher_code** | **str** | A short code for the dine-in voucher purchased by the user. | [optional] 
**voucher** | [**Voucher**](Voucher.md) |  | [optional] 
**voucher_status** | **str** | The status of the dine-in voucher purchased. Only active voucher is eligible for redemption. | [optional] 
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | [optional] 
**campaign_id** | **str** | The dine-in voucher campaign&#39;s ID in GrabFood&#39;s database. | [optional] 

## Example

```python
from grabfood.models.get_dine_in_voucher_response import GetDineInVoucherResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDineInVoucherResponse from a JSON string
get_dine_in_voucher_response_instance = GetDineInVoucherResponse.from_json(json)
# print the JSON string representation of the object
print(GetDineInVoucherResponse.to_json())

# convert the object into a dict
get_dine_in_voucher_response_dict = get_dine_in_voucher_response_instance.to_dict()
# create an instance of GetDineInVoucherResponse from a dict
get_dine_in_voucher_response_from_dict = GetDineInVoucherResponse.from_dict(get_dine_in_voucher_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


