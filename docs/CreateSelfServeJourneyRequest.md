# CreateSelfServeJourneyRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner** | [**CreateSelfServeJourneyRequestPartner**](CreateSelfServeJourneyRequestPartner.md) |  | 

## Example

```python
from grabfood.models.create_self_serve_journey_request import CreateSelfServeJourneyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSelfServeJourneyRequest from a JSON string
create_self_serve_journey_request_instance = CreateSelfServeJourneyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSelfServeJourneyRequest.to_json())

# convert the object into a dict
create_self_serve_journey_request_dict = create_self_serve_journey_request_instance.to_dict()
# create an instance of CreateSelfServeJourneyRequest from a dict
create_self_serve_journey_request_from_dict = CreateSelfServeJourneyRequest.from_dict(create_self_serve_journey_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


