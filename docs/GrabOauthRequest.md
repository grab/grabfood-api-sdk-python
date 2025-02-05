# GrabOauthRequest

Information about the GrabFood client getting an OAuth 2.0 access token from partners. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The client identifier issued to the client to obtain the OAuth 2.0 access_token. | 
**client_secret** | **str** | The client secret issued to the client to obtain the OAuth 2.0 access_token. | 
**grant_type** | **str** | The grant type for the client to obtain the OAuth 2.0 access_token. | 
**scope** | **str** | The scope for the client to obtain the OAuth 2.0 access_token. | 

## Example

```python
from grabfood.models.grab_oauth_request import GrabOauthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GrabOauthRequest from a JSON string
grab_oauth_request_instance = GrabOauthRequest.from_json(json)
# print the JSON string representation of the object
print(GrabOauthRequest.to_json())

# convert the object into a dict
grab_oauth_request_dict = grab_oauth_request_instance.to_dict()
# create an instance of GrabOauthRequest from a dict
grab_oauth_request_from_dict = GrabOauthRequest.from_dict(grab_oauth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


