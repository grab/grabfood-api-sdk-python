# grabfood.GetOauthGrabApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_oauth_grab**](GetOauthGrabApi.md#get_oauth_grab) | **POST** /grabid/v1/oauth2/token | Get Oauth access token


# **get_oauth_grab**
> GrabOauthResponse get_oauth_grab(content_type, grab_oauth_request)

Get Oauth access token

### Example


```python
import grabfood
from grabfood.models.grab_oauth_request import GrabOauthRequest
from grabfood.models.grab_oauth_response import GrabOauthResponse
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
    api_instance = grabfood.GetOauthGrabApi(api_client)
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    grab_oauth_request = grabfood.GrabOauthRequest() # GrabOauthRequest | 

    try:
        # Get Oauth access token
        api_response = api_instance.get_oauth_grab(content_type, grab_oauth_request)
        print("The response of GetOauthGrabApi->get_oauth_grab:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GetOauthGrabApi->get_oauth_grab: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **grab_oauth_request** | [**GrabOauthRequest**](GrabOauthRequest.md)|  | 

### Return type

[**GrabOauthResponse**](GrabOauthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API request is successfully processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

