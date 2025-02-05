# GetMembershipWebviewResponse

This response returns membership detail. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_status** | **str** | Status of the memberID. | [optional] 

## Example

```python
from grabfood.models.get_membership_webview_response import GetMembershipWebviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMembershipWebviewResponse from a JSON string
get_membership_webview_response_instance = GetMembershipWebviewResponse.from_json(json)
# print the JSON string representation of the object
print(GetMembershipWebviewResponse.to_json())

# convert the object into a dict
get_membership_webview_response_dict = get_membership_webview_response_instance.to_dict()
# create an instance of GetMembershipWebviewResponse from a dict
get_membership_webview_response_from_dict = GetMembershipWebviewResponse.from_dict(get_membership_webview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


