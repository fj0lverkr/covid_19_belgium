import numpy as np
import plotly.graph_objects as go


class DataPlotter:
    def __init__(self, mort, cases, hosp):
        self.mort = mort
        self.cases = cases
        self.hosp = hosp

    def plot_graph(self):
        # Create figure and add axes
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=list(self.mort.groups), y=list(self.mort["DEATHS"].agg(np.sum))))

        # Set title
        fig.update_layout(title_text="Covid-19 Evolution over time in Belgium")

        # Add range slider
        fig.update_layout(xaxis=dict(rangeselector=dict(buttons=list([dict(count=1, label="1m", step="month",
                                                                           stepmode="backward"),
                                                                      dict(count=6, label="6m",
                                                                           step="month",
                                                                           stepmode="backward"),
                                                                      dict(count=1, label="YTD", step="year",
                                                                           stepmode="todate"),
                                                                      dict(count=1, label="1y", step="year",
                                                                           stepmode="backward"), dict(step="all")])),
                                     rangeslider=dict(visible=True), type="date"))

        fig.show()
