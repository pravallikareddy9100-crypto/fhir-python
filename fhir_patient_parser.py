import json
from datetime import datetime

def calculate_age(birthdate_str):
    birth = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = datetime.today().date()
    return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

with open("sample_patient.json", "r") as f:
    patient_data = json.load(f)

name = patient_data.get('name', [{}])[0]
given = name.get('given', [''])[0] if name else ''
family = name.get('family', '') if name else ''

print("FHIR Patient Resource Parsed:")
print("Patient Name:", given, family)
print("Gender:", patient_data.get('gender', 'N/A'))
birth = patient_data.get('birthDate', None)
if birth:
    print("Birth Date:", birth)
    print("Age (calculated):", calculate_age(birth))
else:
    print("Birth Date: N/A")
