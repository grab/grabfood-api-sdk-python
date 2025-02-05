# grabfood.AcceptRejectOrderApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_reject_order**](AcceptRejectOrderApi.md#accept_reject_order) | **POST** /partner/v1/order/prepare | Manually accept/reject orders


# **accept_reject_order**
> accept_reject_order(authorization, content_type, accept_order_request)

Manually accept/reject orders

### Example


```python
import grabfood
from grabfood.models.accept_order_request import AcceptOrderRequest
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
    api_instance = grabfood.AcceptRejectOrderApi(api_client)
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    accept_order_request = grabfood.AcceptOrderRequest() # AcceptOrderRequest | 

    try:
        # Manually accept/reject orders
        api_instance.accept_reject_order(authorization, content_type, accept_order_request)
    except Exception as e:
        print("Exception when calling AcceptRejectOrderApi->accept_reject_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **accept_order_request** | [**AcceptOrderRequest**](AcceptOrderRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful. No content returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

