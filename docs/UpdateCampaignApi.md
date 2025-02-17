# grabfood.UpdateCampaignApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_campaign**](UpdateCampaignApi.md#update_campaign) | **PUT** /partner/v1/campaigns/{campaign_id} | Update campaign


# **update_campaign**
> update_campaign(content_type, authorization, campaign_id, update_campaign_request)

Update campaign

### Example


```python
import grabfood
from grabfood.models.update_campaign_request import UpdateCampaignRequest
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
    api_instance = grabfood.UpdateCampaignApi(api_client)
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    campaign_id = 'campaign_id_example' # str | 
    update_campaign_request = grabfood.UpdateCampaignRequest() # UpdateCampaignRequest | 

    try:
        # Update campaign
        api_instance.update_campaign(content_type, authorization, campaign_id, update_campaign_request)
    except Exception as e:
        print("Exception when calling UpdateCampaignApi->update_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **campaign_id** | **str**|  | 
 **update_campaign_request** | [**UpdateCampaignRequest**](UpdateCampaignRequest.md)|  | 

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
**204** | The API request is successfully processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

