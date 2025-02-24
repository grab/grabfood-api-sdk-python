# CancelReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**CancelCode**](CancelCode.md) |  | [optional] 
**reason** | **str** | The detailed cancel reason for the specific cancel code. - Items are unavailable &lt;code 1001&gt; - I have too many orders now &lt;code 1002&gt; - My shop is closed &lt;code 1003&gt; - My shop is closing soon &lt;code 1004&gt;  | [optional] 

## Example

```python
from grabfood.models.cancel_reason import CancelReason

# TODO update the JSON string below
json = "{}"
# create an instance of CancelReason from a JSON string
cancel_reason_instance = CancelReason.from_json(json)
# print the JSON string representation of the object
print(CancelReason.to_json())

# convert the object into a dict
cancel_reason_dict = cancel_reason_instance.to_dict()
# create an instance of CancelReason from a dict
cancel_reason_from_dict = CancelReason.from_dict(cancel_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


