# grabfood.EditOrderApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_order_v1**](EditOrderApi.md#edit_order_v1) | **PUT** /partner/v1/orders/{orderID} | Edit Order V1
[**edit_order_v2**](EditOrderApi.md#edit_order_v2) | **PUT** /partner/v2/orders/{orderID} | Edit Order V2


# **edit_order_v1**
> edit_order_v1(content_type, authorization, order_id, edit_order_request)

Edit Order V1

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
        # Edit Order V1
        api_instance.edit_order_v1(content_type, authorization, order_id, edit_order_request)
    except Exception as e:
        print("Exception when calling EditOrderApi->edit_order_v1: %s\n" % e)
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
**400** | invalid_argument | Code | Reason           | Message                                    | Description                                                                                               |  | ---- | ---------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------- |  | 400  | invalid_argument | nothing changed                            | The items struct is empty                                                                                | | 400  | invalid_argument | can&#39;t remove all items                     | we don&#39;t allow clean all the items                                                                      | | 400  | invalid_argument | externalItemID not supported for this status | externalItemID not supported for this status                                                          | | 400  | invalid_argument | externalItemID only allowed for ADDED item status | externalItemID only allowed for ADDED item status                                                 | | 400  | invalid_argument | invalid price, price can&#39;t be negative     | DepositAmountInMin is negative, OfflinePOSDiscountInMin is negative                                     | | 400  | invalid_argument | params must include all items              | params must include all items in the order                                                              | | 400  | invalid_argument | exceed basket limit                        | Total price exceed basket limit                                                                          | | 400  | invalid_argument | exceed max price amount limit              | Total price exceed limit:&lt;br/&gt;• SG: S$1000&lt;br/&gt;• ID: Rp10,000,000&lt;br/&gt;• PH: ₱15,000&lt;br/&gt;• VN: ₫15,000,000&lt;br/&gt;• TH: ฿300,000&lt;br/&gt;• MY: RM1,500 | | 400  | invalid_argument | recalculate failed                         | recalculate failed                                                                                       | | 400  | invalid_argument | submit edit failed                         | submit edit failed                                                                                       | | 400  | invalid_argument | exceed price increase limit                | exceed price increase limit                                                                              | | 400  | invalid_argument | negative weight                            | negative weight                                                                                          | | 400  | invalid_argument | fraud check error                          | fraud check error                                                                                        | | 400  | invalid_argument | externalItemID inactive or out of selling time | externalItemID inactive or out of selling time                                                      | | 400  | invalid_argument | added item invalid                         | added item invalid                                                                                       |  |  -  |
**403** | forbidden | Code | Reason    | Message      | Description                                                                                               |  | ---- | --------- | ------------ | --------------------------------------------------------------------------------------------------------- |  | 403  | forbidden | not editable | not editable                                                                                              |  |  -  |
**404** | not_found | Code | Reason    | Message              | Description                                                                                               |  | ---- | --------- | -------------------- | --------------------------------------------------------------------------------------------------------- |  | 404  | not_found | not found order      | The orderID is not found grab status.                                                                   | | 404  | not_found | invalid order        | The order status is wrong for edit action.                                                              | | 404  | not_found | not found item       | The itemID doesn&#39;t match with isExternalItemID and can&#39;t be found from grab system.                     | | 404  | not_found | Invalid item status  | The item status isn&#39;t correct. Eg, there is no item in the order but want to delete it.                | | 404  | not_found | order detail abnormal | order detail abnormal                                                                                   | | 404  | not_found | get merchant failed  | get merchant failed                                                                                      |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_order_v2**
> EditOrderV2Response edit_order_v2(content_type, authorization, order_id, edit_order_request)

Edit Order V2

### Example


```python
import grabfood
from grabfood.models.edit_order_request import EditOrderRequest
from grabfood.models.edit_order_v2_response import EditOrderV2Response
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
        # Edit Order V2
        api_response = api_instance.edit_order_v2(content_type, authorization, order_id, edit_order_request)
        print("The response of EditOrderApi->edit_order_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditOrderApi->edit_order_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| The content type of the request body. You must use &#x60;application/json&#x60; for this header as GrabFood API currently does not support other formats. | 
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **order_id** | **str**|  | 
 **edit_order_request** | [**EditOrderRequest**](EditOrderRequest.md)|  | 

### Return type

[**EditOrderV2Response**](EditOrderV2Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API request is successfully processed. |  -  |
**400** | invalid_argument | Code | Reason           | Message                                    | Description                                                                                               |  | ---- | ---------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------- |  | 400  | invalid_argument | nothing changed                            | The items struct is empty                                                                                | | 400  | invalid_argument | can&#39;t remove all items                     | we don&#39;t allow clean all the items                                                                      | | 400  | invalid_argument | externalItemID not supported for this status | externalItemID not supported for this status                                                          | | 400  | invalid_argument | externalItemID only allowed for ADDED item status | externalItemID only allowed for ADDED item status                                                 | | 400  | invalid_argument | invalid price, price can&#39;t be negative     | DepositAmountInMin is negative, OfflinePOSDiscountInMin is negative                                     | | 400  | invalid_argument | params must include all items              | params must include all items in the order                                                              | | 400  | invalid_argument | exceed basket limit                        | Total price exceed basket limit                                                                          | | 400  | invalid_argument | exceed max price amount limit              | Total price exceed limit:&lt;br/&gt;• SG: S$1000&lt;br/&gt;• ID: Rp10,000,000&lt;br/&gt;• PH: ₱15,000&lt;br/&gt;• VN: ₫15,000,000&lt;br/&gt;• TH: ฿300,000&lt;br/&gt;• MY: RM1,500 | | 400  | invalid_argument | recalculate failed                         | recalculate failed                                                                                       | | 400  | invalid_argument | submit edit failed                         | submit edit failed                                                                                       | | 400  | invalid_argument | exceed price increase limit                | exceed price increase limit                                                                              | | 400  | invalid_argument | negative weight                            | negative weight                                                                                          | | 400  | invalid_argument | fraud check error                          | fraud check error                                                                                        | | 400  | invalid_argument | externalItemID inactive or out of selling time | externalItemID inactive or out of selling time                                                      | | 400  | invalid_argument | added item invalid                         | added item invalid                                                                                       |  |  -  |
**403** | forbidden | Code | Reason    | Message      | Description                                                                                               |  | ---- | --------- | ------------ | --------------------------------------------------------------------------------------------------------- |  | 403  | forbidden | not editable | not editable                                                                                              |  |  -  |
**404** | not_found | Code | Reason    | Message              | Description                                                                                               |  | ---- | --------- | -------------------- | --------------------------------------------------------------------------------------------------------- |  | 404  | not_found | not found order      | The orderID is not found grab status.                                                                   | | 404  | not_found | invalid order        | The order status is wrong for edit action.                                                              | | 404  | not_found | not found item       | The itemID doesn&#39;t match with isExternalItemID and can&#39;t be found from grab system.                     | | 404  | not_found | Invalid item status  | The item status isn&#39;t correct. Eg, there is no item in the order but want to delete it.                | | 404  | not_found | order detail abnormal | order detail abnormal                                                                                   | | 404  | not_found | get merchant failed  | get merchant failed                                                                                      |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

