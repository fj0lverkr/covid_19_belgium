from Utils.DataPlotter import DataPlotter
from Utils.DataFeeder import DataFeeder

if __name__ == "__main__":
    graph_title = "Covid-19 evolution over time in Belgium."
    graph = DataPlotter(DataFeeder.feed(), graph_title)
    graph.plot_graph()
