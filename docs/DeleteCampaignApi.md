# grabfood.DeleteCampaignApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_campaign**](DeleteCampaignApi.md#delete_campaign) | **DELETE** /partner/v1/campaigns/{campaign_id} | Delete campaigns


# **delete_campaign**
> delete_campaign(authorization, campaign_id)

Delete campaigns

### Example


```python
import grabfood
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
    api_instance = grabfood.DeleteCampaignApi(api_client)
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    campaign_id = 'campaign_id_example' # str | 

    try:
        # Delete campaigns
        api_instance.delete_campaign(authorization, campaign_id)
    except Exception as e:
        print("Exception when calling DeleteCampaignApi->delete_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **campaign_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The API request is successfully processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

