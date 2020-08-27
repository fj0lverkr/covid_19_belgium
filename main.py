import dash
from Utils.DataPlotter import DataPlotter
from Utils.DataFeeder import DataFeeder


figure_matrix = [[1], [2, 3]]
graph_titles = ["Covid-19 evolution over time in Belgium.", "Cases per province.", "Mortality by age group and sex"]
graph = DataPlotter(DataFeeder.feed(), graph_titles, figure_matrix)
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = graph.plot_graph()
server = app.server

# comment this out when running this through a WSGI file:
app.run_server(debug=False)
