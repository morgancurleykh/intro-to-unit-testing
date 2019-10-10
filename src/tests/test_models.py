import models


def test_Doctor_defined():
    assert models.Doctor is not None


def test_Doctor_can_be_instantiated():
    data = models.Doctor(1, "dfname", "dlname", "daddres", "dspecialty", "npi")

    assert f"{data}" == "Dr. dfname dlname"


def test_Record_defined():
    assert models.Record is not None


def test_Record_can_be_instantiated():
    data = models.Record(
        1,
        "dfname",
        "dlname",
        "daddres",
        "dspecialty",
        "npi",
        "pfname",
        "plname",
        "ssn",
        "icd_code",
        "icd_description",
        "diagnosis",
        "examination_date",
    )

    assert f"{data}" == "pfname plname visited Dr. dfname dlname"
