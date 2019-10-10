import argparse
import factory
import factories
import models
import csv
from random import randint


def records(class_type="model", size=1, max_patient_count=30):
    doctor_class = dict
    record_class = dict

    if class_type == "model":
        doctor_class = models.Doctor
        record_class = models.Record

    doctors = factory.build_batch(
        doctor_class, size=size, FACTORY_CLASS=factories.DoctorFactory
    )

    records = []
    for doctor in doctors:
        patient_count = randint(0, max_patient_count)

        doctor_values = doctor
        if type(doctor) != dict:
            doctor_values = doctor.__dict__
        records.extend(
            factory.build_batch(
                record_class,
                size=patient_count,
                FACTORY_CLASS=factories.RecordFactory,
                **doctor_values,
            )
        )

    if size > 1:
        return records
    else:
        return records[0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "count", type=int, default=10, help="number of records to generate"
    )
    parser.add_argument(
        "-o",
        "--output_file",
        action="store",
        default="records.csv",
        help="output file for records",
    )
    args = parser.parse_args()

    data = records(class_type=dict, size=args.count)

    with open(args.output_file, "w", encoding="utf8", newline="") as output_file:
        fc = csv.DictWriter(output_file, fieldnames=data[0].keys())
        fc.writeheader()
        fc.writerows(data)
