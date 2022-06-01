# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class New(EventTypeAbstractModel):

    Meta: "NewMeta" = Field(...)
    Orders: List["NewOrder"] = Field(...)
    Patient: "NewPatient" = Field(...)
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


class NewOrder(RedoxAbstractModel):

    ApplicationOrderID: Union[str, None] = Field(None)
    CollectionDateTime: Union[str, None] = Field(None)
    CompletionDateTime: Union[str, None] = Field(None)
    ID: str = Field(...)
    Notes: List[str] = Field(None)
    Priority: Union[str, None] = Field(None)
    Procedure: "NewOrderProcedure" = Field(None)
    Provider: "NewOrderProvider" = Field(None)
    ResponseFlag: Union[str, None] = Field(None)
    ResultCopyProviders: List["NewOrderResultCopyProvider"] = Field(None)
    Results: List["NewOrderResult"] = Field(...)
    ResultsStatus: Union[str, None] = Field(None)
    Status: str = Field(...)
    TransactionDateTime: Union[str, None] = Field(None)


class NewOrderProcedure(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class NewOrderProvider(RedoxAbstractModel):

    Address: "NewOrderProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewOrderProviderLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "NewOrderProviderPhoneNumber" = Field(None)


class NewOrderProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewOrderProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewOrderProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class NewOrderResult(RedoxAbstractModel):

    AbnormalFlag: Union[str, None] = Field(None)
    Code: str = Field(...)
    Codeset: Union[str, None] = Field(None)
    CompletionDateTime: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    FileType: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    ObservationMethod: "NewOrderResultObservationMethod" = Field(None)
    Performer: "NewOrderResultPerformer" = Field(None)
    PrimaryResultsInterpreter: "NewOrderResultPrimaryResultsInterpreter" = Field(None)
    Producer: "NewOrderResultProducer" = Field(None)
    ReferenceRange: "NewOrderResultReferenceRange" = Field(None)
    RelatedGroupID: Union[str, None] = Field(None)
    Specimen: "NewOrderResultSpecimen" = Field(None)
    Status: Union[str, None] = Field(None)
    Units: Union[str, None] = Field(None)
    Value: str = Field(...)
    ValueType: str = Field(...)


class NewOrderResultCopyProvider(RedoxAbstractModel):

    Address: "NewOrderResultCopyProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewOrderResultCopyProviderLocation" = Field(None)
    PhoneNumber: "NewOrderResultCopyProviderPhoneNumber" = Field(None)


class NewOrderResultCopyProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewOrderResultCopyProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewOrderResultCopyProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class NewOrderResultObservationMethod(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class NewOrderResultPerformer(RedoxAbstractModel):

    Address: "NewOrderResultPerformerAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewOrderResultPerformerLocation" = Field(None)
    PhoneNumber: "NewOrderResultPerformerPhoneNumber" = Field(None)


class NewOrderResultPerformerAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewOrderResultPerformerLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewOrderResultPerformerPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class NewOrderResultPrimaryResultsInterpreter(RedoxAbstractModel):

    Address: "NewOrderResultPrimaryResultsInterpreterAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewOrderResultPrimaryResultsInterpreterLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "NewOrderResultPrimaryResultsInterpreterPhoneNumber" = Field(None)


class NewOrderResultPrimaryResultsInterpreterAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewOrderResultPrimaryResultsInterpreterLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewOrderResultPrimaryResultsInterpreterPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class NewOrderResultProducer(RedoxAbstractModel):

    Address: "NewOrderResultProducerAddress" = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewOrderResultProducerAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewOrderResultReferenceRange(RedoxAbstractModel):

    High: Union[Number, None] = Field(None)
    Low: Union[Number, None] = Field(None)
    Text: Union[str, None] = Field(None)


class NewOrderResultSpecimen(RedoxAbstractModel):

    BodySite: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    Source: Union[str, None] = Field(None)


class NewPatient(RedoxAbstractModel):

    Contacts: List["NewPatientContact"] = Field(None)
    Demographics: "NewPatientDemographics" = Field(None)
    Identifiers: List["NewPatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)


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
    PhoneNumber: "NewPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)


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


class NewVisit(RedoxAbstractModel):

    AccountNumber: Union[str, None] = Field(None)
    AdditionalStaff: List["NewVisitAdditionalStaff"] = Field(None)
    AttendingProvider: "NewVisitAttendingProvider" = Field(None)
    Location: "NewVisitLocation" = Field(None)
    PatientClass: Union[str, None] = Field(None)
    ReferringProvider: "NewVisitReferringProvider" = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class NewVisitAdditionalStaff(RedoxAbstractModel):

    Address: "NewVisitAdditionalStaffAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewVisitAdditionalStaffLocation" = Field(None)
    PhoneNumber: "NewVisitAdditionalStaffPhoneNumber" = Field(None)
    Role: "NewVisitAdditionalStaffRole" = Field(None)


class NewVisitAdditionalStaffAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewVisitAdditionalStaffLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewVisitAdditionalStaffPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class NewVisitAdditionalStaffRole(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class NewVisitAttendingProvider(RedoxAbstractModel):

    Address: "NewVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "NewVisitAttendingProviderPhoneNumber" = Field(None)


class NewVisitAttendingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewVisitAttendingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewVisitAttendingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class NewVisitLocation(RedoxAbstractModel):

    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewVisitReferringProvider(RedoxAbstractModel):

    Address: "NewVisitReferringProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewVisitReferringProviderLocation" = Field(None)
    PhoneNumber: "NewVisitReferringProviderPhoneNumber" = Field(None)


class NewVisitReferringProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewVisitReferringProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewVisitReferringProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


New.update_forward_refs()
NewMeta.update_forward_refs()
NewOrder.update_forward_refs()
NewOrderProvider.update_forward_refs()
NewOrderResult.update_forward_refs()
NewOrderResultCopyProvider.update_forward_refs()
NewOrderResultPerformer.update_forward_refs()
NewOrderResultPrimaryResultsInterpreter.update_forward_refs()
NewOrderResultProducer.update_forward_refs()
NewPatient.update_forward_refs()
NewPatientContact.update_forward_refs()
NewPatientDemographics.update_forward_refs()
NewVisit.update_forward_refs()
NewVisitAdditionalStaff.update_forward_refs()
NewVisitAttendingProvider.update_forward_refs()
NewVisitReferringProvider.update_forward_refs()
