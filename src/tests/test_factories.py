import factories


def test_DoctorFactory_defined():
    assert factories.DoctorFactory is not None


def test_DoctorFactory_creates_a_Record():
    doctor = factories.DoctorFactory()
    assert doctor.__class__.__name__ == "Doctor"


def test_RecordFactory_defined():
    assert factories.RecordFactory is not None


def test_RecordFactory_creates_a_Record():
    record = factories.RecordFactory()
    assert record.__class__.__name__ == "Record"
