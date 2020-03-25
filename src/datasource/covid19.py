from datetime import datetime
from functools import partial, reduce
from time import mktime
import json
from operator import concat, is_not
import os
import requests

class Covid19:

    DATA_URL = "https://pomber.github.io/covid19/timeseries.json"

    def __init__(self):
        if "ENVIRONMENT" in os.environ and os.environ["ENVIRONMENT"] == 'test':
            with open('src/example-data/timeseries.min.json', 'rb') as file:
                self.data = json.load(file)
        else:
            response = requests.get(self.DATA_URL)
            self.data = response.json()

    def countries(self):
        return sorted(self.data.keys())

    def metrics(self):
        metrics = list(map(lambda country: [
            country + ":confirmed",
            country + ":deaths",
            country + ":recovered"
        ], self.countries()))
        return reduce(concat, metrics)

    # Timeseries Response
    # [
    #   {
    #     "target":"upper_75", // The field being queried for
    #     "datapoints":[
    #       [622,1450754160000],  // Metric value as a float , unixtimestamp in milliseconds
    #       [365,1450754220000]
    #     ]
    #   },
    #   {
    #     "target":"upper_90",
    #     "datapoints":[
    #       [861,1450754160000],
    #       [767,1450754220000]
    #     ]
    #   }
    # ]
    def timeseries(self, target, from_date, to_date):
        country, group = target.split(":")
        country_data = self.data[country]
        from_date_dt, to_date_dt = self.convert_input_dates(from_date, to_date)
        series = list(map(
            lambda datapoint: self.filter_datapoint(datapoint, group, from_date_dt, to_date_dt), country_data
        ))

        return list(filter(partial(is_not, None), series))

    @staticmethod
    def filter_datapoint(datapoint, group, from_date_dt, to_date_dt):
        datapoint_dt = mktime(datetime.strptime(datapoint["date"], "%Y-%m-%d").timetuple())
        if from_date_dt <= datapoint_dt <= to_date_dt:
            try:
                return [float(datapoint[group]), int(datapoint_dt * 1000)]
            except KeyError:
                return [0, int(datapoint_dt * 1000)]
        else:
            return None

    @staticmethod
    def convert_input_dates(from_date, to_date):
        date_format = '%Y-%m-%dT%H:%M:%S.%fZ'
        return [
            mktime(datetime.strptime(from_date, date_format).timetuple()),
            mktime(datetime.strptime(to_date, date_format).timetuple())
        ]
