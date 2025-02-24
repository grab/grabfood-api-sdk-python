# grabfood.CreateSelfServeJourneyApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_self_serve_journey**](CreateSelfServeJourneyApi.md#create_self_serve_journey) | **POST** /partner/v1/self-serve/activation | Create self serve journey


# **create_self_serve_journey**
> CreateSelfServeJourneyResponse create_self_serve_journey(content_type, authorization, create_self_serve_journey_request)

Create self serve journey

### Example


```python
import grabfood
from grabfood.models.create_self_serve_journey_request import CreateSelfServeJourneyRequest
from grabfood.models.create_self_serve_journey_response import CreateSelfServeJourneyResponse
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
    api_instance = grabfood.CreateSelfServeJourneyApi(api_client)
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    create_self_serve_journey_request = grabfood.CreateSelfServeJourneyRequest() # CreateSelfServeJourneyRequest | 

    try:
        # Create self serve journey
        api_response = api_instance.create_self_serve_journey(content_type, authorization, create_self_serve_journey_request)
        print("The response of CreateSelfServeJourneyApi->create_self_serve_journey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreateSelfServeJourneyApi->create_self_serve_journey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **create_self_serve_journey_request** | [**CreateSelfServeJourneyRequest**](CreateSelfServeJourneyRequest.md)|  | 

### Return type

[**CreateSelfServeJourneyResponse**](CreateSelfServeJourneyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

