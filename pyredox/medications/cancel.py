# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic.v1 import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Cancel(EventTypeAbstractModel):
    Meta: "CancelMeta" = Field(...)
    Order: "CancelOrder" = Field(...)
    Patient: "CancelPatient" = Field(...)
    Visit: "CancelVisit" = Field(None)


class CancelMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["CancelMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["CancelMetaLog"] = Field(None)
    Message: "CancelMetaMessage" = Field(None)
    Source: "CancelMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "CancelMetaTransmission" = Field(None)


class CancelMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class CancelMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class CancelMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class CancelOrder(RedoxAbstractModel):
    EnteredBy: "CancelOrderEnteredBy" = Field(None)
    ID: str = Field(...)
    Indications: List["CancelOrderIndication"] = Field(None)
    Medication: "CancelOrderMedication" = Field(...)
    Notes: List[str] = Field(None)
    Pharmacy: "CancelOrderPharmacy" = Field(None)
    Priority: Union[str, None] = Field(None)
    Provider: "CancelOrderProvider" = Field(None)
    VerifiedBy: "CancelOrderVerifiedBy" = Field(None)


class CancelOrderEnteredBy(RedoxAbstractModel):
    Address: "CancelOrderEnteredByAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "CancelOrderEnteredByLocation" = Field(None)
    PhoneNumber: "CancelOrderEnteredByPhoneNumber" = Field(None)


class CancelOrderEnteredByAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelOrderEnteredByLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "CancelOrderEnteredByLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["CancelOrderEnteredByLocationFacilityIdentifier"] = Field(
        None
    )
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelOrderEnteredByLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelOrderEnteredByLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelOrderEnteredByPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class CancelOrderIndication(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class CancelOrderMedication(RedoxAbstractModel):
    Components: List["CancelOrderMedicationComponent"] = Field(None)
    Dispense: "CancelOrderMedicationDispense" = Field(None)
    Dose: "CancelOrderMedicationDose" = Field(None)
    EndDate: Union[str, None] = Field(None)
    FreeTextSig: Union[str, None] = Field(None)
    Frequency: "CancelOrderMedicationFrequency" = Field(None)
    IsPRN: Union[bool, None] = Field(None)
    NumberOfRefillsRemaining: Union[Number, None] = Field(None)
    Product: "CancelOrderMedicationProduct" = Field(...)
    Rate: "CancelOrderMedicationRate" = Field(None)
    Route: "CancelOrderMedicationRoute" = Field(None)
    StartDate: Union[str, None] = Field(None)


class CancelOrderMedicationComponent(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Dose: "CancelOrderMedicationComponentDose" = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelOrderMedicationComponentDose(RedoxAbstractModel):
    Quantity: Union[Number, None] = Field(None)
    Units: Union[str, None] = Field(None)


class CancelOrderMedicationDispense(RedoxAbstractModel):
    Amount: Union[Number, None] = Field(None)
    Units: Union[str, None] = Field(None)


class CancelOrderMedicationDose(RedoxAbstractModel):
    Quantity: Union[Number, None] = Field(None)
    Units: Union[str, None] = Field(None)


class CancelOrderMedicationFrequency(RedoxAbstractModel):
    Period: Union[Number, None] = Field(None)
    Unit: Union[str, None] = Field(None)


class CancelOrderMedicationProduct(RedoxAbstractModel):
    AltCodes: List["CancelOrderMedicationProductAltCode"] = Field(None)
    Code: str = Field(...)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelOrderMedicationProductAltCode(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelOrderMedicationRate(RedoxAbstractModel):
    Quantity: Union[Number, None] = Field(None)
    Units: Union[str, None] = Field(None)


class CancelOrderMedicationRoute(RedoxAbstractModel):
    AltCodes: List["CancelOrderMedicationRouteAltCode"] = Field(None)
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelOrderMedicationRouteAltCode(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelOrderPharmacy(RedoxAbstractModel):
    Address: "CancelOrderPharmacyAddress" = Field(None)
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    PhoneNumber: "CancelOrderPharmacyPhoneNumber" = Field(None)


class CancelOrderPharmacyAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelOrderPharmacyPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class CancelOrderProvider(RedoxAbstractModel):
    Address: "CancelOrderProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "CancelOrderProviderLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "CancelOrderProviderPhoneNumber" = Field(None)


class CancelOrderProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelOrderProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "CancelOrderProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["CancelOrderProviderLocationFacilityIdentifier"] = Field(
        None
    )
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelOrderProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelOrderProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelOrderProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class CancelOrderVerifiedBy(RedoxAbstractModel):
    Address: "CancelOrderVerifiedByAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "CancelOrderVerifiedByLocation" = Field(None)
    PhoneNumber: "CancelOrderVerifiedByPhoneNumber" = Field(None)


class CancelOrderVerifiedByAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelOrderVerifiedByLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "CancelOrderVerifiedByLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "CancelOrderVerifiedByLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelOrderVerifiedByLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelOrderVerifiedByLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelOrderVerifiedByPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class CancelPatient(RedoxAbstractModel):
    Allergies: List["CancelPatientAllergy"] = Field(None)
    Demographics: "CancelPatientDemographics" = Field(None)
    Identifiers: List["CancelPatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)


class CancelPatientAllergy(RedoxAbstractModel):
    AltCodes: List["CancelPatientAllergyAltCode"] = Field(None)
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Comment: Union[str, None] = Field(None)
    Criticality: "CancelPatientAllergyCriticality" = Field(None)
    EndDate: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Reaction: List["CancelPatientAllergyReaction"] = Field(None)
    Severity: "CancelPatientAllergySeverity" = Field(None)
    StartDate: Union[str, None] = Field(None)
    Status: "CancelPatientAllergyStatus" = Field(None)
    Substance: "CancelPatientAllergySubstance" = Field(None)


class CancelPatientAllergyAltCode(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelPatientAllergyCriticality(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelPatientAllergyReaction(RedoxAbstractModel):
    AltCodes: List["CancelPatientAllergyReactionAltCode"] = Field(None)
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Severity: "CancelPatientAllergyReactionSeverity" = Field(None)
    Text: Union[str, None] = Field(None)


class CancelPatientAllergyReactionAltCode(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelPatientAllergyReactionSeverity(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelPatientAllergySeverity(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelPatientAllergyStatus(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelPatientAllergySubstance(RedoxAbstractModel):
    AltCodes: List["CancelPatientAllergySubstanceAltCode"] = Field(None)
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelPatientAllergySubstanceAltCode(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    CodeSystem: Union[str, None] = Field(None)
    CodeSystemName: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelPatientDemographics(RedoxAbstractModel):
    Address: "CancelPatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "CancelPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class CancelPatientDemographicsAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class CancelPatientIdentifier(RedoxAbstractModel):
    ID: str = Field(...)
    IDType: str = Field(...)


class CancelVisit(RedoxAbstractModel):
    AccountNumber: Union[str, None] = Field(None)
    AttendingProvider: "CancelVisitAttendingProvider" = Field(None)
    Insurances: List["CancelVisitInsurance"] = Field(None)
    Location: "CancelVisitLocation" = Field(None)
    PatientClass: Union[str, None] = Field(None)
    ReferringProvider: "CancelVisitReferringProvider" = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class CancelVisitAttendingProvider(RedoxAbstractModel):
    Address: "CancelVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "CancelVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "CancelVisitAttendingProviderPhoneNumber" = Field(None)


class CancelVisitAttendingProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelVisitAttendingProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "CancelVisitAttendingProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "CancelVisitAttendingProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelVisitAttendingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelVisitAttendingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelVisitAttendingProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class CancelVisitInsurance(RedoxAbstractModel):
    AgreementType: Union[str, None] = Field(None)
    Company: "CancelVisitInsuranceCompany" = Field(None)
    CoverageType: Union[str, None] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    GroupName: Union[str, None] = Field(None)
    GroupNumber: Union[str, None] = Field(None)
    Insured: "CancelVisitInsuranceInsured" = Field(None)
    MemberNumber: Union[str, None] = Field(None)
    Plan: "CancelVisitInsurancePlan" = Field(None)
    PolicyNumber: Union[str, None] = Field(None)
    Priority: Union[str, None] = Field(None)


class CancelVisitInsuranceCompany(RedoxAbstractModel):
    Address: "CancelVisitInsuranceCompanyAddress" = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class CancelVisitInsuranceCompanyAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelVisitInsuranceInsured(RedoxAbstractModel):
    Address: "CancelVisitInsuranceInsuredAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    FirstName: Union[str, None] = Field(None)
    Identifiers: List["CancelVisitInsuranceInsuredIdentifier"] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Relationship: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class CancelVisitInsuranceInsuredAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelVisitInsuranceInsuredIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelVisitInsurancePlan(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelVisitLocation(RedoxAbstractModel):
    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List["CancelVisitLocationDepartmentIdentifier"] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["CancelVisitLocationFacilityIdentifier"] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelVisitReferringProvider(RedoxAbstractModel):
    Address: "CancelVisitReferringProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "CancelVisitReferringProviderLocation" = Field(None)
    PhoneNumber: "CancelVisitReferringProviderPhoneNumber" = Field(None)


class CancelVisitReferringProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelVisitReferringProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "CancelVisitReferringProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "CancelVisitReferringProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelVisitReferringProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelVisitReferringProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelVisitReferringProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


Cancel.update_forward_refs()
CancelMeta.update_forward_refs()
CancelOrder.update_forward_refs()
CancelOrderEnteredBy.update_forward_refs()
CancelOrderEnteredByLocation.update_forward_refs()
CancelOrderMedication.update_forward_refs()
CancelOrderMedicationComponent.update_forward_refs()
CancelOrderMedicationProduct.update_forward_refs()
CancelOrderMedicationRoute.update_forward_refs()
CancelOrderPharmacy.update_forward_refs()
CancelOrderProvider.update_forward_refs()
CancelOrderProviderLocation.update_forward_refs()
CancelOrderVerifiedBy.update_forward_refs()
CancelOrderVerifiedByLocation.update_forward_refs()
CancelPatient.update_forward_refs()
CancelPatientAllergy.update_forward_refs()
CancelPatientAllergyReaction.update_forward_refs()
CancelPatientAllergySubstance.update_forward_refs()
CancelPatientDemographics.update_forward_refs()
CancelVisit.update_forward_refs()
CancelVisitAttendingProvider.update_forward_refs()
CancelVisitAttendingProviderLocation.update_forward_refs()
CancelVisitInsurance.update_forward_refs()
CancelVisitInsuranceCompany.update_forward_refs()
CancelVisitInsuranceInsured.update_forward_refs()
CancelVisitLocation.update_forward_refs()
CancelVisitReferringProvider.update_forward_refs()
CancelVisitReferringProviderLocation.update_forward_refs()
