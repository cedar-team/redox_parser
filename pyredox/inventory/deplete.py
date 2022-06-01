# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Deplete(EventTypeAbstractModel):

    Items: List["DepleteItem"] = Field(...)
    Meta: "DepleteMeta" = Field(...)
    Patient: "DepletePatient" = Field(None)
    Visit: "DepleteVisit" = Field(None)


class DepleteItem(RedoxAbstractModel):

    Description: Union[str, None] = Field(None)
    Identifiers: List["DepleteItemIdentifier"] = Field(...)
    Location: "DepleteItemLocation" = Field(None)
    LotNumber: Union[str, None] = Field(None)
    Notes: Union[str, None] = Field(None)
    OrderingProvider: "DepleteItemOrderingProvider" = Field(None)
    Procedure: "DepleteItemProcedure" = Field(None)
    Quantity: Union[Number, None] = Field(None)
    SerialNumber: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)
    Units: Union[str, None] = Field(None)
    UsedQuantity: Union[Number, None] = Field(None)
    Vendor: "DepleteItemVendor" = Field(None)
    WastedQuantity: Union[Number, None] = Field(None)


class DepleteItemIdentifier(RedoxAbstractModel):

    ID: str = Field(...)
    IDType: str = Field(...)


class DepleteItemLocation(RedoxAbstractModel):

    Bin: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class DepleteItemOrderingProvider(RedoxAbstractModel):

    Address: "DepleteItemOrderingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "DepleteItemOrderingProviderLocation" = Field(None)
    PhoneNumber: "DepleteItemOrderingProviderPhoneNumber" = Field(None)


class DepleteItemOrderingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DepleteItemOrderingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class DepleteItemOrderingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class DepleteItemProcedure(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Modifier: Union[str, None] = Field(None)


class DepleteItemVendor(RedoxAbstractModel):

    CatalogNumber: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class DepleteMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["DepleteMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["DepleteMetaLog"] = Field(None)
    Message: "DepleteMetaMessage" = Field(None)
    Source: "DepleteMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "DepleteMetaTransmission" = Field(None)


class DepleteMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class DepleteMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class DepleteMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class DepleteMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class DepleteMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class DepletePatient(RedoxAbstractModel):

    Demographics: "DepletePatientDemographics" = Field(None)
    Identifiers: List["DepletePatientIdentifier"] = Field(None)
    Notes: List[str] = Field(None)


class DepletePatientDemographics(RedoxAbstractModel):

    Address: "DepletePatientDemographicsAddress" = Field(None)
    Citizenship: List[str] = Field(None)
    DeathDateTime: Union[str, None] = Field(None)
    DOB: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    IsDeceased: Union[bool, None] = Field(None)
    IsHispanic: Union[bool, None] = Field(None)
    Language: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MaritalStatus: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "DepletePatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)


class DepletePatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class DepletePatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class DepletePatientIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class DepleteVisit(RedoxAbstractModel):

    VisitNumber: Union[str, None] = Field(None)


Deplete.update_forward_refs()
DepleteItem.update_forward_refs()
DepleteItemOrderingProvider.update_forward_refs()
DepleteMeta.update_forward_refs()
DepletePatient.update_forward_refs()
DepletePatientDemographics.update_forward_refs()
