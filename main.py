import pandas as pd

from Utils.DataPlotter import DataPlotter
from Data.data_urls import *


def get_mortality_data_by_date():
    data = pd.read_json(MORTALITY)
    return data.groupby("DATE")


if __name__ == "__main__":
    mort = get_mortality_data_by_date()
    graph = DataPlotter(mort, 0, 0)
    graph.plot_graph()
