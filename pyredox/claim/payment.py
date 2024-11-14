# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic.v1 import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Payment(EventTypeAbstractModel):
    Meta: "PaymentMeta" = Field(...)
    Payee: "PaymentPayee" = Field(None)
    Payer: "PaymentPayer" = Field(None)
    Payments: List["PaymentPayment"] = Field(...)
    Transaction: "PaymentTransaction" = Field(None)


class PaymentMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["PaymentMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["PaymentMetaLog"] = Field(None)
    Message: "PaymentMetaMessage" = Field(None)
    Source: "PaymentMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "PaymentMetaTransmission" = Field(None)


class PaymentMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PaymentMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class PaymentMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class PaymentMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PaymentMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class PaymentPayee(RedoxAbstractModel):
    Address: "PaymentPayeeAddress" = Field(None)
    EmailAddress: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: "PaymentPayeePhoneNumber" = Field(None)


class PaymentPayeeAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PaymentPayeePhoneNumber(RedoxAbstractModel):
    Fax: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class PaymentPayer(RedoxAbstractModel):
    Address: "PaymentPayerAddress" = Field(None)
    EmailAddress: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: "PaymentPayerPhoneNumber" = Field(None)


class PaymentPayerAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PaymentPayerPhoneNumber(RedoxAbstractModel):
    Fax: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class PaymentPayment(RedoxAbstractModel):
    Claim: "PaymentPaymentClaim" = Field(None)
    DateTime: Union[str, None] = Field(None)
    Patient: "PaymentPaymentPatient" = Field(...)


class PaymentPaymentClaim(RedoxAbstractModel):
    Adjustments: List["PaymentPaymentClaimAdjustment"] = Field(None)
    ChargedAmount: Union[str, None] = Field(None)
    Number: Union[str, None] = Field(None)
    PatientResponsibilityAmount: Union[str, None] = Field(None)
    PaymentAmount: Union[str, None] = Field(None)
    ReceivedDate: Union[str, None] = Field(None)
    ReferenceNumbers: List["PaymentPaymentClaimReferenceNumber"] = Field(None)
    ServiceDateTime: Union[str, None] = Field(None)
    ServiceEndDateTime: Union[str, None] = Field(None)
    Services: List["PaymentPaymentClaimService"] = Field(None)
    Status: Union[str, None] = Field(None)
    SubmissionNumber: Union[str, None] = Field(None)


class PaymentPaymentClaimAdjustment(RedoxAbstractModel):
    Amount: Union[str, None] = Field(None)
    Quantity: Union[str, None] = Field(None)
    Reason: Union[str, None] = Field(None)
    ReasonGroup: Union[str, None] = Field(None)


class PaymentPaymentClaimReferenceNumber(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PaymentPaymentClaimService(RedoxAbstractModel):
    AdjudicatedProcedure: "PaymentPaymentClaimServiceAdjudicatedProcedure" = Field(None)
    AllowedAmount: Union[str, None] = Field(None)
    ChargedAmount: Union[str, None] = Field(None)
    ChargedUnits: Union[str, None] = Field(None)
    DeductibleAmount: Union[str, None] = Field(None)
    PaymentAmount: Union[str, None] = Field(None)
    PaymentUnits: Union[str, None] = Field(None)
    ReferenceNumbers: List["PaymentPaymentClaimServiceReferenceNumber"] = Field(None)
    ServiceDateTime: Union[str, None] = Field(None)
    ServiceEndDateTime: Union[str, None] = Field(None)
    SubmittedProcedure: "PaymentPaymentClaimServiceSubmittedProcedure" = Field(None)


class PaymentPaymentClaimServiceAdjudicatedProcedure(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    CodeSet: Union[str, None] = Field(None)
    Modifiers: List[str] = Field(None)
    Name: Union[str, None] = Field(None)


class PaymentPaymentClaimServiceReferenceNumber(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PaymentPaymentClaimServiceSubmittedProcedure(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    CodeSet: Union[str, None] = Field(None)
    Modifiers: List[str] = Field(None)
    Name: Union[str, None] = Field(None)


class PaymentPaymentPatient(RedoxAbstractModel):
    Demographics: "PaymentPaymentPatientDemographics" = Field(None)
    Identifiers: List["PaymentPaymentPatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)


class PaymentPaymentPatientDemographics(RedoxAbstractModel):
    Address: "PaymentPaymentPatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "PaymentPaymentPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class PaymentPaymentPatientDemographicsAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PaymentPaymentPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class PaymentPaymentPatientIdentifier(RedoxAbstractModel):
    ID: str = Field(...)
    IDType: str = Field(...)


class PaymentTransaction(RedoxAbstractModel):
    CreditOrDebit: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    PaymentDateTime: Union[str, None] = Field(None)
    PaymentMethod: Union[str, None] = Field(None)
    Receiver: "PaymentTransactionReceiver" = Field(None)
    Submitter: "PaymentTransactionSubmitter" = Field(None)
    TotalPaymentAmount: Union[str, None] = Field(None)
    TrackingNumber: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PaymentTransactionReceiver(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PaymentTransactionSubmitter(RedoxAbstractModel):
    EmailAddress: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: "PaymentTransactionSubmitterPhoneNumber" = Field(None)


class PaymentTransactionSubmitterPhoneNumber(RedoxAbstractModel):
    Fax: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


Payment.update_forward_refs()
PaymentMeta.update_forward_refs()
PaymentPayee.update_forward_refs()
PaymentPayer.update_forward_refs()
PaymentPayment.update_forward_refs()
PaymentPaymentClaim.update_forward_refs()
PaymentPaymentClaimService.update_forward_refs()
PaymentPaymentPatient.update_forward_refs()
PaymentPaymentPatientDemographics.update_forward_refs()
PaymentTransaction.update_forward_refs()
PaymentTransactionSubmitter.update_forward_refs()
