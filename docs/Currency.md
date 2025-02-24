# Currency

A JSON object containing code, symbol, and exponent for a given currency. Refer to [Country and Currency](#section/Getting-started/Country-and-currency).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The three-letter ISO currency code. This is the currency that is associated with the payment amount.  | 
**symbol** | **str** | The currency symbol.  | 
**exponent** | **int** | The log base 10 of the number of times we have to multiply the major unit to get the minor unit. Should be 0 for VN and 2 for other countries (&#x60;SG&#x60;/&#x60;MY&#x60;/&#x60;ID&#x60;/&#x60;TH&#x60;/&#x60;PH&#x60;/&#x60;KH&#x60;/&#x60;MM&#x60;).  | 

## Example

```python
from grabfood.models.currency import Currency

# TODO update the JSON string below
json = "{}"
# create an instance of Currency from a JSON string
currency_instance = Currency.from_json(json)
# print the JSON string representation of the object
print(Currency.to_json())

# convert the object into a dict
currency_dict = currency_instance.to_dict()
# create an instance of Currency from a dict
currency_from_dict = Currency.from_dict(currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


