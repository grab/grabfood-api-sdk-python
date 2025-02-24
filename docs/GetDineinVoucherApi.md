# grabfood.GetDineinVoucherApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dinein_voucher**](GetDineinVoucherApi.md#get_dinein_voucher) | **GET** /partner/v1/dinein/voucher | Get Dine In Voucher


# **get_dinein_voucher**
> GetDineInVoucherResponse get_dinein_voucher(authorization, merchant_id, voucher_code=voucher_code, certificate_id=certificate_id)

Get Dine In Voucher

### Example


```python
import grabfood
from grabfood.models.get_dine_in_voucher_response import GetDineInVoucherResponse
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
    api_instance = grabfood.GetDineinVoucherApi(api_client)
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    merchant_id = 'merchant_id_example' # str | 
    voucher_code = 'voucher_code_example' # str | A short code for the dine-in voucher purchased by the user. Required if `certificateID` is not specified. (optional)
    certificate_id = 'certificate_id_example' # str | This certificateID is decoded from scanning the QR code, and 1:1 mapping with voucherCode. Required if `voucherCode` is not specified. (optional)

    try:
        # Get Dine In Voucher
        api_response = api_instance.get_dinein_voucher(authorization, merchant_id, voucher_code=voucher_code, certificate_id=certificate_id)
        print("The response of GetDineinVoucherApi->get_dinein_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetDineinVoucherApi->get_dinein_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **merchant_id** | **str**|  | 
 **voucher_code** | **str**| A short code for the dine-in voucher purchased by the user. Required if &#x60;certificateID&#x60; is not specified. | [optional] 
 **certificate_id** | **str**| This certificateID is decoded from scanning the QR code, and 1:1 mapping with voucherCode. Required if &#x60;voucherCode&#x60; is not specified. | [optional] 

### Return type

[**GetDineInVoucherResponse**](GetDineInVoucherResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API request is successfully processed. |  -  |
**400** | invalid_argument | Code | Reason           | Message                                    | Description                                                                                    |  | ---- | ---------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------- |  | 400  | invalid_argument | invalid certificateID                      | The certificateID is not valid.                                                                | | 400  | invalid_argument | voucherCode or certificateID not specified | The voucherCode and certificateID are both empty in params, one of the both must be provided.  |  |  -  |
**404** | not_found | Code | Reason      | Message                      | Description                                                                                     |  | -----| ----------- | ---------------------------- | ----------------------------------------------------------------------------------------------- |  | 404  | not_found   | voucher not found            | The voucher is not found for the specified voucherCode or certificateID.                        | | 404  | not_found   | failed to get store info     | The store is not found for the specified merchantID.                                             |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

