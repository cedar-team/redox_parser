# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic.v1 import Field

from pyredox import inventory
from ..abstract_base import GenericEventTypeAbstractModel
from . import types as generic


class _Inventory(GenericEventTypeAbstractModel):
    _redox_module = inventory


class Deplete(_Inventory):
    Items: List[generic.Item] = Field(...)
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(None)
    Visit: generic.Visit = Field(None)


class Update(_Inventory):
    Items: List[generic.Item] = Field(...)
    Meta: generic.Meta = Field(...)
