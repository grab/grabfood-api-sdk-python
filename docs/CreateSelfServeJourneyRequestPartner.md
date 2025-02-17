# CreateSelfServeJourneyRequestPartner

A JSON object containing store information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant&#39;s ID that is on the partner&#39;s database. | 

## Example

```python
from grabfood.models.create_self_serve_journey_request_partner import CreateSelfServeJourneyRequestPartner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSelfServeJourneyRequestPartner from a JSON string
create_self_serve_journey_request_partner_instance = CreateSelfServeJourneyRequestPartner.from_json(json)
# print the JSON string representation of the object
print(CreateSelfServeJourneyRequestPartner.to_json())

# convert the object into a dict
create_self_serve_journey_request_partner_dict = create_self_serve_journey_request_partner_instance.to_dict()
# create an instance of CreateSelfServeJourneyRequestPartner from a dict
create_self_serve_journey_request_partner_from_dict = CreateSelfServeJourneyRequestPartner.from_dict(create_self_serve_journey_request_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


