# ListCampaignResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ongoing** | [**List[Campaign]**](Campaign.md) |  | [optional] 
**upcoming** | [**List[Campaign]**](Campaign.md) |  | [optional] 

## Example

```python
from grabfood.models.list_campaign_response import ListCampaignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCampaignResponse from a JSON string
list_campaign_response_instance = ListCampaignResponse.from_json(json)
# print the JSON string representation of the object
print(ListCampaignResponse.to_json())

# convert the object into a dict
list_campaign_response_dict = list_campaign_response_instance.to_dict()
# create an instance of ListCampaignResponse from a dict
list_campaign_response_from_dict = ListCampaignResponse.from_dict(list_campaign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


