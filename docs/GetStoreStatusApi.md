# grabfood.GetStoreStatusApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_store_status**](GetStoreStatusApi.md#get_store_status) | **GET** /partner/v1/merchants/{merchantID}/store/status | Get Store Status


# **get_store_status**
> StoreStatusResponse get_store_status(authorization, merchant_id)

Get Store Status

### Example


```python
import grabfood
from grabfood.models.store_status_response import StoreStatusResponse
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
    api_instance = grabfood.GetStoreStatusApi(api_client)
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    merchant_id = '1-CYNGRUNGSBCCC' # str | The merchant's ID that is in GrabFood's database.

    try:
        # Get Store Status
        api_response = api_instance.get_store_status(authorization, merchant_id)
        print("The response of GetStoreStatusApi->get_store_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetStoreStatusApi->get_store_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **merchant_id** | **str**| The merchant&#39;s ID that is in GrabFood&#39;s database. | 

### Return type

[**StoreStatusResponse**](StoreStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized. The access token is invalid. |  -  |
**5XX** | All other unexpected errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

