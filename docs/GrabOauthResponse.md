# GrabOauthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The OAuth 2.0 access token issued by the partner. | [optional] 
**token_type** | **str** | The type of token issued which is case insensitive. | [optional] 
**expires_in** | **int** | The access token lifespan in seconds. The token is reused till it expires - default is 604799 (7 days). | [optional] 

## Example

```python
from grabfood.models.grab_oauth_response import GrabOauthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GrabOauthResponse from a JSON string
grab_oauth_response_instance = GrabOauthResponse.from_json(json)
# print the JSON string representation of the object
print(GrabOauthResponse.to_json())

# convert the object into a dict
grab_oauth_response_dict = grab_oauth_response_instance.to_dict()
# create an instance of GrabOauthResponse from a dict
grab_oauth_response_from_dict = GrabOauthResponse.from_dict(grab_oauth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


