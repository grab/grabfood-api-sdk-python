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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from grabfood.models.menu_sync_fail import MenuSyncFail
from typing import Optional, Set
from typing_extensions import Self

class MenuSyncResponse(BaseModel):
    """
    
    """ # noqa: E501
    created_time: datetime = Field(description="The Unix time the specified menu was created in GrabFood's database.", alias="createdTime")
    updated_time: datetime = Field(description="The Unix time the specified menu was created in GrabFood's database.", alias="updatedTime")
    code: StrictStr = Field(description="The status code for this request. See [Menu sync response statuses](#section/Menu-sync-response-statuses) for more information.")
    errors: Optional[List[StrictStr]] = Field(default=None, description="An array of strings of error message.")
    sections: Optional[List[MenuSyncFail]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["createdTime", "updatedTime", "code", "errors", "sections"]

    @field_validator('code')
    def code_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Success', 'PartialSuccess', 'InQueuing']):
            raise ValueError("must be one of enum values ('Success', 'PartialSuccess', 'InQueuing')")
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
        """Create an instance of MenuSyncResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in sections (list)
        _items = []
        if self.sections:
            for _item_sections in self.sections:
                if _item_sections:
                    _items.append(_item_sections.to_dict())
            _dict['sections'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        # set to None if sections (nullable) is None
        # and model_fields_set contains the field
        if self.sections is None and "sections" in self.model_fields_set:
            _dict['sections'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MenuSyncResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdTime": obj.get("createdTime"),
            "updatedTime": obj.get("updatedTime"),
            "code": obj.get("code"),
            "errors": obj.get("errors"),
            "sections": [MenuSyncFail.from_dict(_item) for _item in obj["sections"]] if obj.get("sections") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


