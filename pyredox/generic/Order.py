# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from redox_parser import order
from ..abstract_base import GenericEventTypeAbstractModel
from . import types as generic


class _Order(GenericEventTypeAbstractModel):
    _redox_module = order


class Cancel(_Order):
    Meta: generic.Meta = Field(...)
    Order: generic.Order = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class GroupedOrders(_Order):
    Meta: generic.Meta = Field(...)
    Orders: List[generic.Order] = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class New(_Order):
    Meta: generic.Meta = Field(...)
    Order: generic.Order = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class Query(_Order):
    EndDateTime: Union[str, None] = Field(None)
    Meta: generic.Meta = Field(...)
    OrderIDs: List[str] = Field(None)
    Patients: List[generic.Patient] = Field(None)
    Procedures: List[generic.Procedure] = Field(None)
    StartDateTime: Union[str, None] = Field(None)
    VisitNumbers: List[str] = Field(None)


class QueryResponse(_Order):
    Meta: generic.Meta = Field(...)
    Orders: List[generic.Order] = Field(None)


class Update(_Order):
    Meta: generic.Meta = Field(...)
    Order: generic.Order = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)
