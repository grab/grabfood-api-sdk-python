# EditOrderV2Response



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The order&#39;s ID that is returned from GrabFood. Refer to FAQs for more details about [orderID and shortOrderNumber](#section/Order/What&#39;s-the-difference-between-orderID-and-shortOrderNumber). | [optional] 
**short_order_number** | **str** | The GrabFood short order number. This is unique for each merchant per day. Refer to FAQs for more details about [orderID and shortOrderNumber](#section/Order/What&#39;s-the-difference-between-orderID-and-shortOrderNumber). | [optional] 
**merchant_id** | **str** | The merchant&#39;s ID that is in GrabFood&#39;s database. | [optional] 
**partner_merchant_id** | **str** | The merchant&#39;s ID that is on the partner&#39;s database. | [optional] 
**payment_type** | **str** | The payment method used. Refer to FAQs for more details about [paymentType](#section/Order/Does-the-paymentType-affect-partners). | [optional] 
**cutlery** | **bool** | The boolean value to indicate whether cutlery are needed or not. Refer to FAQs for more details about [cutlery](#section/Order/What-do-the-true-or-false-values-mean-for-cutlery). | [optional] 
**order_time** | **str** | The UTC time that a consumer places the order, based on ISO_8601/RFC3339. | [optional] 
**submit_time** | **datetime** | The order submit time, based on ISO_8601/RFC3339. &#x60;null&#x60; in EditOrder V2 response. Only present in the [List Orders](#tag/list-order) response. | [optional] 
**complete_time** | **datetime** | The order complete time, based on ISO_8601/RFC3339. &#x60;null&#x60; in EditOrder V2 response. Only present in the [List Orders](#tag/list-order) response. | [optional] 
**scheduled_time** | **str** | The order scheduled time, based on ISO_8601/RFC3339. Empty for non-scheduled orders. | [optional] 
**order_state** | **str** | The state of the order. Empty in EditOrder V2 response. Only present in the [List Orders](#tag/list-order) response. Refer to [Order States](#section/Order-states). | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**feature_flags** | [**OrderFeatureFlags**](OrderFeatureFlags.md) |  | [optional] 
**items** | [**List[OrderItem]**](OrderItem.md) | The ordered items in an array of JSON Object.  | [optional] 
**campaigns** | [**List[OrderCampaign]**](OrderCampaign.md) | The campaigns that are applicable for the order. &#x60;null&#x60; when there is no campaign applied. Only campaigns that are funded by merchants will be sent.  | [optional] 
**promos** | [**List[OrderPromo]**](OrderPromo.md) | An array of promotion objects. &#x60;null&#x60; when there is no promo code applied. Only promotions that are funded by merchants will be sent. | [optional] 
**price** | [**OrderPrice**](OrderPrice.md) |  | [optional] 
**dine_in** | [**DineIn**](DineIn.md) |  | [optional] 
**receiver** | **object** | This field is set to &#x60;null&#x60; in the EditOrder V2 response. Refer to the [Submit Order](#tag/submit-order-webhook/operation/submit-order-webhook) payload for the complete receiver information. | [optional] 
**order_ready_estimation** | [**OrderReadyEstimation**](OrderReadyEstimation.md) |  | [optional] 
**membership_id** | **str** | Membership ID for loyalty project. Only present for loyalty program partners. Empty if not applicable. | [optional] 
**discounts** | [**List[GrabDiscount1]**](GrabDiscount1.md) | The discounts that are applicable for the paybill order in dineout STO case. &#x60;null&#x60; when there is no discount applied. This is only applicable for STO order  | [optional] 
**payments** | **List[str]** | This field is set to &#x60;null&#x60; in the EditOrder V2 response. Refer to the [Submit Order](#tag/submit-order-webhook/operation/submit-order-webhook) payload for the complete payment details. | [optional] 

## Example

```python
from grabfood.models.edit_order_v2_response import EditOrderV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EditOrderV2Response from a JSON string
edit_order_v2_response_instance = EditOrderV2Response.from_json(json)
# print the JSON string representation of the object
print(EditOrderV2Response.to_json())

# convert the object into a dict
edit_order_v2_response_dict = edit_order_v2_response_instance.to_dict()
# create an instance of EditOrderV2Response from a dict
edit_order_v2_response_from_dict = EditOrderV2Response.from_dict(edit_order_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


