# OutOfStockInstruction

An JSON object that indicates the instructions to be taken by the merchant when the item is out of stock.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The short instruction message. | [optional] 
**instruction_type** | **str** | Type of out-of-stock instruction chosen by customer. &#x60;CONTACT&#x60; is disabled by default, kindly reach out to your integration manager if you wish to receive this instruction. | [optional] 
**replacement_item_id** | **str** | The preferred item&#39;s ID in the partner system. Only applicable when the instructionType is &#x60;SPECIFIC_ITEM&#x60;. | [optional] 
**replacement_grab_item_id** | **str** | The preferred item&#39;s ID in the Grab system. Only applicable when the instructionType is &#x60;SPECIFIC_ITEM&#x60;. | [optional] 

## Example

```python
from grabfood.models.out_of_stock_instruction import OutOfStockInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of OutOfStockInstruction from a JSON string
out_of_stock_instruction_instance = OutOfStockInstruction.from_json(json)
# print the JSON string representation of the object
print(OutOfStockInstruction.to_json())

# convert the object into a dict
out_of_stock_instruction_dict = out_of_stock_instruction_instance.to_dict()
# create an instance of OutOfStockInstruction from a dict
out_of_stock_instruction_from_dict = OutOfStockInstruction.from_dict(out_of_stock_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


