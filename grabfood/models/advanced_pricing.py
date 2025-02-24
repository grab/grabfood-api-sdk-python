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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AdvancedPricing(BaseModel):
    """
    Price configuration (in minor unit) for different service, order type and channel combination. If a service type does not have a specified price, it will utilize the default price of the item. Refer [Service Based Menu](#section/Service-Based-Menu). 
    """ # noqa: E501
    delivery_on_demand_grab_app: Optional[StrictInt] = Field(default=None, description="Service type: `Delivery`, Order type: `Instant`, Channel: `Grab App` ", alias="Delivery_OnDemand_GrabApp")
    delivery_scheduled_grab_app: Optional[StrictInt] = Field(default=None, description="Service type: `Delivery`, Order type: `Scheduled`, Channel: `Grab App` ", alias="Delivery_Scheduled_GrabApp")
    self_pick_up_on_demand_grab_app: Optional[StrictInt] = Field(default=None, description="Service type: `Self Pick Up`, Order type: `Instant`, Channel: `Grab App` ", alias="SelfPickUp_OnDemand_GrabApp")
    dine_in_on_demand_grab_app: Optional[StrictInt] = Field(default=None, description="Service type: `Dine In`, Order type: `Instant`, Channel: `Grab App` ", alias="DineIn_OnDemand_GrabApp")
    delivery_on_demand_store_front: Optional[StrictInt] = Field(default=None, description="Service type: `Delivery`, Order type: `Instant`, Channel: `Store Front` ", alias="Delivery_OnDemand_StoreFront")
    delivery_scheduled_store_front: Optional[StrictInt] = Field(default=None, description="Service type: `Delivery`, Order type: `Scheduled`, Channel: `Store Front` ", alias="Delivery_Scheduled_StoreFront")
    self_pick_up_on_demand_store_front: Optional[StrictInt] = Field(default=None, description="Service type: `Self Pick Up`, Order type: `Instant`, Channel: `Store Front` ", alias="SelfPickUp_OnDemand_StoreFront")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["Delivery_OnDemand_GrabApp", "Delivery_Scheduled_GrabApp", "SelfPickUp_OnDemand_GrabApp", "DineIn_OnDemand_GrabApp", "Delivery_OnDemand_StoreFront", "Delivery_Scheduled_StoreFront", "SelfPickUp_OnDemand_StoreFront"]

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
        """Create an instance of AdvancedPricing from a JSON string"""
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
        """Create an instance of AdvancedPricing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Delivery_OnDemand_GrabApp": obj.get("Delivery_OnDemand_GrabApp"),
            "Delivery_Scheduled_GrabApp": obj.get("Delivery_Scheduled_GrabApp"),
            "SelfPickUp_OnDemand_GrabApp": obj.get("SelfPickUp_OnDemand_GrabApp"),
            "DineIn_OnDemand_GrabApp": obj.get("DineIn_OnDemand_GrabApp"),
            "Delivery_OnDemand_StoreFront": obj.get("Delivery_OnDemand_StoreFront"),
            "Delivery_Scheduled_StoreFront": obj.get("Delivery_Scheduled_StoreFront"),
            "SelfPickUp_OnDemand_StoreFront": obj.get("SelfPickUp_OnDemand_StoreFront")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


