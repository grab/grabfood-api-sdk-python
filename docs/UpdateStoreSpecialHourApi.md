# grabfood.UpdateStoreSpecialHourApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_store_special_hour**](UpdateStoreSpecialHourApi.md#update_store_special_hour) | **PUT** /partner/v2/merchants/{merchantID}/store/special-opening-hour | Update Store Special Hours


# **update_store_special_hour**
> UpdateSpecialHourResponse update_store_special_hour(content_type, authorization, merchant_id, update_special_hour_request)

Update Store Special Hours

### Example


```python
import grabfood
from grabfood.models.update_special_hour_request import UpdateSpecialHourRequest
from grabfood.models.update_special_hour_response import UpdateSpecialHourResponse
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
    api_instance = grabfood.UpdateStoreSpecialHourApi(api_client)
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    merchant_id = '1-CYNGRUNGSBCCC' # str | The merchant's ID that is in GrabFood's database.
    update_special_hour_request = grabfood.UpdateSpecialHourRequest() # UpdateSpecialHourRequest | 

    try:
        # Update Store Special Hours
        api_response = api_instance.update_store_special_hour(content_type, authorization, merchant_id, update_special_hour_request)
        print("The response of UpdateStoreSpecialHourApi->update_store_special_hour:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateStoreSpecialHourApi->update_store_special_hour: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **merchant_id** | **str**| The merchant&#39;s ID that is in GrabFood&#39;s database. | 
 **update_special_hour_request** | [**UpdateSpecialHourRequest**](UpdateSpecialHourRequest.md)|  | 

### Return type

[**UpdateSpecialHourResponse**](UpdateSpecialHourResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized. The access token is invalid. |  -  |
**5XX** | All other unexpected errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

