# CampaignQuotas

The quotas/limits for a particular campaign.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The maximum number of redemptions. Default is unlimited if unspecified.  | [optional] 
**total_count_per_user** | **int** | The maximum number of redemptions per user. Default is unlimited if unspecified. | [optional] 

## Example

```python
from grabfood.models.campaign_quotas import CampaignQuotas

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignQuotas from a JSON string
campaign_quotas_instance = CampaignQuotas.from_json(json)
# print the JSON string representation of the object
print(CampaignQuotas.to_json())

# convert the object into a dict
campaign_quotas_dict = campaign_quotas_instance.to_dict()
# create an instance of CampaignQuotas from a dict
campaign_quotas_from_dict = CampaignQuotas.from_dict(campaign_quotas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


