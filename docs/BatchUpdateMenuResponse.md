# BatchUpdateMenuResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | [optional] 
**status** | **str** | The status of this request. | [optional] 
**errors** | [**List[MenuEntityError]**](MenuEntityError.md) | The error messages when batch update menu record was partial success/fail. &#x60;null&#x60; when the request was success. | [optional] 

## Example

```python
from grabfood.models.batch_update_menu_response import BatchUpdateMenuResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdateMenuResponse from a JSON string
batch_update_menu_response_instance = BatchUpdateMenuResponse.from_json(json)
# print the JSON string representation of the object
print(BatchUpdateMenuResponse.to_json())

# convert the object into a dict
batch_update_menu_response_dict = batch_update_menu_response_instance.to_dict()
# create an instance of BatchUpdateMenuResponse from a dict
batch_update_menu_response_from_dict = BatchUpdateMenuResponse.from_dict(batch_update_menu_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


