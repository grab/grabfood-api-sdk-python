# grabfood.CheckOrderCancelableApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_order_cancelable**](CheckOrderCancelableApi.md#check_order_cancelable) | **GET** /partner/v1/order/cancelable | Check order cancelable


# **check_order_cancelable**
> CheckOrderCancelableResponse check_order_cancelable(authorization, order_id, merchant_id)

Check order cancelable

### Example


```python
import grabfood
from grabfood.models.check_order_cancelable_response import CheckOrderCancelableResponse
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
    api_instance = grabfood.CheckOrderCancelableApi(api_client)
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    order_id = 'order_id_example' # str | 
    merchant_id = '1-CYNGRUNGSBCCC' # str | The merchant's ID that is in GrabFood's database.

    try:
        # Check order cancelable
        api_response = api_instance.check_order_cancelable(authorization, order_id, merchant_id)
        print("The response of CheckOrderCancelableApi->check_order_cancelable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckOrderCancelableApi->check_order_cancelable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **order_id** | **str**|  | 
 **merchant_id** | **str**| The merchant&#39;s ID that is in GrabFood&#39;s database. | 

### Return type

[**CheckOrderCancelableResponse**](CheckOrderCancelableResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API request is successfully processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

