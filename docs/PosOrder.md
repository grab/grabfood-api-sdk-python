# PosOrder

The POSOrder indicates the detail order information from POS system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The long orderID in grab system. | [optional] 
**partner_order_id** | **str** | The orderID in pos system. | [optional] 
**merchant_id** | **str** | The merchant&#39;s ID is the one in GrabFood&#39;s database. | [optional] 
**partner_merchant_id** | **str** | The merchant ID in pos system. | [optional] 
**order_time** | **datetime** | The UTC time that a consumer places the order, based on ISO_8601/RFC3339. | [optional] 
**order_state** | **str** | The order state in POS system, eg, COMPLETED. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**items** | [**List[POSItem]**](POSItem.md) | The ordered items in an array of JSON Object.  | [optional] 
**price** | [**PosPriceDetails**](PosPriceDetails.md) |  | [optional] 
**dine_in** | [**DineIn**](DineIn.md) |  | [optional] 
**payments** | [**List[Payment]**](Payment.md) | An array of payment objects. &#x60;null&#x60; when there is no payment info from pos. This is only applicable for STO order | [optional] 

## Example

```python
from grabfood.models.pos_order import PosOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PosOrder from a JSON string
pos_order_instance = PosOrder.from_json(json)
# print the JSON string representation of the object
print(PosOrder.to_json())

# convert the object into a dict
pos_order_dict = pos_order_instance.to_dict()
# create an instance of PosOrder from a dict
pos_order_from_dict = PosOrder.from_dict(pos_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


