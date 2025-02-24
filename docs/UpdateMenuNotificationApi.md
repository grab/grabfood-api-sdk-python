# grabfood.UpdateMenuNotificationApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_menu_notification**](UpdateMenuNotificationApi.md#update_menu_notification) | **POST** /partner/v1/merchant/menu/notification | Notify Grab of updated menu


# **update_menu_notification**
> update_menu_notification(content_type, authorization, update_menu_notif_request)

Notify Grab of updated menu

### Example


```python
import grabfood
from grabfood.models.update_menu_notif_request import UpdateMenuNotifRequest
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
    api_instance = grabfood.UpdateMenuNotificationApi(api_client)
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    update_menu_notif_request = grabfood.UpdateMenuNotifRequest() # UpdateMenuNotifRequest | 

    try:
        # Notify Grab of updated menu
        api_instance.update_menu_notification(content_type, authorization, update_menu_notif_request)
    except Exception as e:
        print("Exception when calling UpdateMenuNotificationApi->update_menu_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **update_menu_notif_request** | [**UpdateMenuNotifRequest**](UpdateMenuNotifRequest.md)|  | 

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
**204** | Successful. No Content returned. |  * x-job-id - Uniquely identifies a menu sync job. Please mention this value while raising any issues on [Menu sync state webhook](#tag/menu-sync-state-webhook). <br>  |
**4XX** | invalid_argument Fail example with code and reason. | Code | Reason           | Message                                            | | -----| ---------------  | -------------------------------------------------- | | 409  | invalid_argument | sync menu too frequently, retry after 120 seconds  |  &gt; Note: A distributed interval lock mechanism with a default duration of 120 seconds is in place for the same requests sent. The lock duration is customizable and may vary across different partners.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

