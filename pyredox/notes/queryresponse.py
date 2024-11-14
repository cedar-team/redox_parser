# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic.v1 import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class QueryResponse(EventTypeAbstractModel):
    Meta: "QueryResponseMeta" = Field(...)
    Notes: List["QueryResponseNote"] = Field(None)


class QueryResponseMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["QueryResponseMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["QueryResponseMetaLog"] = Field(None)
    Message: "QueryResponseMetaMessage" = Field(None)
    Source: "QueryResponseMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "QueryResponseMetaTransmission" = Field(None)


class QueryResponseMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class QueryResponseMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class QueryResponseMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class QueryResponseMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class QueryResponseMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class QueryResponseNote(RedoxAbstractModel):
    ContentType: Union[str, None] = Field(None)
    DocumentID: Union[str, None] = Field(None)
    DocumentType: Union[str, None] = Field(None)
    DocumentationDateTime: Union[str, None] = Field(None)
    FileContents: Union[str, None] = Field(None)
    FileName: Union[str, None] = Field(None)
    Patient: "QueryResponseNotePatient" = Field(None)
    ServiceDateTime: Union[str, None] = Field(None)
    Visit: "QueryResponseNoteVisit" = Field(None)


class QueryResponseNotePatient(RedoxAbstractModel):
    Identifiers: List["QueryResponseNotePatientIdentifier"] = Field(None)


class QueryResponseNotePatientIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class QueryResponseNoteVisit(RedoxAbstractModel):
    VisitNumber: Union[str, None] = Field(None)


QueryResponse.update_forward_refs()
QueryResponseMeta.update_forward_refs()
QueryResponseNote.update_forward_refs()
QueryResponseNotePatient.update_forward_refs()
