import pandas as pd
import numpy as np
import plotly.graph_objects as go

from Data.data_urls import *


def plot_covid_19_mortality():
    # Load data and print columns (for reference)
    data = pd.read_json(MORTALITY)
    print(data.columns)

    # Group data and verify by printing aggregated DEATHS
    grouped_data = data.groupby("DATE")
    print(grouped_data["DEATHS"].agg(np.sum))

    # Create figure and add axes
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(grouped_data.groups), y=list(grouped_data["DEATHS"].agg(np.sum))))

    # Set title
    fig.update_layout(title_text="Covid-19 Evolution over time in Belgium")

    # Add range slider
    fig.update_layout(xaxis=dict(rangeselector=dict(buttons=list([dict(count=1, label="1m", step="month",
                                                                       stepmode="backward"), dict(count=6, label="6m",
                                                                                                  step="month",
                                                                                                  stepmode="backward"),
                                                                  dict(count=1, label="YTD", step="year",
                                                                       stepmode="todate"),
                                                                  dict(count=1, label="1y", step="year",
                                                                       stepmode="backward"), dict(step="all")])),
                                 rangeslider=dict(visible=True), type="date"))

    fig.show()


if __name__ == "__main__":
    plot_covid_19_mortality()
