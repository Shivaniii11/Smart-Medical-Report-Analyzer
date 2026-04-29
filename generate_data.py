import pandas as pd

data = [
    # Blood
    ["Hemoglobin", 12, 16, "g/dL", "Blood", "High"],
    ["WBC", 4000, 11000, "cells/uL", "Blood", "High"],
    ["RBC", 4.5, 5.9, "million/uL", "Blood", "High"],
    ["Platelets", 150000, 450000, "cells/uL", "Blood", "High"],
    ["Hematocrit", 36, 50, "%", "Blood", "High"],
    ["MCV", 80, 100, "fL", "Blood", "High"],
    ["MCH", 27, 33, "pg", "Blood", "High"],
    ["MCHC", 32, 36, "g/dL", "Blood", "High"],
    ["Neutrophils", 40, 70, "%", "Blood", "High"],
    ["Lymphocytes", 20, 40, "%", "Blood", "High"],

    # Diabetes
    ["Glucose", 70, 99, "mg/dL", "Diabetes", "Critical"],
    ["HbA1c", 4, 5.6, "%", "Diabetes", "Critical"],

    # Lipid
    ["Total Cholesterol", 0, 200, "mg/dL", "Lipid", "Critical"],
    ["HDL", 40, 100, "mg/dL", "Lipid", "Good"],
    ["LDL", 0, 100, "mg/dL", "Lipid", "Critical"],
    ["Triglycerides", 0, 150, "mg/dL", "Lipid", "Critical"],
    ["Cholesterol Ratio", 3, 5, "ratio", "Lipid", "Critical"],

    # Liver
    ["SGPT (ALT)", 7, 56, "U/L", "Liver", "Critical"],
    ["SGOT (AST)", 10, 40, "U/L", "Liver", "Critical"],
    ["Bilirubin", 0.1, 1.2, "mg/dL", "Liver", "Critical"],
    ["Albumin", 3.5, 5.5, "g/dL", "Liver", "Good"],
    ["Alkaline Phosphatase", 44, 147, "U/L", "Liver", "Critical"],

    # Kidney
    ["Creatinine", 0.6, 1.3, "mg/dL", "Kidney", "Critical"],
    ["Urea", 7, 20, "mg/dL", "Kidney", "Critical"],
    ["Uric Acid", 3.5, 7.2, "mg/dL", "Kidney", "Critical"],
    ["eGFR", 90, 120, "mL/min", "Kidney", "Critical"],

    # Thyroid
    ["TSH", 0.4, 4.0, "mIU/L", "Thyroid", "Critical"],
    ["T3", 80, 200, "ng/dL", "Thyroid", "Critical"],
    ["T4", 5, 12, "µg/dL", "Thyroid", "Critical"],

    # Vitamins
    ["Vitamin D", 30, 100, "ng/mL", "Vitamins", "Critical"],
    ["Vitamin B12", 200, 900, "pg/mL", "Vitamins", "Critical"],

    # Inflammation
    ["CRP", 0, 5, "mg/L", "Inflammation", "Critical"],

    # Heart
    ["Troponin", 0, 0.04, "ng/mL", "Heart", "Critical"],
    ["Blood Pressure Systolic", 90, 120, "mmHg", "Heart", "Critical"],
    ["Blood Pressure Diastolic", 60, 80, "mmHg", "Heart", "Critical"]
]

# Create DataFrame
df = pd.DataFrame(data, columns=["test", "min", "max", "unit", "category", "severity"])

# Save to CSV
df.to_csv("normal_ranges.csv", index=False)

print("CSV file created successfully ✅")