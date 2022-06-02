# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class PatientQuery(EventTypeAbstractModel):

    Location: "PatientQueryLocation" = Field(None)
    Meta: "PatientQueryMeta" = Field(...)
    Patient: "PatientQueryPatient" = Field(...)


class PatientQueryLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)


class PatientQueryMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["PatientQueryMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["PatientQueryMetaLog"] = Field(None)
    Message: "PatientQueryMetaMessage" = Field(None)
    Source: "PatientQueryMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "PatientQueryMetaTransmission" = Field(None)


class PatientQueryMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PatientQueryMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class PatientQueryMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class PatientQueryMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PatientQueryMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class PatientQueryPatient(RedoxAbstractModel):

    Identifiers: List["PatientQueryPatientIdentifier"] = Field(...)


class PatientQueryPatientIdentifier(RedoxAbstractModel):

    ID: str = Field(...)
    IDType: str = Field(...)


PatientQuery.update_forward_refs()
PatientQueryMeta.update_forward_refs()
PatientQueryPatient.update_forward_refs()