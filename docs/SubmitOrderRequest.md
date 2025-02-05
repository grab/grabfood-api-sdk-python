# SubmitOrderRequest

A JSON object containing the order information. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The order&#39;s ID that is returned from GrabFood. Refer to FAQs for more details about [orderID and shortOrderNumber](#section/Order/What&#39;s-the-difference-between-orderID-and-shortOrderNumber). | 
**short_order_number** | **str** | The GrabFood short order number. This is unique for each merchant per day. Refer to FAQs for more details about [orderID and shortOrderNumber](#section/Order/What&#39;s-the-difference-between-orderID-and-shortOrderNumber). | 
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | 
**partner_merchant_id** | **str** | The merchant&#39;s ID that is on the partner&#39;s database. | [optional] 
**payment_type** | **str** | The payment method used. Refer to FAQs for more details about [paymentType](#section/Order/Does-the-paymentType-affect-partners). | 
**cutlery** | **bool** | The boolean value to indicate whether cutlery are needed or not. Refer to FAQs for more details about [cutlery](#section/Order/What-do-the-true-or-false-values-mean-for-cutlery). | 
**order_time** | **str** | The UTC time that a consumer places the order, based on ISO_8601/RFC3339. | 
**submit_time** | **datetime** | The order submit time, based on ISO_8601/RFC3339. &#x60;null&#x60; in Submit Order payload. Only present in the [List Orders](#tag/list-order) response. | [optional] 
**complete_time** | **datetime** | The order complete time, based on ISO_8601/RFC3339. &#x60;null&#x60; in Submit Order payload. Only present in the [List Orders](#tag/list-order) response. | [optional] 
**scheduled_time** | **str** | The order scheduled time, based on ISO_8601/RFC3339. Empty for non-scheduled orders. | [optional] 
**order_state** | **str** | The state of the order. Empty in Submit Order payload. Only present in the [List Orders](#tag/list-order) response. Refer to [Order States](#section/Order-states). | [optional] 
**currency** | [**Currency**](Currency.md) |  | 
**feature_flags** | [**OrderFeatureFlags**](OrderFeatureFlags.md) |  | 
**items** | [**List[OrderItem]**](OrderItem.md) | The ordered items in an array of JSON Object.  | 
**campaigns** | [**List[OrderCampaign]**](OrderCampaign.md) | The campaigns that are applicable for the order. &#x60;null&#x60; when there is no campaign applied. Only campaigns that are funded by merchants will be sent.  | [optional] 
**promos** | [**List[OrderPromo]**](OrderPromo.md) | An array of promotion objects. &#x60;null&#x60; when there is no promo code applied. Only promotions that are funded by merchants will be sent. | [optional] 
**price** | [**OrderPrice**](OrderPrice.md) |  | 
**dine_in** | [**DineIn**](DineIn.md) |  | [optional] 
**receiver** | [**Receiver**](Receiver.md) |  | [optional] 
**order_ready_estimation** | [**OrderReadyEstimation**](OrderReadyEstimation.md) |  | [optional] 
**membership_id** | **str** | Membership ID for loyalty project. Only present for loyalty program partners. Empty if not applicable. | [optional] 

## Example

```python
from grabfood.models.submit_order_request import SubmitOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitOrderRequest from a JSON string
submit_order_request_instance = SubmitOrderRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitOrderRequest.to_json())

# convert the object into a dict
submit_order_request_dict = submit_order_request_instance.to_dict()
# create an instance of SubmitOrderRequest from a dict
submit_order_request_from_dict = SubmitOrderRequest.from_dict(submit_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


