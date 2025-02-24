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
from grabfood.models.special_opening_hour_metadata import SpecialOpeningHourMetadata
from grabfood.models.special_opening_hour_opening_hours import SpecialOpeningHourOpeningHours
from typing import Optional, Set
from typing_extensions import Self

class SpecialOpeningHour(BaseModel):
    """
    SpecialOpeningHour
    """ # noqa: E501
    start_date: Optional[StrictStr] = Field(default=None, description="The start date of store special opening hours.", alias="startDate")
    end_date: Optional[StrictStr] = Field(default=None, description="The end date of store special opening hours.", alias="endDate")
    metadata: Optional[SpecialOpeningHourMetadata] = None
    opening_hours: Optional[SpecialOpeningHourOpeningHours] = Field(default=None, alias="openingHours")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["startDate", "endDate", "metadata", "openingHours"]

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
        """Create an instance of SpecialOpeningHour from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of opening_hours
        if self.opening_hours:
            _dict['openingHours'] = self.opening_hours.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpecialOpeningHour from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "metadata": SpecialOpeningHourMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "openingHours": SpecialOpeningHourOpeningHours.from_dict(obj["openingHours"]) if obj.get("openingHours") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


