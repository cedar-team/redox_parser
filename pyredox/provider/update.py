# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic.v1 import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Update(EventTypeAbstractModel):
    Meta: "UpdateMeta" = Field(...)
    Providers: List["UpdateProvider"] = Field(...)


class UpdateMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["UpdateMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["UpdateMetaLog"] = Field(None)
    Message: "UpdateMetaMessage" = Field(None)
    Source: "UpdateMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "UpdateMetaTransmission" = Field(None)


class UpdateMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdateMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class UpdateMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class UpdateMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class UpdateMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class UpdateProvider(RedoxAbstractModel):
    Demographics: "UpdateProviderDemographics" = Field(None)
    Identifiers: List["UpdateProviderIdentifier"] = Field(...)
    IsActive: bool = Field(...)
    Qualifications: List["UpdateProviderQualification"] = Field(None)
    Roles: List["UpdateProviderRole"] = Field(None)


class UpdateProviderDemographics(RedoxAbstractModel):
    Addresses: List["UpdateProviderDemographicsAddress"] = Field(None)
    Credentials: List[str] = Field(None)
    DOB: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    Languages: List[str] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "UpdateProviderDemographicsPhoneNumber" = Field(None)
    Sex: Union[str, None] = Field(None)


class UpdateProviderDemographicsAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    Use: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateProviderDemographicsPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class UpdateProviderIdentifier(RedoxAbstractModel):
    ID: str = Field(...)
    IDType: Union[str, None] = Field(None)


class UpdateProviderQualification(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    EndDate: Union[str, None] = Field(None)
    Identifiers: List["UpdateProviderQualificationIdentifier"] = Field(None)
    StartDate: Union[str, None] = Field(None)


class UpdateProviderQualificationIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateProviderRole(RedoxAbstractModel):
    Availability: List["UpdateProviderRoleAvailability"] = Field(None)
    Identifiers: List["UpdateProviderRoleIdentifier"] = Field(None)
    Locations: List["UpdateProviderRoleLocation"] = Field(None)
    Organization: "UpdateProviderRoleOrganization" = Field(None)
    Services: List["UpdateProviderRoleService"] = Field(None)
    Specialties: List["UpdateProviderRoleSpecialty"] = Field(None)


class UpdateProviderRoleAvailability(RedoxAbstractModel):
    AvailableEndTime: Union[str, None] = Field(None)
    AvailableStartTime: Union[str, None] = Field(None)
    Days: List[str] = Field(None)


class UpdateProviderRoleIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateProviderRoleLocation(RedoxAbstractModel):
    Address: "UpdateProviderRoleLocationAddress" = Field(None)
    Description: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    Identifiers: List["UpdateProviderRoleLocationIdentifier"] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: "UpdateProviderRoleLocationPhoneNumber" = Field(None)
    Status: Union[str, None] = Field(None)


class UpdateProviderRoleLocationAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateProviderRoleLocationIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateProviderRoleLocationPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class UpdateProviderRoleOrganization(RedoxAbstractModel):
    Address: "UpdateProviderRoleOrganizationAddress" = Field(None)
    Identifiers: List["UpdateProviderRoleOrganizationIdentifier"] = Field(None)
    IsActive: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateProviderRoleOrganizationAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateProviderRoleOrganizationIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateProviderRoleService(RedoxAbstractModel):
    Description: Union[str, None] = Field(None)
    Identifiers: List["UpdateProviderRoleServiceIdentifier"] = Field(None)
    PhoneNumber: "UpdateProviderRoleServicePhoneNumber" = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateProviderRoleServiceIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateProviderRoleServicePhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class UpdateProviderRoleSpecialty(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


Update.update_forward_refs()
UpdateMeta.update_forward_refs()
UpdateProvider.update_forward_refs()
UpdateProviderDemographics.update_forward_refs()
UpdateProviderQualification.update_forward_refs()
UpdateProviderRole.update_forward_refs()
UpdateProviderRoleLocation.update_forward_refs()
UpdateProviderRoleOrganization.update_forward_refs()
UpdateProviderRoleService.update_forward_refs()
