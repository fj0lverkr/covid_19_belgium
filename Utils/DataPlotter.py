import numpy as np
import plotly.graph_objects as go


class DataPlotter:
    def __init__(self, data, title):
        self.data = data
        self.title = title

    def plot_graph(self):
        # Create figure and add axes
        fig = go.Figure()
        for d in self.data:
            data_groups = d["data"].groups
            data_key = d["key"]
            data_values = d["data"][data_key].agg(np.sum)
            fig.add_trace(go.Scatter(x=list(data_groups), y=list(data_values), name=data_key.replace("_", " ").title(),
                                     yaxis="y"))

        # Set title
        fig.update_layout(title_text=self.title)

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
