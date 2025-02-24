# Campaign

A JSON object containing the campaign details for a merchant. Only campaigns that are funded by merchants will be sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The campaign&#39;s ID. | 
**created_by** | **str** | The party who created the campaign. Can be created by partners via API, merchants via the merchant app or Grab. | 
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | 
**name** | **str** | The campaign&#39;s name. | 
**quotas** | [**CampaignQuotas**](CampaignQuotas.md) |  | [optional] 
**conditions** | [**CampaignConditions**](CampaignConditions.md) |  | [optional] 
**discount** | [**CampaignDiscount**](CampaignDiscount.md) |  | [optional] 
**custom_tag** | **str** | Specify the tag for custom bundle offer campaign. Only whitelisted partner is supported as of now. | [optional] 

## Example

```python
from grabfood.models.campaign import Campaign

# TODO update the JSON string below
json = "{}"
# create an instance of Campaign from a JSON string
campaign_instance = Campaign.from_json(json)
# print the JSON string representation of the object
print(Campaign.to_json())

# convert the object into a dict
campaign_dict = campaign_instance.to_dict()
# create an instance of Campaign from a dict
campaign_from_dict = Campaign.from_dict(campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


