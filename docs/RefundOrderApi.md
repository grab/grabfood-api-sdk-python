# grabfood.RefundOrderApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refund_order**](RefundOrderApi.md#refund_order) | **POST** /partner/v1/orders/refund | Refund Order


# **refund_order**
> refund_order(authorization, content_type, refund_order_request)

Refund Order

### Example


```python
import grabfood
from grabfood.models.refund_order_request import RefundOrderRequest
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
    api_instance = grabfood.RefundOrderApi(api_client)
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    refund_order_request = grabfood.RefundOrderRequest() # RefundOrderRequest | 

    try:
        # Refund Order
        api_instance.refund_order(authorization, content_type, refund_order_request)
    except Exception as e:
        print("Exception when calling RefundOrderApi->refund_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **refund_order_request** | [**RefundOrderRequest**](RefundOrderRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. No content returned. |  -  |
**400** | invalid_argument | Code | Reason           | Message                                    | Description                                                                                               |  | ---- | ---------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------- |  | 400  | invalid_argument | INVALID_ORDER                              | The orderID is not found in grab, or the order is not a ScanToOrder or offline POS order               | | 400  | invalid_argument | ORDER_ALREADY_REFUND                       | The order already been refunded                                                                          | | 400  | invalid_argument | ORDER_WRONG_STATUS_FOR_REFUND              | The order is not in COMPLETED status, can&#39;t be refunded                                                 | | 400  | invalid_argument | REACH_DAILY_THROTTLE                       | Reached daily refund limit                                                                               | | 400  | invalid_argument | TIME_OUT_REFUND_PERIOD                     | Exceed the refund time window                                                                            |  |  -  |
**404** | Not Found. Order doesn&#39;t exist. |  -  |
**500** | Internal Server Error. Server encountered an unexpected error that prevented it from serving the API request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

