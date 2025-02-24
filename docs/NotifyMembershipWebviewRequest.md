# NotifyMembershipWebviewRequest

This request submits membership registration request to partner. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | The unique member ID on the partner&#39;s database. | [optional] 
**grab_id** | **str** | The id used to identify an unique grab user. | [optional] 
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | [optional] 
**action** | **str** | Action completed in partner&#39;s webview. | [optional] 

## Example

```python
from grabfood.models.notify_membership_webview_request import NotifyMembershipWebviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotifyMembershipWebviewRequest from a JSON string
notify_membership_webview_request_instance = NotifyMembershipWebviewRequest.from_json(json)
# print the JSON string representation of the object
print(NotifyMembershipWebviewRequest.to_json())

# convert the object into a dict
notify_membership_webview_request_dict = notify_membership_webview_request_instance.to_dict()
# create an instance of NotifyMembershipWebviewRequest from a dict
notify_membership_webview_request_from_dict = NotifyMembershipWebviewRequest.from_dict(notify_membership_webview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


