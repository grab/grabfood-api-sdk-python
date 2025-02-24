# Receiver

A JSON object containing the receiver information. Only applicable for orders that are delivered by the restaurant. `null` if not applicable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the receiver. | [optional] 
**phones** | **str** | The receiver&#39;s phone number. | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 

## Example

```python
from grabfood.models.receiver import Receiver

# TODO update the JSON string below
json = "{}"
# create an instance of Receiver from a JSON string
receiver_instance = Receiver.from_json(json)
# print the JSON string representation of the object
print(Receiver.to_json())

# convert the object into a dict
receiver_dict = receiver_instance.to_dict()
# create an instance of Receiver from a dict
receiver_from_dict = Receiver.from_dict(receiver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


