import pandas as pd

from Data.data_urls import *


def get_mortality_by_date():
    _data = pd.read_json(MORTALITY)
    return _data.groupby("DATE")


def get_cases_by_date():
    _data = pd.read_json(CONFIRMED_DETAILED)
    return _data.groupby("DATE")


def get_cases_by_province():
    _data = pd.read_json(CONFIRMED_DETAILED)
    return _data.groupby("PROVINCE")


def get_hosp_by_date():
    _data = pd.read_json(HOSPITALISATIONS)
    return _data.groupby("DATE")


def get_tests_by_date():
    _data = pd.read_json(TOTAL_TESTS)
    return _data.groupby("DATE")


class DataFeeder:
    @classmethod
    def feed(cls):
        mort = {"data": get_mortality_by_date(), "key": "DEATHS", "grouped_by": "DATE", "target_fig": 1}
        cases_date = {"data": get_cases_by_date(), "key": "CASES", "grouped_by": "DATE", "target_fig": 1}
        cases_province = {"data": get_cases_by_province(), "key": "CASES", "grouped_by": "PROVINCE", "target_fig": 2}
        hosp_in = {"data": get_hosp_by_date(), "key": "NEW_IN", "grouped_by": "DATE", "target_fig": 1}
        hosp_out = {"data": get_hosp_by_date(), "key": "NEW_OUT", "grouped_by": "DATE", "target_fig": 1}
        hosp_icu = {"data": get_hosp_by_date(), "key": "TOTAL_IN_ICU", "grouped_by": "DATE", "target_fig": 1}
        hosp_total = {"data": get_hosp_by_date(), "key": "TOTAL_IN", "grouped_by": "DATE", "target_fig": 1}
        tests = {"data": get_tests_by_date(), "key": "TESTS_ALL", "grouped_by": "DATE", "target_fig": 1}

        # the sequence of returning data is important as this will otherwise screw with the labels
        return [cases_date, hosp_in, hosp_out, hosp_icu, hosp_total, mort, tests, cases_province]
