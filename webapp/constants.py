from enum import Enum
import pandas as pd

class WorkTime():
    DEFAULT = 96600.0

class WorkMultiplier():
    OPD = 7.2
    IPD = 20.0
    ER  =15.0
    ICU = 60.0
    LABOUR = 15.0

def calculate_workload(data):

    minute_per_day = data['opd'] * WorkMultiplier.OPD
    minute_per_day += data['ipd'] * WorkMultiplier.IPD
    minute_per_day += data['er'] * WorkMultiplier.ER
    minute_per_day += data['icu'] * WorkMultiplier.ICU
    minute_per_day += data['labour'] * WorkMultiplier.LABOUR

    minute_per_year = minute_per_day/5*230*1.15
    human = minute_per_year/WorkTime.DEFAULT

    return minute_per_day, minute_per_year, human

province_df = pd.read_csv("data/thai.csv")
province_choices = [tuple(row) for row in province_df.itertuples(index=False)]



