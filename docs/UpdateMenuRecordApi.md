# grabfood.UpdateMenuRecordApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_update_menu**](UpdateMenuRecordApi.md#batch_update_menu) | **PUT** /partner/v1/batch/menu | Batch Update Menu
[**update_menu**](UpdateMenuRecordApi.md#update_menu) | **PUT** /partner/v1/menu | Update menu record


# **batch_update_menu**
> BatchUpdateMenuResponse batch_update_menu(content_type, authorization, batch_update_menu_item)

Batch Update Menu

### Example


```python
import grabfood
from grabfood.models.batch_update_menu_item import BatchUpdateMenuItem
from grabfood.models.batch_update_menu_response import BatchUpdateMenuResponse
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
    api_instance = grabfood.UpdateMenuRecordApi(api_client)
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    batch_update_menu_item = grabfood.BatchUpdateMenuItem() # BatchUpdateMenuItem | 

    try:
        # Batch Update Menu
        api_response = api_instance.batch_update_menu(content_type, authorization, batch_update_menu_item)
        print("The response of UpdateMenuRecordApi->batch_update_menu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateMenuRecordApi->batch_update_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **batch_update_menu_item** | [**BatchUpdateMenuItem**](BatchUpdateMenuItem.md)|  | 

### Return type

[**BatchUpdateMenuResponse**](BatchUpdateMenuResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API request is successfully processed. Refer to status and errors for more info. |  -  |
**400** | invalid_argument | Description | | ----------- | | Invalid parameter | | Batch update menu support at most 200 items |  |  -  |
**409** | conflict. BatchUpdate ITEM xxx too frequently, retry after 10 seconds  |  -  |
**429** | Too Many Requests  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_menu**
> update_menu(content_type, authorization, update_menu_request)

Update menu record

### Example


```python
import grabfood
from grabfood.models.update_menu_request import UpdateMenuRequest
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
    api_instance = grabfood.UpdateMenuRecordApi(api_client)
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    update_menu_request = grabfood.UpdateMenuRequest() # UpdateMenuRequest | 

    try:
        # Update menu record
        api_instance.update_menu(content_type, authorization, update_menu_request)
    except Exception as e:
        print("Exception when calling UpdateMenuRecordApi->update_menu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **update_menu_request** | [**UpdateMenuRequest**](UpdateMenuRequest.md)|  | 

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
**204** | Successful. No Content returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

