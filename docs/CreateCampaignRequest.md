# CreateCampaignRequest

This request creates a campaign for your GrabFood store. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | 
**name** | **str** | The campaign&#39;s name. | 
**quotas** | [**CampaignQuotas**](CampaignQuotas.md) |  | [optional] 
**conditions** | [**CampaignConditions**](CampaignConditions.md) |  | 
**discount** | [**CampaignDiscount**](CampaignDiscount.md) |  | 
**custom_tag** | **str** | Specify the tag for custom bundle offer campaign. Only whitelisted partner is supported as of now. | [optional] 

## Example

```python
from grabfood.models.create_campaign_request import CreateCampaignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCampaignRequest from a JSON string
create_campaign_request_instance = CreateCampaignRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCampaignRequest.to_json())

# convert the object into a dict
create_campaign_request_dict = create_campaign_request_instance.to_dict()
# create an instance of CreateCampaignRequest from a dict
create_campaign_request_from_dict = CreateCampaignRequest.from_dict(create_campaign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


