# grabfood.MarkOrderReadyApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mark_order_ready**](MarkOrderReadyApi.md#mark_order_ready) | **POST** /partner/v1/orders/mark | Mark order as ready


# **mark_order_ready**
> mark_order_ready(content_type, authorization, mark_order_request)

Mark order as ready

### Example


```python
import grabfood
from grabfood.models.mark_order_request import MarkOrderRequest
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
    api_instance = grabfood.MarkOrderReadyApi(api_client)
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    mark_order_request = grabfood.MarkOrderRequest() # MarkOrderRequest | 

    try:
        # Mark order as ready
        api_instance.mark_order_ready(content_type, authorization, mark_order_request)
    except Exception as e:
        print("Exception when calling MarkOrderReadyApi->mark_order_ready: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **mark_order_request** | [**MarkOrderRequest**](MarkOrderRequest.md)|  | 

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
**204** | Successful. No content returned. |  -  |
**400** | invalid_argument | Code | Reason | Message | | ----- | ------ | ------- | | 400 | invalid_argument | invalid order state | | 400 | invalid_argument | order already marked ready| | 400 | invalid_argument | invalid markStatus: 0|  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

