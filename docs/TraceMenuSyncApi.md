# grabfood.TraceMenuSyncApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trace_menu_sync**](TraceMenuSyncApi.md#trace_menu_sync) | **GET** /partner/v1/merchant/menu/trace | Trace menu sync


# **trace_menu_sync**
> MenuSyncResponse trace_menu_sync(authorization, merchant_id)

Trace menu sync

### Example


```python
import grabfood
from grabfood.models.menu_sync_response import MenuSyncResponse
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
    api_instance = grabfood.TraceMenuSyncApi(api_client)
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    merchant_id = '1-CYNGRUNGSBCCC' # str | The merchant's ID that is in GrabFood's database.

    try:
        # Trace menu sync
        api_response = api_instance.trace_menu_sync(authorization, merchant_id)
        print("The response of TraceMenuSyncApi->trace_menu_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TraceMenuSyncApi->trace_menu_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **merchant_id** | **str**| The merchant&#39;s ID that is in GrabFood&#39;s database. | 

### Return type

[**MenuSyncResponse**](MenuSyncResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sync success or fail |  -  |
**4xx** | Common error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

