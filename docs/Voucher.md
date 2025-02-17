# Voucher

A JSON object containing dine-in voucher details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the voucher. | [optional] 
**discounted_price** | **str** | The amount paid after discount is applied in local currency. | [optional] 
**original_price** | **str** | The original amount before discount is applied in local currency. | [optional] 
**description_info** | [**VoucherDescriptionInfo**](VoucherDescriptionInfo.md) |  | [optional] 
**voucher_type** | **str** | The type of the dine-in voucher. | [optional] 

## Example

```python
from grabfood.models.voucher import Voucher

# TODO update the JSON string below
json = "{}"
# create an instance of Voucher from a JSON string
voucher_instance = Voucher.from_json(json)
# print the JSON string representation of the object
print(Voucher.to_json())

# convert the object into a dict
voucher_dict = voucher_instance.to_dict()
# create an instance of Voucher from a dict
voucher_from_dict = Voucher.from_dict(voucher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


