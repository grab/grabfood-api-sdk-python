# SellingTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** | The selling time group start time in date &amp; time format. UTC format is expected.  | [optional] 
**end_time** | **str** | The selling time group end time in date &amp; time format. UTC format is expected.  | [optional] 
**id** | **str** | The selling time&#39;s ID on the partner system. This ID should be unique with length min 1 and max 64.  | [optional] 
**name** | **str** | The name of the selling time.  | [optional] 
**service_hours** | [**ServiceHours**](ServiceHours.md) |  | [optional] 

## Example

```python
from grabfood.models.selling_time import SellingTime

# TODO update the JSON string below
json = "{}"
# create an instance of SellingTime from a JSON string
selling_time_instance = SellingTime.from_json(json)
# print the JSON string representation of the object
print(SellingTime.to_json())

# convert the object into a dict
selling_time_dict = selling_time_instance.to_dict()
# create an instance of SellingTime from a dict
selling_time_from_dict = SellingTime.from_dict(selling_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


