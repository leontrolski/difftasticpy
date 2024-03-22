import copy
import json
import difftasticpy


def test_foo() -> None:
    assert (
        difftasticpy.diff(
            json.dumps(JSON_A, indent=4),
            json.dumps(JSON_B, indent=4),
            width=120,
        )
        == ""
    )


JSON_A = [
    {
        "payload": {
            "CommonBlock": {
                "A0": {
                    "always": [],
                    "primaryRecipients": ["0000000000"],
                    "secondaryRecipients": [],
                },
                "D0": {
                    "initialCorrelationID": "fake-correlation-id",
                    "publicationID": "PUB-035",
                    "replayIndicator": False,
                    "serviceTicketURL": None,
                    "transactionID": "fake-transaction-id",
                    "transactionTimestamp": "2024-01-12T02:00:00+00:00",
                },
                "M0": {
                    "GSPGroupID": "_J",
                    "MPANCore": "1900012374324",
                    "distributorDIPID": "0000000000",
                },
                "S0": {
                    "eventCode": "[MSAppAccepted]",
                    "interfaceID": "IF-035",
                    "schemaVersion": "009",
                },
                "S1": {
                    "DIPConnectionProviderID": None,
                    "environmentTag": "SIT",
                    "senderCorrelationID": None,
                    "senderDIPID": "0000000000",
                    "senderRoleID": "REGS",
                    "senderTimestamp": "2024-01-12T01:00:00+00:00",
                    "senderUniqueReference": "S-IF-035-2200000003-REGS-19700101-0",
                    "subText": "test",
                },
            },
            "CustomBlock": {
                "B007": {
                    "proposedAppointmentResponseCode": "SP000 - Proposed Appointment ACCEPTED",
                    "responseCode": "A",
                },
                "B012": {
                    "serviceProviderAppointmentRequestingSupplierDIPID": "2300000012",
                    "serviceProviderAppointmentRequestingSupplierMPID": "MRCY",
                },
                "B013": {"CSSRegistrationRequestID": "CSSSwitchIDEXAMPLE"},
                "B070": {
                    "appointmentScenario": "COS",
                    "contractReferenceMeteringService": "OESLMRCYMO",
                    "proposedMeteringServiceDIPEffectiveFromDate": "2024-01-15T00:00:00+00:00",
                    "proposedMeteringServiceDIPID": "1200000015",
                    "proposedMeteringServiceMPID": "OESL",
                },
            },
        }
    }
]
JSON_B = [
    {
        "payload": {
            "CommonBlock": {
                "A0": {
                    "always": [],
                    "primaryRecipients": ["0000000000"],
                    "secondaryRecipients": [],
                },
                "D0": {
                    "initialCorrelationID": "fake-correlation-id",
                    "publicationID": "PUB-035",
                    "replayIndicator": False,
                    "serviceTicketURL": None,
                    "transactionID": "fake-transaction-id",
                    "transactionTimestamp": "2024-01-12T02:00:00+00:00",
                },
                "M0": {
                    "GSPGroupID": "_J",
                    "MPANCore": "1900012374324",
                    "distributorDIPID": "0000000000",
                },
                "S0": {
                    "eventCode": "[MSAppAccepted]",
                    "interfaceID": "IF-035",
                    "schemaVersion": "009",
                },
                "S1": {
                    "DIPConnectionProviderID": None,
                    "environmentTag": "SIT",
                    "senderCorrelationID": None,
                    "senderDIPID": "0000000000",
                    "senderRoleID": "REGS",
                    "senderTimestamp": "2024-01-12T01:00:00+00:00",
                    "senderUniqueReference": "S-IF-035-3300000003-REGS-19700101-0",
                    "subText": "test",
                },
            },
            "CustomBlock": {
                "B012": {
                    "serviceProviderAppointmentRequestingSupplierDIPID": "2300000012",
                    "serviceProviderAppointmentRequestingSupplierMPID": "MRCY",
                    "foo": "bar",
                },
                "B013": {"CSSRegistrationRequestID": "CSSSwitchIDEXAMPLE"},
                "B070": {
                    "appointmentScenario": "COS",
                    "contractReferenceMeteringService": "OESLMRCYMO",
                    "proposedMeteringServiceDIPEffectiveFromDate": "2024-01-15T00:00:00+00:00",
                    "proposedMeteringServiceDIPID": "1200000015",
                    "proposedMeteringServiceMPID": "OESL",
                },
            },
        }
    }
]
