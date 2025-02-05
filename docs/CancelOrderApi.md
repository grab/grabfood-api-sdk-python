# grabfood.CancelOrderApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](CancelOrderApi.md#cancel_order) | **PUT** /partner/v1/order/cancel | Cancel an order


# **cancel_order**
> CancelOrderResponse cancel_order(content_type, authorization, cancel_order_request)

Cancel an order

### Example


```python
import grabfood
from grabfood.models.cancel_order_request import CancelOrderRequest
from grabfood.models.cancel_order_response import CancelOrderResponse
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
    api_instance = grabfood.CancelOrderApi(api_client)
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    cancel_order_request = grabfood.CancelOrderRequest() # CancelOrderRequest | 

    try:
        # Cancel an order
        api_response = api_instance.cancel_order(content_type, authorization, cancel_order_request)
        print("The response of CancelOrderApi->cancel_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CancelOrderApi->cancel_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **cancel_order_request** | [**CancelOrderRequest**](CancelOrderRequest.md)|  | 

### Return type

[**CancelOrderResponse**](CancelOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API request is successfully processed. |  -  |
**400** | invalid_argument |  -  |
**403** | This request is forbidden.  For each 403 HTTP response, a detailed reason will be returned. | Type | Message | | -------| ------------| | Invalid order | Order cannot be cancelled via this endpoint as this order does not belong to you. Please contact Grab Support for further assistance. | | Daily limit reached | Order cannot be cancelled via this endpoint as the daily limit for order cancellations has been reached. Please contact Grab Support for further assistance. | | Weekly limit reached | Order cannot be cancelled via this endpoint as the weekly limit for order cancellations has been reached. Please contact Grab Support for further assistance. | | Monthly limit reached | Order cannot be cancelled via this endpoint as the monthly limit for order cancellations has been reached. Please contact Grab Support for further assistance. | | Mix and match order | Order cannot be cancelled via this endpoint as it is part of a GKMM (Grab Kitchen Mix And Match) order. Please contact Grab Support for further assistance. | | Self-pick up order | Order cannot be cancelled via this endpoint as it is a self-pick up order. Please contact Grab Support for further assistance. | | Scheduled order | Order cannot be cancelled via this endpoint as it is a scheduled order. Please contact Grab Support for further assistance. | | Time limit | Order cannot be cancelled via this endpoint as the cancellation time limit has been reached since a driver has been allocated for too long. Please contact Grab Support for further assistance. | | Manual-accept stores | Order cannot be cancelled via this endpoint as only stores on auto-accept can use this endpoint. Please contact Grab Support for further assistance. | | Outdated driver app | Order cannot be cancelled via this endpoint as the driver&#39;s Grab app is outdated. Please contact Grab Support for further assistance. | | Unallocated order | Order cannot be cancelled via this endpoint as the order has not been allocated yet. Please contact Grab Support for further assistance. | | Default error (edge case) | Order cannot be cancelled via this endpoint as a default error has occured. Please contact Grab Support for further assistance. |  |  -  |
**404** | not_found |  -  |
**409** | conflict |  -  |
**500** | 5XX error codes are rare and indicate that GrabFood is facing an internal server error. This type of error is applicable to all HTTP response codes in the 500 range, e.g. 500, 504. Retry the operation at a later time with a unique ID. Use an exponential backoff retry mechanism to resend the requests at an increasingly slower interval. It is also a good practice to use a randomized delay (jitter) in your retry schedule.  | Type | Message | | -------| ------------| | Get order error | Get order failed. | | Cancel order error | Cancel order failed. |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

