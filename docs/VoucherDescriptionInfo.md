# VoucherDescriptionInfo

A JSON object containing dine-in voucher's description information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The description of the dine-in voucher. | [optional] 

## Example

```python
from grabfood.models.voucher_description_info import VoucherDescriptionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VoucherDescriptionInfo from a JSON string
voucher_description_info_instance = VoucherDescriptionInfo.from_json(json)
# print the JSON string representation of the object
print(VoucherDescriptionInfo.to_json())

# convert the object into a dict
voucher_description_info_dict = voucher_description_info_instance.to_dict()
# create an instance of VoucherDescriptionInfo from a dict
voucher_description_info_from_dict = VoucherDescriptionInfo.from_dict(voucher_description_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


