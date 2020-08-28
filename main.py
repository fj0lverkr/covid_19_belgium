import dash
from Utils.DataPlotter import DataPlotter
from Utils.DataFeeder import DataFeeder


dashboard_heading = "Covid-19 dashboard Belgium."
figure_matrix = [[1], [2, 3]]
graph_titles = ["Evolution over time.", "Cases per province.", "Mortality by age group and sex."]
dashboard = DataPlotter(DataFeeder.feed(), dashboard_heading, graph_titles, figure_matrix)
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css',
                        'https://fonts.googleapis.com/css2?family=Work+Sans:wght@200;300;400&display=swap']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, title="Covid-19 Belgium")
app.layout = dashboard.plot_graph()
server = app.server

# comment this out when running this through a WSGI file:
app.run_server(debug=False)
