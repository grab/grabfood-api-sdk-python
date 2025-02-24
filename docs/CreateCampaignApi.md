# grabfood.CreateCampaignApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_campaign**](CreateCampaignApi.md#create_campaign) | **POST** /partner/v1/campaigns | Create campaign


# **create_campaign**
> CreateCampaignResponse create_campaign(content_type, authorization, create_campaign_request)

Create campaign

### Example


```python
import grabfood
from grabfood.models.create_campaign_request import CreateCampaignRequest
from grabfood.models.create_campaign_response import CreateCampaignResponse
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
    api_instance = grabfood.CreateCampaignApi(api_client)
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    create_campaign_request = grabfood.CreateCampaignRequest() # CreateCampaignRequest | 

    try:
        # Create campaign
        api_response = api_instance.create_campaign(content_type, authorization, create_campaign_request)
        print("The response of CreateCampaignApi->create_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreateCampaignApi->create_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **create_campaign_request** | [**CreateCampaignRequest**](CreateCampaignRequest.md)|  | 

### Return type

[**CreateCampaignResponse**](CreateCampaignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API request is successfully processed. |  -  |
**400** | invalid_argument | Code | Reason           | Message                            | | ---- | ---------------- | ----------------------------------- | | 400  | invalid_argument | items not found                  | | 400  | invalid_argument | startTime has to be after now    | | 400  | invalid_argument | CAMPAIGN_START_TIME_TOO_CLOSE_TO_NOW:failed to create MFC:    | | 400  | invalid_argument | CAMPAIGN_DURATION_TOO_LONG:failed to create MFC:    | | 400  | invalid_argument | EFFECTIVE_DATE_OVERLAP:failed to create MFC: Item(s) are on multiple promotions in the same promotion period: SGITE2021052909250501859400 (4-CY4VMFMANYBYJ6-CZNZFFL1G8KKLX-94794295)\&quot;    | | 400  | invalid_argument | EATER_TYPE_CONDITION_IS_NOT_SUPPORTED:failed to create MFC: This level campaign can&#39;t be applied for such eater type    | | 400  | invalid_argument | INVALID_QUOTAS:failed to create MFC:    | | 400  | invalid_argument | INVALID_DISCOUNT_VALUE:failed to create MFC:     | | 400  | invalid_argument | INVALID_PARAMS:failed to create MFC: Order level campaign should have min basket condition    | | 400  | invalid_argument | INVALID_BUNDLE_OFFER:failed to create MFC: bundle price invalid    | | 400  | invalid_argument | INVALID_BUNDLE_OFFER:failed to create MFC: itemIDs should be between 2 and 20    | | 400  | invalid_argument | NOT_SUPPORT_BUNDLE_SAME_MULTIPLE_ITEMS:failed to create MFC: bundle multiple items is not supported for same item bundle    | | 400  | invalid_argument | EXCEED_ACTIVE_CAMPAIGN_MAX_LIMIT:failed to create MFC: number of same campaign level&#39;s promotions exceeds maximum limit(100)    |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

