import pandas as pd

from Data.data_urls import *


def get_mortality_by_date():
    _data = pd.read_json(MORTALITY)
    return _data.groupby("DATE")


def get_cases_by_date():
    _data = pd.read_json(CONFIRMED_DETAILED)
    return _data.groupby("DATE")


def get_hosp_by_date():
    _data = pd.read_json(HOSPITALISATIONS)
    return _data.groupby("DATE")


def get_tests_by_date():
    _data = pd.read_json(TOTAL_TESTS)
    return _data.groupby("DATE")


class DataFeeder:
    @classmethod
    def feed(cls):
        mort = {"data": get_mortality_by_date(), "key": "DEATHS"}
        cases = {"data": get_cases_by_date(), "key": "CASES"}
        hosp_in = {"data": get_hosp_by_date(), "key": "NEW_IN"}
        hosp_out = {"data": get_hosp_by_date(), "key": "NEW_OUT"}
        hosp_icu = {"data": get_hosp_by_date(), "key": "TOTAL_IN_ICU"}
        hosp_total = {"data": get_hosp_by_date(), "key": "TOTAL_IN"}
        tests = {"data": get_tests_by_date(), "key": "TESTS_ALL"}
        return [cases, hosp_in, hosp_out, hosp_icu, hosp_total, mort, tests]
