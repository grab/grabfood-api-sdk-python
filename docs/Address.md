# Address

A JSON object containing the receiver’s location information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_number** | **str** | The delivery address&#39; unit number. | [optional] 
**delivery_instruction** | **str** | Instructions for the delivery. | [optional] 
**poi_source** | **str** | POI source | [optional] 
**poi_id** | **str** | POI ID, empty when poiSource is GRAB. | [optional] 
**address** | **str** | The delivery address containing street name, city, postal code, and country. Has value only when poiSource is &#x60;GRAB&#x60;. | [optional] 
**postcode** | **str** | The postcode of the delivery address. Has value only when poiSource is &#x60;GRAB&#x60;. | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 

## Example

```python
from grabfood.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


