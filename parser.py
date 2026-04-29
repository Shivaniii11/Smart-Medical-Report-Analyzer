import re
import pandas as pd

ranges = pd.read_csv("normal_ranges.csv")

def extract_values(text):
    results = []

    for _, row in ranges.iterrows():
        test = row["test"]

        pattern = rf"{re.escape(test)}\s*[:\-]?\s*(\d+\.?\d*)"
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            value = float(match.group(1))

            status = "Normal"
            if value < row["min"]:
                status = "Low"
            elif value > row["max"]:
                status = "High"

            results.append([
                test, value, row["unit"],
                row["min"], row["max"],
                status, row["category"]
            ])

    return pd.DataFrame(results, columns=[
        "Test", "Value", "Unit",
        "Min", "Max", "Status", "Category"
    ])