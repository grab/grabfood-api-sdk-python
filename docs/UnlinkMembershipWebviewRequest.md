# UnlinkMembershipWebviewRequest

This request submits membership unbind request to partner. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | The unique member ID on the partner&#39;s database. | 

## Example

```python
from grabfood.models.unlink_membership_webview_request import UnlinkMembershipWebviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnlinkMembershipWebviewRequest from a JSON string
unlink_membership_webview_request_instance = UnlinkMembershipWebviewRequest.from_json(json)
# print the JSON string representation of the object
print(UnlinkMembershipWebviewRequest.to_json())

# convert the object into a dict
unlink_membership_webview_request_dict = unlink_membership_webview_request_instance.to_dict()
# create an instance of UnlinkMembershipWebviewRequest from a dict
unlink_membership_webview_request_from_dict = UnlinkMembershipWebviewRequest.from_dict(unlink_membership_webview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


