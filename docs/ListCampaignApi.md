# grabfood.ListCampaignApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_campaign**](ListCampaignApi.md#list_campaign) | **GET** /partner/v1/campaigns | List campaigns


# **list_campaign**
> ListCampaignResponse list_campaign(authorization, merchant_id)

List campaigns

### Example


```python
import grabfood
from grabfood.models.list_campaign_response import ListCampaignResponse
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
    api_instance = grabfood.ListCampaignApi(api_client)
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    merchant_id = '1-CYNGRUNGSBCCC' # str | The merchant's ID that is in GrabFood's database.

    try:
        # List campaigns
        api_response = api_instance.list_campaign(authorization, merchant_id)
        print("The response of ListCampaignApi->list_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListCampaignApi->list_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **merchant_id** | **str**| The merchant&#39;s ID that is in GrabFood&#39;s database. | 

### Return type

[**ListCampaignResponse**](ListCampaignResponse.md)

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

