# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from redox_parser import patientadmin
from ..abstract_base import GenericEventTypeAbstractModel
from . import types as generic


class _PatientAdmin(GenericEventTypeAbstractModel):
    _redox_module = patientadmin


class Arrival(_PatientAdmin):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class Cancel(_PatientAdmin):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class CensusQuery(_PatientAdmin):
    Departments: List[str] = Field(None)
    Facilities: List[str] = Field(None)
    Meta: generic.Meta = Field(...)
    PatientClasses: List[str] = Field(None)


class CensusQueryResponse(_PatientAdmin):
    Meta: generic.Meta = Field(...)
    Patients: List[generic.Patient] = Field(None)


class Discharge(_PatientAdmin):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class NewPatient(_PatientAdmin):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)


class PatientMerge(_PatientAdmin):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)


class PatientUpdate(_PatientAdmin):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)


class PreAdmit(_PatientAdmin):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class Registration(_PatientAdmin):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class Transfer(_PatientAdmin):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class VisitMerge(_PatientAdmin):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(...)


class VisitQuery(_PatientAdmin):
    Departments: List[str] = Field(None)
    Facilities: List[str] = Field(None)
    Meta: generic.Meta = Field(...)
    PatientClasses: List[str] = Field(None)
    Patients: List[generic.Patient] = Field(None)
    VisitNumbers: List[str] = Field(None)
    VisitStartDateTime: Union[str, None] = Field(None)
    VisitStatuses: List[str] = Field(None)


class VisitQueryResponse(_PatientAdmin):
    Meta: generic.Meta = Field(...)
    Patients: List[generic.Patient] = Field(None)


class VisitUpdate(_PatientAdmin):
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)
