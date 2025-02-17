# CreateSelfServeJourneyResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_url** | **str** | A JSON object containing store information | 

## Example

```python
from grabfood.models.create_self_serve_journey_response import CreateSelfServeJourneyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSelfServeJourneyResponse from a JSON string
create_self_serve_journey_response_instance = CreateSelfServeJourneyResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSelfServeJourneyResponse.to_json())

# convert the object into a dict
create_self_serve_journey_response_dict = create_self_serve_journey_response_instance.to_dict()
# create an instance of CreateSelfServeJourneyResponse from a dict
create_self_serve_journey_response_from_dict = CreateSelfServeJourneyResponse.from_dict(create_self_serve_journey_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


