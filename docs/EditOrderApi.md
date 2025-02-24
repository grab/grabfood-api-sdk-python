# grabfood.EditOrderApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_order**](EditOrderApi.md#edit_order) | **PUT** /partner/v1/orders/{orderID} | Edit Order


# **edit_order**
> edit_order(content_type, authorization, order_id, edit_order_request)

Edit Order

### Example


```python
import grabfood
from grabfood.models.edit_order_request import EditOrderRequest
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
    api_instance = grabfood.EditOrderApi(api_client)
    content_type = 'application/json' # str | The content type of the request body. You must use `application/json` for this header as GrabFood API currently does not support other formats.
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    order_id = 'order_id_example' # str | 
    edit_order_request = grabfood.EditOrderRequest() # EditOrderRequest | 

    try:
        # Edit Order
        api_instance.edit_order(content_type, authorization, order_id, edit_order_request)
    except Exception as e:
        print("Exception when calling EditOrderApi->edit_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **order_id** | **str**|  | 
 **edit_order_request** | [**EditOrderRequest**](EditOrderRequest.md)|  | 

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
**204** | Successful. No content returned. |  -  |
**4XX** | invalid_argument Fail example with code and reason. | Code | Reason | Message | | ------| ------| ------ | | 400 | invalid_argument | nothing changed | | 400 | invalid_argument | can&#39;t remove all items | | 404 | not_found | order detail abnormal | | 403 | forbidden | not editable | | 400 | invalid_argument | recalculate failed | | 400 | invalid_argument| submit edit failed | | 404 | not_found | get merchant failed | | 400 | invalid_argument | exceed basket limit | | 400 | invalid_argument | exceed price increase limit | | 400 | invalid_argument | negative weight | | 400 | invalid_argument | parameters must include all items | | 400 | invalid_argument | fraud check error | | 400  | invalid_argument | externalItemID not supported for this status | | 400 | invalid_argument | externalItemID inactive or out of selling time | | 400 | invalid_argument | added item invalid |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

