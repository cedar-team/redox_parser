# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic.v1 import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class NaturalLanguageProcessingQuery(EventTypeAbstractModel):
    Meta: "NaturalLanguageProcessingQueryMeta" = Field(...)
    Task: "NaturalLanguageProcessingQueryTask" = Field(None)
    Text: "NaturalLanguageProcessingQueryText" = Field(None)


class NaturalLanguageProcessingQueryMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["NaturalLanguageProcessingQueryMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["NaturalLanguageProcessingQueryMetaLog"] = Field(None)
    Message: "NaturalLanguageProcessingQueryMetaMessage" = Field(None)
    Source: "NaturalLanguageProcessingQueryMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "NaturalLanguageProcessingQueryMetaTransmission" = Field(None)


class NaturalLanguageProcessingQueryMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NaturalLanguageProcessingQueryMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class NaturalLanguageProcessingQueryMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class NaturalLanguageProcessingQueryMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NaturalLanguageProcessingQueryMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class NaturalLanguageProcessingQueryTask(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)


class NaturalLanguageProcessingQueryText(RedoxAbstractModel):
    Contents: Union[str, None] = Field(None)


NaturalLanguageProcessingQuery.update_forward_refs()
NaturalLanguageProcessingQueryMeta.update_forward_refs()
