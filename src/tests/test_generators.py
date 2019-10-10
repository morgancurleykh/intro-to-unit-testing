import generators


def test_record_defined():
    assert generators.records is not None


def test_record_returns_an_instance_of_Record():
    data = generators.records()
    assert data.__class__.__name__ == "Record"


def test_record_returns_a_list_of_Record_instances():
    data = generators.records(size=10)
    assert len(data) >= 10

    for i in data:
        assert i.__class__.__name__ == "Record"


def test_record_returns_an_instance_of_dict():
    data = generators.records(class_type=dict)
    assert type(data) == dict


def test_record_returns_a_list_of_dict_instances():
    data = generators.records(class_type=dict, size=10)
    assert len(data) >= 10

    for i in data:
        assert type(i) == dict
