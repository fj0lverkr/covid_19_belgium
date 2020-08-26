import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objects as go


class DataPlotter:
    def __init__(self, data, title, matrix):
        self.data = data
        self.title = title
        self.matrix = matrix

    def plot_graph(self):
        container_children = []
        row_no = 1

        # create figures
        for row in self.matrix:
            row_children = []
            for col in row:
                col_children = []
                fig = go.Figure()

                # Add plots
                for d in self.data:
                    data_groups = d["data"].groups
                    data_target = d["target_fig"]
                    data_key = d["key"]
                    data_values = d["data"][data_key].agg(np.sum)
                    if data_target == 1 and data_target == col:
                        fig.add_trace(go.Scatter(x=list(data_groups), y=list(data_values),
                                                 name=data_key.replace("_", " ").title(), yaxis="y"))
                        # Set title
                        fig.update_layout(title_text=self.title)

                        # Add range slider
                        fig.update_layout(
                            xaxis=dict(rangeselector=dict(buttons=list([dict(count=1, label="1m", step="month",
                                                                             stepmode="backward"),
                                                                        dict(count=6, label="6m",
                                                                             step="month",
                                                                             stepmode="backward"),
                                                                        dict(count=1, label="YTD", step="year",
                                                                             stepmode="todate"),
                                                                        dict(count=1, label="1y", step="year",
                                                                             stepmode="backward"), dict(step="all")])),
                                       rangeslider=dict(visible=True), type="date"))
                    elif data_target == 2 and data_target == col:
                        fig.add_trace(
                            go.Pie(
                                labels=list(data_groups),
                                values=list(data_values),
                                textinfo='label+value',
                                insidetextorientation='radial'
                            )
                        )
                col_children.append(dcc.Graph(figure=fig))
                div_col = html.Div(children=col_children,className=f"col-{int(12/len(row))}",
                                   id=f"row_{row_no}_col_{col}")
                row_children.append(div_col)
            div_row = html.Div(children=row_children, className="row", id=f"row_{row_no}")
            container_children.append(div_row)
            row_no += 1
        return html.Div(children=container_children, className="container-fluid")
