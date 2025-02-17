# MenuSyncWebhookRequest

This request pushes the state of a menu sync operation. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | An universally unique identifier (UUID) string. Used to uniquely identify a webhook request. Partners should use this value to distinguish between different webhook requests. If two requests contain the same requestID, only the first request should be considered and later requests **must** be ignored or discarded.  | [optional] 
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | [optional] 
**partner_merchant_id** | **str** | The merchant&#39;s ID that is on the partner&#39;s database. | [optional] 
**job_id** | **str** | An UUID string. Uniquely identifies a menu sync job. This can be found from the [Menu Update Notification](#tag/update-menu-noti) API response header.  | [optional] 
**updated_at** | **str** | Indicates the time of menu sync status change. This is based on ISO_8601/RFC3339. For example: &#x60;2022-07-29T15:55:59Z&#x60;.  | [optional] 
**status** | **str** | Indicates the state of the menu sync job. | [optional] 
**errors** | **List[str]** | A string array of errors that occurred during processing. This array is empty if the status is not &#x60;FAILED&#x60;. | [optional] 

## Example

```python
from grabfood.models.menu_sync_webhook_request import MenuSyncWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MenuSyncWebhookRequest from a JSON string
menu_sync_webhook_request_instance = MenuSyncWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(MenuSyncWebhookRequest.to_json())

# convert the object into a dict
menu_sync_webhook_request_dict = menu_sync_webhook_request_instance.to_dict()
# create an instance of MenuSyncWebhookRequest from a dict
menu_sync_webhook_request_from_dict = MenuSyncWebhookRequest.from_dict(menu_sync_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


