# coding: utf-8

"""
Copyright 2024 Grabtaxi Holdings PTE LTE (GRAB), All rights reserved.
Use of this source code is governed by an MIT-style license that can be found in the LICENSE file

GrabFood

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

API version: 1.1.3

 Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Currency(BaseModel):
    """
    A JSON object containing code, symbol, and exponent for a given currency. Refer to [Country and Currency](#section/Getting-started/Country-and-currency).
    """ # noqa: E501
    code: Annotated[str, Field(strict=True, max_length=3)] = Field(description="The three-letter ISO currency code. This is the currency that is associated with the payment amount. ")
    symbol: Annotated[str, Field(strict=True, max_length=3)] = Field(description="The currency symbol. ")
    exponent: StrictInt = Field(description="The log base 10 of the number of times we have to multiply the major unit to get the minor unit. Should be 0 for VN and 2 for other countries (`SG`/`MY`/`ID`/`TH`/`PH`/`KH`/`MM`). ")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["code", "symbol", "exponent"]

    @field_validator('code')
    def code_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['IDR', 'MYR', 'PHP', 'SGD', 'THB', 'VND', 'KHR', 'MMK']):
            raise ValueError("must be one of enum values ('IDR', 'MYR', 'PHP', 'SGD', 'THB', 'VND', 'KHR', 'MMK')")
        return value

    @field_validator('symbol')
    def symbol_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Rp', 'RM', '₱', 'S$', '฿', '₫', '៛', 'K']):
            raise ValueError("must be one of enum values ('Rp', 'RM', '₱', 'S$', '฿', '₫', '៛', 'K')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Currency from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Currency from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "symbol": obj.get("symbol"),
            "exponent": obj.get("exponent")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


