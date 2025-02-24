# PushIntegrationStatusWebhookRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_merchant_id** | **str** | The merchant&#39;s ID that is on the partner&#39;s database. | 
**grab_merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | 
**integration_status** | **str** | The store integration status. - &#x60;INACTIVE&#x60;: Merchant integration deactivated - &#x60;ACTIVE&#x60;: Merchant integration activated - &#x60;SYNCING&#x60;: Merchant integration is syncing - &#x60;FAILED&#x60;: Merchant integration has failed  | 

## Example

```python
from grabfood.models.push_integration_status_webhook_request import PushIntegrationStatusWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PushIntegrationStatusWebhookRequest from a JSON string
push_integration_status_webhook_request_instance = PushIntegrationStatusWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(PushIntegrationStatusWebhookRequest.to_json())

# convert the object into a dict
push_integration_status_webhook_request_dict = push_integration_status_webhook_request_instance.to_dict()
# create an instance of PushIntegrationStatusWebhookRequest from a dict
push_integration_status_webhook_request_from_dict = PushIntegrationStatusWebhookRequest.from_dict(push_integration_status_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


