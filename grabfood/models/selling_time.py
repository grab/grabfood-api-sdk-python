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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from grabfood.models.service_hours import ServiceHours
from typing import Optional, Set
from typing_extensions import Self

class SellingTime(BaseModel):
    """
    SellingTime
    """ # noqa: E501
    start_time: Optional[StrictStr] = Field(default=None, description="The selling time group start time in date & time format. UTC format is expected. ", alias="startTime")
    end_time: Optional[StrictStr] = Field(default=None, description="The selling time group end time in date & time format. UTC format is expected. ", alias="endTime")
    id: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="The selling time's ID on the partner system. This ID should be unique with length min 1 and max 64. ")
    name: Optional[Annotated[str, Field(strict=True, max_length=30)]] = Field(default=None, description="The name of the selling time. ")
    service_hours: Optional[ServiceHours] = Field(default=None, alias="serviceHours")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["startTime", "endTime", "id", "name", "serviceHours"]

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
        """Create an instance of SellingTime from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of service_hours
        if self.service_hours:
            _dict['serviceHours'] = self.service_hours.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SellingTime from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "serviceHours": ServiceHours.from_dict(obj["serviceHours"]) if obj.get("serviceHours") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


