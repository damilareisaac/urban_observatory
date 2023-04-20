import pandas as pd
import requests


class DataInjector:
    def __init__(self, slice="PM2.5"):
        self.url = "http://uoweb3.ncl.ac.uk/api/v1.1/sensors/PER_AIRMON_MONITOR1135100/data/json/?starttime=20220601&endtime=20220831"
        self.slice = slice

        # get data from source
        self.resp_data = self.get_data()

        # print raw response data
        print(self.resp_data)

        # get slice of sensor parameters
        self.slice_data = self.get_slice_data()

        # get response as dataframe
        self.resp_data_frame = self.convert_resp_slice_to_data_frame()

        self.time_value_dict = self.get_time_value_dict_from_dataframe()

    def get_data(self):
        print(f"getting data from server")
        # Request data from source (Urban Observatory Platform)
        resp = requests.get(self.url)
        # get json  from response
        resp_dict = resp.json()
        return resp_dict

    def get_slice_data(self):
        # get data slice from response
        resp_pm_25 = self.resp_data["sensors"][0]["data"][self.slice]
        return resp_pm_25

    def convert_resp_slice_to_data_frame(self):
        df = pd.DataFrame(self.slice_data)
        return df

    def get_time_value_dict_from_dataframe(self):
        print(f" getting timestamp and value from dataframe...")
        time_value_df = self.resp_data_frame[["Timestamp", "Value"]]
        time_value_dict = time_value_df.to_dict()

        print(f"COMPLETED! Returned timestamp")

        return time_value_dict

    @property
    def time_series_data(self):
        return self.time_value_dict
