# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic.v1 import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class AuthResponse(EventTypeAbstractModel):
    Authorization: "AuthResponseAuthorization" = Field(None)
    Meta: "AuthResponseMeta" = Field(...)
    Patient: "AuthResponsePatient" = Field(...)
    Referral: "AuthResponseReferral" = Field(None)


class AuthResponseAuthorization(RedoxAbstractModel):
    AdditionalDates: List["AuthResponseAuthorizationAdditionalDate"] = Field(None)
    AdmissionSource: Union[str, None] = Field(None)
    AdmissionType: Union[str, None] = Field(None)
    AlternateID: Union[str, None] = Field(None)
    Category: Union[str, None] = Field(None)
    CertificationCode: Union[str, None] = Field(None)
    Decision: Union[str, None] = Field(None)
    DecisionReason: Union[str, None] = Field(None)
    Diagnoses: List["AuthResponseAuthorizationDiagnosis"] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    EventDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    IssueDate: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    Number: Union[str, None] = Field(None)
    Providers: List["AuthResponseAuthorizationProvider"] = Field(None)
    Quantity: "AuthResponseAuthorizationQuantity" = Field(None)
    RelatedCause: Union[str, None] = Field(None)
    Request: "AuthResponseAuthorizationRequest" = Field(None)
    ServiceLevel: Union[str, None] = Field(None)
    ServiceLocation: Union[str, None] = Field(None)
    ServiceType: Union[str, None] = Field(None)
    Services: List["AuthResponseAuthorizationService"] = Field(None)
    Type: Union[str, None] = Field(None)


