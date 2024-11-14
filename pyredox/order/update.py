# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic.v1 import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Update(EventTypeAbstractModel):
    Meta: "UpdateMeta" = Field(...)
    Order: "UpdateOrder" = Field(...)
    Patient: "UpdatePatient" = Field(...)
    Visit: "UpdateVisit" = Field(None)


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


class UpdateOrder(RedoxAbstractModel):
    ApplicationOrderID: Union[str, None] = Field(None)
    ClinicalInfo: List["UpdateOrderClinicalInfo"] = Field(None)
    CollectionDateTime: Union[str, None] = Field(None)
    Comments: Union[str, None] = Field(None)
    Diagnoses: List["UpdateOrderDiagnosis"] = Field(None)
    Expiration: Union[str, None] = Field(None)
    ID: str = Field(...)
    Notes: List[str] = Field(None)
    OrderingFacility: "UpdateOrderOrderingFacility" = Field(None)
    Priority: Union[str, None] = Field(None)
    Procedure: "UpdateOrderProcedure" = Field(None)
    Provider: "UpdateOrderProvider" = Field(None)
    ResultCopyProviders: List["UpdateOrderResultCopyProvider"] = Field(None)
    Specimen: "UpdateOrderSpecimen" = Field(None)
    Status: Union[str, None] = Field(None)
    TransactionDateTime: Union[str, None] = Field(None)


class UpdateOrderClinicalInfo(RedoxAbstractModel):
    Abbreviation: Union[str, None] = Field(None)
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    Units: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class UpdateOrderDiagnosis(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateOrderOrderingFacility(RedoxAbstractModel):
    Address: "UpdateOrderOrderingFacilityAddress" = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class UpdateOrderOrderingFacilityAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateOrderProcedure(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class UpdateOrderProvider(RedoxAbstractModel):
    Address: "UpdateOrderProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "UpdateOrderProviderLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "UpdateOrderProviderPhoneNumber" = Field(None)


class UpdateOrderProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateOrderProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "UpdateOrderProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["UpdateOrderProviderLocationFacilityIdentifier"] = Field(
        None
    )
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateOrderProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateOrderProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateOrderProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class UpdateOrderResultCopyProvider(RedoxAbstractModel):
    Address: "UpdateOrderResultCopyProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "UpdateOrderResultCopyProviderLocation" = Field(None)
    PhoneNumber: "UpdateOrderResultCopyProviderPhoneNumber" = Field(None)


class UpdateOrderResultCopyProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateOrderResultCopyProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "UpdateOrderResultCopyProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "UpdateOrderResultCopyProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateOrderResultCopyProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateOrderResultCopyProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateOrderResultCopyProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class UpdateOrderSpecimen(RedoxAbstractModel):
    BodySite: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    Source: Union[str, None] = Field(None)


class UpdatePatient(RedoxAbstractModel):
    Demographics: "UpdatePatientDemographics" = Field(None)
    Identifiers: List["UpdatePatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)


class UpdatePatientDemographics(RedoxAbstractModel):
    Address: "UpdatePatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "UpdatePatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class UpdatePatientDemographicsAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdatePatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class UpdatePatientIdentifier(RedoxAbstractModel):
    ID: str = Field(...)
    IDType: str = Field(...)


class UpdateVisit(RedoxAbstractModel):
    AccountNumber: Union[str, None] = Field(None)
    AttendingProvider: "UpdateVisitAttendingProvider" = Field(None)
    ConsultingProvider: "UpdateVisitConsultingProvider" = Field(None)
    Guarantor: "UpdateVisitGuarantor" = Field(None)
    Insurances: List["UpdateVisitInsurance"] = Field(None)
    Location: "UpdateVisitLocation" = Field(None)
    PatientClass: Union[str, None] = Field(None)
    ReferringProvider: "UpdateVisitReferringProvider" = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class UpdateVisitAttendingProvider(RedoxAbstractModel):
    Address: "UpdateVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "UpdateVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "UpdateVisitAttendingProviderPhoneNumber" = Field(None)


class UpdateVisitAttendingProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateVisitAttendingProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "UpdateVisitAttendingProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "UpdateVisitAttendingProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateVisitAttendingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateVisitAttendingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateVisitAttendingProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class UpdateVisitConsultingProvider(RedoxAbstractModel):
    Address: "UpdateVisitConsultingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "UpdateVisitConsultingProviderLocation" = Field(None)
    PhoneNumber: "UpdateVisitConsultingProviderPhoneNumber" = Field(None)


class UpdateVisitConsultingProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateVisitConsultingProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "UpdateVisitConsultingProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "UpdateVisitConsultingProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateVisitConsultingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateVisitConsultingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateVisitConsultingProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class UpdateVisitGuarantor(RedoxAbstractModel):
    Address: "UpdateVisitGuarantorAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    Employer: "UpdateVisitGuarantorEmployer" = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Number: Union[str, None] = Field(None)
    PhoneNumber: "UpdateVisitGuarantorPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    Spouse: "UpdateVisitGuarantorSpouse" = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateVisitGuarantorAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateVisitGuarantorEmployer(RedoxAbstractModel):
    Address: "UpdateVisitGuarantorEmployerAddress" = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class UpdateVisitGuarantorEmployerAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateVisitGuarantorPhoneNumber(RedoxAbstractModel):
    Business: Union[str, None] = Field(None)
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)


class UpdateVisitGuarantorSpouse(RedoxAbstractModel):
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)


