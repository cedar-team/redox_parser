# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic.v1 import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class PatientQuery(EventTypeAbstractModel):
    Meta: "PatientQueryMeta" = Field(...)
    Patient: "PatientQueryPatient" = Field(None)


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
    Demographics: "PatientQueryPatientDemographics" = Field(None)
    Identifiers: List["PatientQueryPatientIdentifier"] = Field(None)
    Notes: List[str] = Field(None)


class PatientQueryPatientDemographics(RedoxAbstractModel):
    Address: "PatientQueryPatientDemographicsAddress" = Field(None)
    Citizenship: List[str] = Field(None)
    DOB: Union[str, None] = Field(None)
    DeathDateTime: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    IsDeceased: Union[bool, None] = Field(None)
    IsHispanic: Union[bool, None] = Field(None)
    Language: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MaritalStatus: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "PatientQueryPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class PatientQueryPatientDemographicsAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PatientQueryPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class PatientQueryPatientIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


PatientQuery.update_forward_refs()
PatientQueryMeta.update_forward_refs()
PatientQueryPatient.update_forward_refs()
PatientQueryPatientDemographics.update_forward_refs()
