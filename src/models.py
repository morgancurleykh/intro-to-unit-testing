class Doctor(object):
    def __init__(
        self,
        id,
        doctor_first_name,
        doctor_last_name,
        doctor_address,
        doctor_specialty,
        npi,
    ):

        self.id = id
        self.doctor_first_name = doctor_first_name
        self.doctor_last_name = doctor_last_name
        self.doctor_address = doctor_address
        self.doctor_specialty = doctor_specialty
        self.npi = npi

    def __str__(self):
        return f"Dr. {self.doctor_first_name} {self.doctor_last_name}"


class Record(object):
    def __init__(
        self,
        id,
        doctor_first_name,
        doctor_last_name,
        doctor_address,
        doctor_specialty,
        npi,
        patient_first_name,
        patient_last_name,
        ssn,
        icd_code,
        icd_code_description,
        diagnosis,
        examination_date,
    ):

        self.id = id
        self.doctor_first_name = doctor_first_name
        self.doctor_last_name = doctor_last_name
        self.doctor_address = doctor_address
        self.doctor_specialty = doctor_specialty
        self.npi = npi
        self.patient_first_name = patient_first_name
        self.patient_last_name = patient_last_name
        self.ssn = ssn
        self.icd_code = icd_code
        self.icd_code_description = icd_code_description
        self.diagnosis = diagnosis
        self.examination_date = examination_date

    def __str__(self):
        return f"{self.patient_first_name} {self.patient_last_name} visited Dr. {self.doctor_first_name} {self.doctor_last_name}"  # noqa: E501
