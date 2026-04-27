# GenerateSTOQRCodeResponse

The STO QR deeplink response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qr_code** | **str** | The deeplink of scan to order QR. | [optional] 

## Example

```python
from grabfood.models.generate_stoqr_code_response import GenerateSTOQRCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateSTOQRCodeResponse from a JSON string
generate_stoqr_code_response_instance = GenerateSTOQRCodeResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateSTOQRCodeResponse.to_json())

# convert the object into a dict
generate_stoqr_code_response_dict = generate_stoqr_code_response_instance.to_dict()
# create an instance of GenerateSTOQRCodeResponse from a dict
generate_stoqr_code_response_from_dict = GenerateSTOQRCodeResponse.from_dict(generate_stoqr_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


