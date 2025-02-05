# grabfood.UpdateDeliveryStateApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_delivery_state**](UpdateDeliveryStateApi.md#update_delivery_state) | **POST** /partner/v1/order/delivery | Update delivery state


# **update_delivery_state**
> update_delivery_state(content_type, authorization, order_delivery_request)

Update delivery state

### Example


```python
import grabfood
from grabfood.models.order_delivery_request import OrderDeliveryRequest
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
    api_instance = grabfood.UpdateDeliveryStateApi(api_client)
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    order_delivery_request = grabfood.OrderDeliveryRequest() # OrderDeliveryRequest | 

    try:
        # Update delivery state
        api_instance.update_delivery_state(content_type, authorization, order_delivery_request)
    except Exception as e:
        print("Exception when calling UpdateDeliveryStateApi->update_delivery_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **order_delivery_request** | [**OrderDeliveryRequest**](OrderDeliveryRequest.md)|  | 

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

