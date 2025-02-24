# PartnerOauthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The OAuth 2.0 access token issued by the partner. | [optional] 
**token_type** | **str** | The type of token issued which is case insensitive. | [optional] 
**expires_in** | **int** | The access token lifespan in seconds. | [optional] 

## Example

```python
from grabfood.models.partner_oauth_response import PartnerOauthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerOauthResponse from a JSON string
partner_oauth_response_instance = PartnerOauthResponse.from_json(json)
# print the JSON string representation of the object
print(PartnerOauthResponse.to_json())

# convert the object into a dict
partner_oauth_response_dict = partner_oauth_response_instance.to_dict()
# create an instance of PartnerOauthResponse from a dict
partner_oauth_response_from_dict = PartnerOauthResponse.from_dict(partner_oauth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


