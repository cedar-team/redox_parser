# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic.v1 import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class QueryResponse(EventTypeAbstractModel):
    Meta: "QueryResponseMeta" = Field(...)
    Referrals: List["QueryResponseReferral"] = Field(None)


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


class QueryResponseReferral(RedoxAbstractModel):
    AlternateID: Union[str, None] = Field(None)
    Authorization: "QueryResponseReferralAuthorization" = Field(None)
    Category: Union[str, None] = Field(None)
    DateTime: Union[str, None] = Field(None)
    DepartmentSpecialty: Union[str, None] = Field(None)
    Diagnoses: List["QueryResponseReferralDiagnosis"] = Field(None)
    ExpirationDateTime: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    Priority: Union[str, None] = Field(None)
    Procedures: List["QueryResponseReferralProcedure"] = Field(None)
    ProcessDateTime: Union[str, None] = Field(None)
    ProviderSpecialty: Union[str, None] = Field(None)
    Providers: List["QueryResponseReferralProvider"] = Field(None)
    Reason: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)
    Visit: "QueryResponseReferralVisit" = Field(None)


class QueryResponseReferralAuthorization(RedoxAbstractModel):
    AuthorizedTreatmentCount: Union[str, None] = Field(None)
    Company: "QueryResponseReferralAuthorizationCompany" = Field(None)
    DateTime: Union[str, None] = Field(None)
    ExpirationDateTime: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    Number: Union[str, None] = Field(None)
    Plan: "QueryResponseReferralAuthorizationPlan" = Field(None)
    ReimbursementLimit: Union[str, None] = Field(None)
    RequestedTreatmentCount: Union[str, None] = Field(None)
    RequestedTreatmentUnits: Union[str, None] = Field(None)


class QueryResponseReferralAuthorizationCompany(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class QueryResponseReferralAuthorizationPlan(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class QueryResponseReferralDiagnosis(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    Type: Union[str, None] = Field(None)


class QueryResponseReferralProcedure(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Modifiers: List[str] = Field(None)
    Notes: List[str] = Field(None)
    Quantity: Union[str, None] = Field(None)
    Units: Union[str, None] = Field(None)


class QueryResponseReferralProvider(RedoxAbstractModel):
    Address: "QueryResponseReferralProviderAddress" = Field(None)
    ContactInfo: Union[str, None] = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "QueryResponseReferralProviderLocation" = Field(None)
    PhoneNumber: "QueryResponseReferralProviderPhoneNumber" = Field(None)
    Type: Union[str, None] = Field(None)


class QueryResponseReferralProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class QueryResponseReferralProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "QueryResponseReferralProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "QueryResponseReferralProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class QueryResponseReferralProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class QueryResponseReferralProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class QueryResponseReferralProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class QueryResponseReferralVisit(RedoxAbstractModel):
    VisitNumber: Union[str, None] = Field(None)


QueryResponse.update_forward_refs()
QueryResponseMeta.update_forward_refs()
QueryResponseReferral.update_forward_refs()
QueryResponseReferralAuthorization.update_forward_refs()
QueryResponseReferralProvider.update_forward_refs()
QueryResponseReferralProviderLocation.update_forward_refs()