class UpdateVisitInsurance(RedoxAbstractModel):
    AgreementType: Union[str, None] = Field(None)
    Company: "UpdateVisitInsuranceCompany" = Field(None)
    CoverageType: Union[str, None] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    GroupName: Union[str, None] = Field(None)
    GroupNumber: Union[str, None] = Field(None)
    Insured: "UpdateVisitInsuranceInsured" = Field(None)
    MemberNumber: Union[str, None] = Field(None)
    Plan: "UpdateVisitInsurancePlan" = Field(None)
    PolicyNumber: Union[str, None] = Field(None)
    Priority: Union[str, None] = Field(None)


class UpdateVisitInsuranceCompany(RedoxAbstractModel):
    Address: "UpdateVisitInsuranceCompanyAddress" = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class UpdateVisitInsuranceCompanyAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateVisitInsuranceInsured(RedoxAbstractModel):
    Address: "UpdateVisitInsuranceInsuredAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    FirstName: Union[str, None] = Field(None)
    Identifiers: List["UpdateVisitInsuranceInsuredIdentifier"] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Relationship: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class UpdateVisitInsuranceInsuredAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateVisitInsuranceInsuredIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateVisitInsurancePlan(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateVisitLocation(RedoxAbstractModel):
    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List["UpdateVisitLocationDepartmentIdentifier"] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["UpdateVisitLocationFacilityIdentifier"] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateVisitReferringProvider(RedoxAbstractModel):
    Address: "UpdateVisitReferringProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "UpdateVisitReferringProviderLocation" = Field(None)
    PhoneNumber: "UpdateVisitReferringProviderPhoneNumber" = Field(None)


class UpdateVisitReferringProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class UpdateVisitReferringProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "UpdateVisitReferringProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "UpdateVisitReferringProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class UpdateVisitReferringProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateVisitReferringProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class UpdateVisitReferringProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


Update.update_forward_refs()
UpdateMeta.update_forward_refs()
UpdateOrder.update_forward_refs()
UpdateOrderOrderingFacility.update_forward_refs()
UpdateOrderProvider.update_forward_refs()
UpdateOrderProviderLocation.update_forward_refs()
UpdateOrderResultCopyProvider.update_forward_refs()
UpdateOrderResultCopyProviderLocation.update_forward_refs()
UpdatePatient.update_forward_refs()
UpdatePatientDemographics.update_forward_refs()
UpdateVisit.update_forward_refs()
UpdateVisitAttendingProvider.update_forward_refs()
UpdateVisitAttendingProviderLocation.update_forward_refs()
UpdateVisitConsultingProvider.update_forward_refs()
UpdateVisitConsultingProviderLocation.update_forward_refs()
UpdateVisitGuarantor.update_forward_refs()
UpdateVisitGuarantorEmployer.update_forward_refs()
UpdateVisitInsurance.update_forward_refs()
UpdateVisitInsuranceCompany.update_forward_refs()
UpdateVisitInsuranceInsured.update_forward_refs()
UpdateVisitLocation.update_forward_refs()
UpdateVisitReferringProvider.update_forward_refs()
UpdateVisitReferringProviderLocation.update_forward_refs()