class AuthResponseAuthorizationAdditionalDate(RedoxAbstractModel):
    DateTime: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AuthResponseAuthorizationDiagnosis(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AuthResponseAuthorizationProvider(RedoxAbstractModel):
    Address: "AuthResponseAuthorizationProviderAddress" = Field(None)
    ContactInfo: Union[str, None] = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "AuthResponseAuthorizationProviderLocation" = Field(None)
    PhoneNumber: "AuthResponseAuthorizationProviderPhoneNumber" = Field(None)
    Type: Union[str, None] = Field(None)


class AuthResponseAuthorizationProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AuthResponseAuthorizationProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "AuthResponseAuthorizationProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "AuthResponseAuthorizationProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AuthResponseAuthorizationProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class AuthResponseAuthorizationProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class AuthResponseAuthorizationProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class AuthResponseAuthorizationQuantity(RedoxAbstractModel):
    Units: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class AuthResponseAuthorizationRequest(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class AuthResponseAuthorizationService(RedoxAbstractModel):
    AuthorizationNumber: Union[str, None] = Field(None)
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Decision: Union[str, None] = Field(None)
    DecisionReason: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    IssueDate: Union[str, None] = Field(None)
    Modifiers: List[str] = Field(None)
    Notes: List[str] = Field(None)
    Quantity: "AuthResponseAuthorizationServiceQuantity" = Field(None)
    RevenueCode: Union[str, None] = Field(None)
    ServiceDate: Union[str, None] = Field(None)


class AuthResponseAuthorizationServiceQuantity(RedoxAbstractModel):
    Units: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class AuthResponseMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["AuthResponseMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["AuthResponseMetaLog"] = Field(None)
    Message: "AuthResponseMetaMessage" = Field(None)
    Source: "AuthResponseMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "AuthResponseMetaTransmission" = Field(None)


class AuthResponseMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class AuthResponseMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class AuthResponseMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class AuthResponseMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class AuthResponseMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class AuthResponsePatient(RedoxAbstractModel):
    Contacts: List["AuthResponsePatientContact"] = Field(None)
    Demographics: "AuthResponsePatientDemographics" = Field(None)
    Identifiers: List["AuthResponsePatientIdentifier"] = Field(...)
    Insurances: List["AuthResponsePatientInsurance"] = Field(None)
    Notes: List[str] = Field(None)


class AuthResponsePatientContact(RedoxAbstractModel):
    Address: "AuthResponsePatientContactAddress" = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "AuthResponsePatientContactPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    Roles: List[str] = Field(None)


class AuthResponsePatientContactAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AuthResponsePatientContactPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class AuthResponsePatientDemographics(RedoxAbstractModel):
    Address: "AuthResponsePatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "AuthResponsePatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class AuthResponsePatientDemographicsAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AuthResponsePatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class AuthResponsePatientIdentifier(RedoxAbstractModel):
    ID: str = Field(...)
    IDType: str = Field(...)


class AuthResponsePatientInsurance(RedoxAbstractModel):
    AgreementType: Union[str, None] = Field(None)
    Company: "AuthResponsePatientInsuranceCompany" = Field(None)
    CoverageType: Union[str, None] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    GroupName: Union[str, None] = Field(None)
    GroupNumber: Union[str, None] = Field(None)
    Insured: "AuthResponsePatientInsuranceInsured" = Field(None)
    MemberNumber: Union[str, None] = Field(None)
    Plan: "AuthResponsePatientInsurancePlan" = Field(None)
    PolicyNumber: Union[str, None] = Field(None)
    Priority: Union[str, None] = Field(None)


class AuthResponsePatientInsuranceCompany(RedoxAbstractModel):
    Address: "AuthResponsePatientInsuranceCompanyAddress" = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class AuthResponsePatientInsuranceCompanyAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AuthResponsePatientInsuranceInsured(RedoxAbstractModel):
    Address: "AuthResponsePatientInsuranceInsuredAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    FirstName: Union[str, None] = Field(None)
    Identifiers: List["AuthResponsePatientInsuranceInsuredIdentifier"] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Relationship: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class AuthResponsePatientInsuranceInsuredAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AuthResponsePatientInsuranceInsuredIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class AuthResponsePatientInsurancePlan(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AuthResponseReferral(RedoxAbstractModel):
    AlternateID: Union[str, None] = Field(None)
    Authorization: "AuthResponseReferralAuthorization" = Field(None)
    Category: Union[str, None] = Field(None)
    DateTime: Union[str, None] = Field(None)
    DepartmentSpecialty: Union[str, None] = Field(None)
    Diagnoses: List["AuthResponseReferralDiagnosis"] = Field(None)
    ExpirationDateTime: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    Priority: Union[str, None] = Field(None)
    Procedures: List["AuthResponseReferralProcedure"] = Field(None)
    ProcessDateTime: Union[str, None] = Field(None)
    ProviderSpecialty: Union[str, None] = Field(None)
    Providers: List["AuthResponseReferralProvider"] = Field(None)
    Reason: Union[str, None] = Field(None)
    RelatedCause: Union[str, None] = Field(None)
    RequestType: Union[str, None] = Field(None)
    ServiceLocation: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)
    StatusReason: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)
    Visit: "AuthResponseReferralVisit" = Field(None)


class AuthResponseReferralAuthorization(RedoxAbstractModel):
    AuthorizedTreatmentCount: Union[str, None] = Field(None)
    Company: "AuthResponseReferralAuthorizationCompany" = Field(None)
    DateTime: Union[str, None] = Field(None)
    ExpirationDateTime: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    Number: Union[str, None] = Field(None)
    Plan: "AuthResponseReferralAuthorizationPlan" = Field(None)
    ReimbursementLimit: Union[str, None] = Field(None)
    RequestedTreatmentCount: Union[str, None] = Field(None)
    RequestedTreatmentUnits: Union[str, None] = Field(None)


class AuthResponseReferralAuthorizationCompany(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class AuthResponseReferralAuthorizationPlan(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class AuthResponseReferralDiagnosis(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    Type: Union[str, None] = Field(None)


class AuthResponseReferralProcedure(RedoxAbstractModel):
    Authorization: "AuthResponseReferralProcedureAuthorization" = Field(None)
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Modifiers: List[str] = Field(None)
    Notes: List[str] = Field(None)
    Quantity: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)
    StatusReason: Union[str, None] = Field(None)
    Units: Union[str, None] = Field(None)


class AuthResponseReferralProcedureAuthorization(RedoxAbstractModel):
    DateTime: Union[str, None] = Field(None)
    ExpirationDateTime: Union[str, None] = Field(None)


class AuthResponseReferralProvider(RedoxAbstractModel):
    Address: "AuthResponseReferralProviderAddress" = Field(None)
    ContactInfo: Union[str, None] = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "AuthResponseReferralProviderLocation" = Field(None)
    PhoneNumber: "AuthResponseReferralProviderPhoneNumber" = Field(None)
    Type: Union[str, None] = Field(None)


class AuthResponseReferralProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AuthResponseReferralProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "AuthResponseReferralProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "AuthResponseReferralProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AuthResponseReferralProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class AuthResponseReferralProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class AuthResponseReferralProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class AuthResponseReferralVisit(RedoxAbstractModel):
    VisitNumber: Union[str, None] = Field(None)


AuthResponse.update_forward_refs()
AuthResponseAuthorization.update_forward_refs()
AuthResponseAuthorizationProvider.update_forward_refs()
AuthResponseAuthorizationProviderLocation.update_forward_refs()
AuthResponseAuthorizationService.update_forward_refs()
AuthResponseMeta.update_forward_refs()
AuthResponsePatient.update_forward_refs()
AuthResponsePatientContact.update_forward_refs()
AuthResponsePatientDemographics.update_forward_refs()
AuthResponsePatientInsurance.update_forward_refs()
AuthResponsePatientInsuranceCompany.update_forward_refs()
AuthResponsePatientInsuranceInsured.update_forward_refs()
AuthResponseReferral.update_forward_refs()
AuthResponseReferralAuthorization.update_forward_refs()
AuthResponseReferralProcedure.update_forward_refs()
AuthResponseReferralProvider.update_forward_refs()
AuthResponseReferralProviderLocation.update_forward_refs()
