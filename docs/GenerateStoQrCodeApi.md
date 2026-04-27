# grabfood.GenerateStoQrCodeApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_sto_qr_code**](GenerateStoQrCodeApi.md#generate_sto_qr_code) | **GET** /partner/v1/dinein/sto/qrcode | Generate STO QR code


# **generate_sto_qr_code**
> GenerateSTOQRCodeResponse generate_sto_qr_code(authorization, content_type, merchant_id, qr_type, table_number)

Generate STO QR code

### Example


```python
import grabfood
from grabfood.models.generate_stoqr_code_response import GenerateSTOQRCodeResponse
from grabfood.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://partner-api.grab.com/grabfood-sandbox
# See configuration.py for a list of all supported configuration parameters.
configuration = grabfood.Configuration(
    host = "https://partner-api.grab.com/grabfood-sandbox"
)


# Enter a context with an instance of the API client
with grabfood.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grabfood.GenerateStoQrCodeApi(api_client)
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    merchant_id = 'merchant_id_example' # str | 
    qr_type = 'qr_type_example' # str | 
    table_number = 'table_number_example' # str | 

    try:
        # Generate STO QR code
        api_response = api_instance.generate_sto_qr_code(authorization, content_type, merchant_id, qr_type, table_number)
        print("The response of GenerateStoQrCodeApi->generate_sto_qr_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerateStoQrCodeApi->generate_sto_qr_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **merchant_id** | **str**|  | 
 **qr_type** | **str**|  | 
 **table_number** | **str**|  | 

### Return type

[**GenerateSTOQRCodeResponse**](GenerateSTOQRCodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API request is successfully processed. |  -  |
**400** | invalid_argument | Code | Reason           | Message                                    | Description                                                                                               |  | ---- | ---------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------- |  | 400  | invalid_argument | not enabled                                | The generate STO QR code feature is not enabled for the merchant, please reach out to the integration manager    |  |  -  |
**404** | not_found | Code | Reason      | Message                      | Description                                                                                     |  | -----| ----------- | ---------------------------- | ----------------------------------------------------------------------------------------------- |  | 404  | not_found   | failed to get store info     | The store is not found for the specified merchantID.                                            |  |  -  |
**500** | internal | Code | Reason      | Message                      | Description                                                                                     |  | -----| ----------- | ---------------------------- | ----------------------------------------------------------------------------------------------- |  | 500  | internal    | generate QR failed        | generate QR failed, please try again later.                                                      |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

