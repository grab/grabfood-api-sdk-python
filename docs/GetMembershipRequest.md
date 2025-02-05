# GetMembershipRequest

This request submits membership unbind request to partner. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | The unique member ID on the partner&#39;s database. | 

## Example

```python
from grabfood.models.get_membership_request import GetMembershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMembershipRequest from a JSON string
get_membership_request_instance = GetMembershipRequest.from_json(json)
# print the JSON string representation of the object
print(GetMembershipRequest.to_json())

# convert the object into a dict
get_membership_request_dict = get_membership_request_instance.to_dict()
# create an instance of GetMembershipRequest from a dict
get_membership_request_from_dict = GetMembershipRequest.from_dict(get_membership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


