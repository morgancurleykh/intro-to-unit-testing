import factory
from datetime import datetime
import models


class DoctorFactory(factory.Factory):
    class Meta:
        model = models.Doctor

    id = factory.Sequence(lambda n: n + 1)
    doctor_first_name = factory.Faker("first_name")
    doctor_last_name = factory.Faker("last_name")
    doctor_address = factory.Faker("address")
    doctor_specialty = factory.Faker("word")
    npi = factory.Faker("isbn10")


class RecordFactory(factory.Factory):
    class Meta:
        model = models.Record

    id = factory.Sequence(lambda n: n + 1)
    doctor_first_name = factory.Faker("first_name")
    doctor_last_name = factory.Faker("last_name")
    doctor_address = factory.Faker("address")
    doctor_specialty = factory.Faker("word")
    npi = factory.Faker("isbn10")
    patient_first_name = factory.Faker("first_name")
    patient_last_name = factory.Faker("last_name")
    ssn = factory.Faker("ssn")
    icd_code = factory.Faker("pyint", min_value=0, max_value=9999, step=1)
    icd_code_description = factory.Faker("sentence")
    diagnosis = factory.Faker("sentences", nb=3)
    examination_date = factory.Faker(
        "date", pattern="%Y-%m-%d", end_datetime=datetime.now()
    )
