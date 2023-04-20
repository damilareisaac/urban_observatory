import pandas as pd


class DataPreprocessor:
    def __init__(self, data_from_mqtt_subscriber):
        self.raw_data = data_from_mqtt_subscriber

        # filter outliers
        self.outliers = self.filter_outliers()

        print(f"printing outliers", flush=True)
        print(self.outliers, flush=True)

        self.average_by_day = self.compute_average_by_day()

    def filter_outliers(self):
        # convert raw data to dataframe
        data_df = pd.DataFrame(self.raw_data)

        # filter outliers (values > 50)
        outliers = data_df.loc[data_df["Value"] > 50]

        # return all outliers as dictionary object
        return outliers

    def compute_average_by_day(self):
        df_without_outliers = self.compute_values_without_outliers()

        df_without_outliers.Timestamp = pd.to_datetime(
            df_without_outliers.Timestamp / 1000, unit="s"
        )

        average_by_days = (
            df_without_outliers.groupby([pd.Grouper(key="Timestamp", freq="D")])
            .Value.mean()
            .reset_index()
        )

        print(average_by_days)

        average_by_days.Timestamp = average_by_days.Timestamp.astype("str")

        return average_by_days

    def compute_values_without_outliers(self):
        data_df = pd.DataFrame(self.raw_data)
        values = data_df.loc[data_df["Value"] <= 50]
        return values

    @property
    def average_by_days(self):
        return self.average_by_day.to_dict()
