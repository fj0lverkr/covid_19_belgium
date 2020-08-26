import dash
from Utils.DataPlotter import DataPlotter
from Utils.DataFeeder import DataFeeder

if __name__ == "__main__":
    graph_title = "Covid-19 evolution over time in Belgium."
    figure_matrix = [[1], [2, 3]]
    graph = DataPlotter(DataFeeder.feed(), graph_title, figure_matrix)
    external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.layout = graph.plot_graph()
    app.run_server(debug=False)
