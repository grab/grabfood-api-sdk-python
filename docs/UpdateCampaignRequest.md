# UpdateCampaignRequest

This request updates a campaign for your GrabFood store. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | [optional] 
**name** | **str** | The campaign&#39;s name. | [optional] 
**quotas** | [**CampaignQuotas**](CampaignQuotas.md) |  | [optional] 
**conditions** | [**CampaignConditions**](CampaignConditions.md) |  | [optional] 
**discount** | [**CampaignDiscount**](CampaignDiscount.md) |  | [optional] 
**custom_tag** | **str** | Specify the tag for custom bundle offer campaign. Only whitelisted partner is supported as of now. | [optional] 

## Example

```python
from grabfood.models.update_campaign_request import UpdateCampaignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCampaignRequest from a JSON string
update_campaign_request_instance = UpdateCampaignRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCampaignRequest.to_json())

# convert the object into a dict
update_campaign_request_dict = update_campaign_request_instance.to_dict()
# create an instance of UpdateCampaignRequest from a dict
update_campaign_request_from_dict = UpdateCampaignRequest.from_dict(update_campaign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


