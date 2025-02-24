# UpdateMenuNotifRequest

This request notifies GrabFood about the partner's updated food menu. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | 

## Example

```python
from grabfood.models.update_menu_notif_request import UpdateMenuNotifRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMenuNotifRequest from a JSON string
update_menu_notif_request_instance = UpdateMenuNotifRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMenuNotifRequest.to_json())

# convert the object into a dict
update_menu_notif_request_dict = update_menu_notif_request_instance.to_dict()
# create an instance of UpdateMenuNotifRequest from a dict
update_menu_notif_request_from_dict = UpdateMenuNotifRequest.from_dict(update_menu_notif_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


