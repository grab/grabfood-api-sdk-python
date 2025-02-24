# grabfood.RedeemDineinVoucherApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redeem_dinein_voucher**](RedeemDineinVoucherApi.md#redeem_dinein_voucher) | **POST** /partner/v1/dinein/voucher/redeem | Redeem Dine In Voucher


# **redeem_dinein_voucher**
> RedeemDineInVoucherResponse redeem_dinein_voucher(authorization, content_type, redeem_dine_in_voucher_request)

Redeem Dine In Voucher

### Example


```python
import grabfood
from grabfood.models.redeem_dine_in_voucher_request import RedeemDineInVoucherRequest
from grabfood.models.redeem_dine_in_voucher_response import RedeemDineInVoucherResponse
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
    api_instance = grabfood.RedeemDineinVoucherApi(api_client)
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    redeem_dine_in_voucher_request = grabfood.RedeemDineInVoucherRequest() # RedeemDineInVoucherRequest | 

    try:
        # Redeem Dine In Voucher
        api_response = api_instance.redeem_dinein_voucher(authorization, content_type, redeem_dine_in_voucher_request)
        print("The response of RedeemDineinVoucherApi->redeem_dinein_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedeemDineinVoucherApi->redeem_dinein_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **redeem_dine_in_voucher_request** | [**RedeemDineInVoucherRequest**](RedeemDineInVoucherRequest.md)|  | 

### Return type

[**RedeemDineInVoucherResponse**](RedeemDineInVoucherResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API request is successfully processed. |  -  |
**400** | invalid_argument | Code | Reason           | Message                                    | Description                                                                                               |  | ---- | ---------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------- |  | 400  | invalid_argument | invalid certificateID                      | The certificateID is not valid.                                                                           | | 400  | invalid_argument | not enabled                                | The QR redemption feature is not enabled for the merchant, please reach out to the integration manager    |  |  -  |
**404** | not_found | Code | Reason      | Message                      | Description                                                                                     |  | -----| ----------- | ---------------------------- | ----------------------------------------------------------------------------------------------- |  | 404  | not_found   | voucher not found            | The voucher is not found for the specified voucherCode or certificateID.                        | | 404  | not_found   | failed to get store info     | The store is not found for the specified merchantID.                                            |  |  -  |
**500** | internal | Code | Reason      | Message                      | Description                                                                                     |  | -----| ----------- | ---------------------------- | ----------------------------------------------------------------------------------------------- |  | 500  | internal    | redeem failed                | Redemption failed, please try again later.                                                      |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

