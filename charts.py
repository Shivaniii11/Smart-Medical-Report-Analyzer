import plotly.express as px

def plot_data(df):
    return px.bar(
        df,
        x="Test",
        y="Value",
        color="Status",
        title="Medical Report Chart"
    )