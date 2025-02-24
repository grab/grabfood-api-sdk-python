# CampaignDiscount

The discount detail for a particular campaign when conditions are satisfied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of discount  | 
**cap** | **float** | The maximum discount dollar amount. It is **not required** and will be ignored when the &#x60;discount.type&#x60; is: - &#x60;net&#x60; - &#x60;delivery&#x60; - &#x60;freeItem&#x60; - &#x60;bundleSameNet&#x60; - &#x60;bundleSamePercentage&#x60; - &#x60;bundleSameFixPrice&#x60; - &#x60;bundleDiffNet&#x60; - &#x60;bundleDiffPercentage&#x60; - &#x60;bundleDiffFixPrice&#x60;  | [optional] 
**value** | **float** | Specify the discount amount. Decimal number is not supported For VN, ID and TH. For example, &#x60;10.5&#x60; is not allowed and it should be &#x60;10.0&#x60;. * Dollar amount value when &#x60;discount.type&#x60; is &#x60;net&#x60;, &#x60;delivery&#x60;, &#x60;bundleSameNet&#x60;, &#x60;bundleSameFixPrice&#x60;, &#x60;bundleDiffNet&#x60;, &#x60;bundleDiffFixPrice&#x60;. * Percentage value (0-100) when &#x60;discount.type&#x60; is &#x60;percentage&#x60;, &#x60;bundleSamePercentage&#x60;, &#x60;bundleDiffPercentage&#x60;. * **Not required** when &#x60;discount.type&#x60; is &#x60;freeItem&#x60;.  | [optional] 
**scope** | [**CampaignScope**](CampaignScope.md) |  | 

## Example

```python
from grabfood.models.campaign_discount import CampaignDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignDiscount from a JSON string
campaign_discount_instance = CampaignDiscount.from_json(json)
# print the JSON string representation of the object
print(CampaignDiscount.to_json())

# convert the object into a dict
campaign_discount_dict = campaign_discount_instance.to_dict()
# create an instance of CampaignDiscount from a dict
campaign_discount_from_dict = CampaignDiscount.from_dict(campaign_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


