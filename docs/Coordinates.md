# Coordinates

A JSON object containing the coordinates of the delivery address. Only has value when poiSource is `GRAB`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | The latitude coordinates of the delivery address. | [optional] 
**longitude** | **float** | The longitude coordinates of the delivery address. | [optional] 

## Example

```python
from grabfood.models.coordinates import Coordinates

# TODO update the JSON string below
json = "{}"
# create an instance of Coordinates from a JSON string
coordinates_instance = Coordinates.from_json(json)
# print the JSON string representation of the object
print(Coordinates.to_json())

# convert the object into a dict
coordinates_dict = coordinates_instance.to_dict()
# create an instance of Coordinates from a dict
coordinates_from_dict = Coordinates.from_dict(coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


