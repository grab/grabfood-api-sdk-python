# grabfood.UpdateOrderReadyTimeApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_order_ready_time**](UpdateOrderReadyTimeApi.md#update_order_ready_time) | **PUT** /partner/v1/order/readytime | Update new order ready time


# **update_order_ready_time**
> update_order_ready_time(content_type, authorization, new_order_time_request)

Update new order ready time

### Example


```python
import grabfood
from grabfood.models.new_order_time_request import NewOrderTimeRequest
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
    api_instance = grabfood.UpdateOrderReadyTimeApi(api_client)
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    new_order_time_request = grabfood.NewOrderTimeRequest() # NewOrderTimeRequest | 

    try:
        # Update new order ready time
        api_instance.update_order_ready_time(content_type, authorization, new_order_time_request)
    except Exception as e:
        print("Exception when calling UpdateOrderReadyTimeApi->update_order_ready_time: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **new_order_time_request** | [**NewOrderTimeRequest**](NewOrderTimeRequest.md)|  | 

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
**400** | invalid_argument | Code | Reason | Message | | ----- | ----- | ------- | | 400 | invalid_argument | invalid new order ready time | | 400 | invalid_argument | order ready time not allowed to change |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

