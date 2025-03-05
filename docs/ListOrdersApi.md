# grabfood.ListOrdersApi

All URIs are relative to *https://partner-api.grab.com/grabfood-sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_orders**](ListOrdersApi.md#list_orders) | **GET** /partner/v1/orders | List orders


# **list_orders**
> ListOrdersResponse list_orders(authorization, merchant_id, var_date=var_date, page=page, order_ids=order_ids)

List orders

### Example


```python
import grabfood
from grabfood.models.list_orders_response import ListOrdersResponse
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
    api_instance = grabfood.ListOrdersApi(api_client)
    authorization = 'Bearer <ACCESS_TOKEN_HERE>' # str | Specify the generated authorization token of the bearer type.
    merchant_id = '1-CYNGRUNGSBCCC' # str | The merchant's ID that is in GrabFood's database.
    var_date = 'var_date_example' # str |  (optional)
    page = 1 # int | Specify the page number for the report. Required if orderIDs is not provided. (optional)
    order_ids = ['[\"123-CYNKLPCVRN5\",\"456-PCVRN5CYNKL\"]'] # List[str] | List of order IDs. If provided, date and page are not required. (optional)

    try:
        # List orders
        api_response = api_instance.list_orders(authorization, merchant_id, var_date=var_date, page=page, order_ids=order_ids)
        print("The response of ListOrdersApi->list_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListOrdersApi->list_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Specify the generated authorization token of the bearer type. | 
 **merchant_id** | **str**| The merchant&#39;s ID that is in GrabFood&#39;s database. | 
 **var_date** | **str**|  | [optional] 
 **page** | **int**| Specify the page number for the report. Required if orderIDs is not provided. | [optional] 
 **order_ids** | [**List[str]**](str.md)| List of order IDs. If provided, date and page are not required. | [optional] 

### Return type

[**ListOrdersResponse**](ListOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sync success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

