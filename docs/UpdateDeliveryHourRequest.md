# UpdateDeliveryHourRequest

Object contains store delivery hours.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opening_hour** | [**StoreHour**](StoreHour.md) |  | 
**force** | **bool** | To enable force update store delivery hours. Error will be returned if set to false while there is ongoing order. | 

## Example

```python
from grabfood.models.update_delivery_hour_request import UpdateDeliveryHourRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDeliveryHourRequest from a JSON string
update_delivery_hour_request_instance = UpdateDeliveryHourRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDeliveryHourRequest.to_json())

# convert the object into a dict
update_delivery_hour_request_dict = update_delivery_hour_request_instance.to_dict()
# create an instance of UpdateDeliveryHourRequest from a dict
update_delivery_hour_request_from_dict = UpdateDeliveryHourRequest.from_dict(update_delivery_hour_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


