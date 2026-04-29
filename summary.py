def generate_summary(df):

    if df.empty:
        return "No values found."

    abnormal = df[df["Status"] != "Normal"]

    summary = f"Total Tests: {len(df)}\n"
    summary += f"Abnormal Values: {len(abnormal)}\n\n"

    for _, row in abnormal.iterrows():
        summary += f"- {row['Test']} is {row['Status']} ({row['Value']} {row['Unit']})\n"

    return summary