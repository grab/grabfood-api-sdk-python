# CampaignConditions

The conditions to apply to a campaign.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** | The campaign&#39;s start time in UTC format. For example, 2021-09-23T03:30:00Z means 2021-09-23 11:30:00 (UTC +08:00). | 
**end_time** | **datetime** | The campaign&#39;s end time in UTC format. | 
**eater_type** | **str** | The type of eater eligible for the campaign.  * &#x60;all&#x60; - campaign will be applied to everyone. No limitation on campaign type. * &#x60;new&#x60; - campaign will be applied to consumers who have not ordered from this store in the last three months. Only applicable to **order-level** campaign.  | 
**min_basket_amount** | **float** | The minimum basket amount to be eligible for the campaign. Only applicable to **order-level** campaign but not to item-level discount campaign. | [optional] 
**bundle_quantity** | **int** | Specify the bundle quantity for bundle offer campaign. | [optional] 
**working_hour** | [**WorkingHour**](WorkingHour.md) |  | [optional] 

## Example

```python
from grabfood.models.campaign_conditions import CampaignConditions

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignConditions from a JSON string
campaign_conditions_instance = CampaignConditions.from_json(json)
# print the JSON string representation of the object
print(CampaignConditions.to_json())

# convert the object into a dict
campaign_conditions_dict = campaign_conditions_instance.to_dict()
# create an instance of CampaignConditions from a dict
campaign_conditions_from_dict = CampaignConditions.from_dict(campaign_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


