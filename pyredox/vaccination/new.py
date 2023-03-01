# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class New(EventTypeAbstractModel):
    Meta: "NewMeta" = Field(...)
    Patient: "NewPatient" = Field(...)
    Vaccinations: List["NewVaccination"] = Field(...)
    Visit: "NewVisit" = Field(None)


class NewMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["NewMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["NewMetaLog"] = Field(None)
    Message: "NewMetaMessage" = Field(None)
    Source: "NewMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "NewMetaTransmission" = Field(None)


class NewMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class NewMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class NewMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class NewPatient(RedoxAbstractModel):
    Consent: "NewPatientConsent" = Field(None)
    Contacts: List["NewPatientContact"] = Field(None)
    Demographics: "NewPatientDemographics" = Field(None)
    Identifiers: List["NewPatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)


class NewPatientConsent(RedoxAbstractModel):
    EffectiveDate: Union[str, None] = Field(None)
    Notification: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)


class NewPatientContact(RedoxAbstractModel):
    Address: "NewPatientContactAddress" = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "NewPatientContactPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    Roles: List[str] = Field(None)


class NewPatientContactAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewPatientContactPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class NewPatientDemographics(RedoxAbstractModel):
    Address: "NewPatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "NewPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class NewPatientDemographicsAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class NewPatientIdentifier(RedoxAbstractModel):
    ID: str = Field(...)
    IDType: str = Field(...)


class NewVaccination(RedoxAbstractModel):
    ClinicalInfo: List["NewVaccinationClinicalInfo"] = Field(None)
    DateTime: str = Field(...)
    Dose: "NewVaccinationDose" = Field(None)
    Location: "NewVaccinationLocation" = Field(None)
    Notes: List[str] = Field(None)
    Order: "NewVaccinationOrder" = Field(None)
    Product: "NewVaccinationProduct" = Field(...)
    Provider: "NewVaccinationProvider" = Field(None)
    RefusalReason: Union[str, None] = Field(None)
    Route: "NewVaccinationRoute" = Field(None)
    Site: "NewVaccinationSite" = Field(None)


class NewVaccinationClinicalInfo(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    CompletionDateTime: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    RelatedGroupID: Union[str, None] = Field(None)
    Units: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)
    ValueType: Union[str, None] = Field(None)


class NewVaccinationDose(RedoxAbstractModel):
    Quantity: Union[str, None] = Field(None)
    Units: Union[str, None] = Field(None)


class NewVaccinationLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List["NewVaccinationLocationDepartmentIdentifier"] = Field(
        None
    )
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["NewVaccinationLocationFacilityIdentifier"] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewVaccinationLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class NewVaccinationLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class NewVaccinationOrder(RedoxAbstractModel):
    EHRID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    Provider: "NewVaccinationOrderProvider" = Field(None)


class NewVaccinationOrderProvider(RedoxAbstractModel):
    Address: "NewVaccinationOrderProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewVaccinationOrderProviderLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "NewVaccinationOrderProviderPhoneNumber" = Field(None)


class NewVaccinationOrderProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewVaccinationOrderProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "NewVaccinationOrderProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "NewVaccinationOrderProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewVaccinationOrderProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class NewVaccinationOrderProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class NewVaccinationOrderProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class NewVaccinationProduct(RedoxAbstractModel):
    Code: str = Field(...)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    LotNumber: Union[str, None] = Field(None)
    Manufacturer: "NewVaccinationProductManufacturer" = Field(None)


class NewVaccinationProductManufacturer(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewVaccinationProvider(RedoxAbstractModel):
    Address: "NewVaccinationProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewVaccinationProviderLocation" = Field(None)
    PhoneNumber: "NewVaccinationProviderPhoneNumber" = Field(None)


class NewVaccinationProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewVaccinationProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "NewVaccinationProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "NewVaccinationProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewVaccinationProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class NewVaccinationProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class NewVaccinationProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class NewVaccinationRoute(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewVaccinationSite(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewVisit(RedoxAbstractModel):
    AccountNumber: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


New.update_forward_refs()
NewMeta.update_forward_refs()
NewPatient.update_forward_refs()
NewPatientContact.update_forward_refs()
NewPatientDemographics.update_forward_refs()
NewVaccination.update_forward_refs()
NewVaccinationLocation.update_forward_refs()
NewVaccinationOrder.update_forward_refs()
NewVaccinationOrderProvider.update_forward_refs()
NewVaccinationOrderProviderLocation.update_forward_refs()
NewVaccinationProduct.update_forward_refs()
NewVaccinationProvider.update_forward_refs()
NewVaccinationProviderLocation.update_forward_refs()
