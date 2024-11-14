# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic.v1 import Field

from pyredox import patienteducation
from ..abstract_base import GenericEventTypeAbstractModel
from . import types as generic


class _PatientEducation(GenericEventTypeAbstractModel):
    _redox_module = patienteducation


class Delete(_PatientEducation):
    Education: List[generic.Education] = Field(...)
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class New(_PatientEducation):
    Education: List[generic.Education] = Field(...)
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class Update(_PatientEducation):
    Education: List[generic.Education] = Field(...)
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)
