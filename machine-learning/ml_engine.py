from prophet import Prophet


class MLPredictor(object):
    def __init__(self, data_df):
        """
        :param data_df: Dataframe type dataset
        """
        self.train_data = self.convert_col_name(data_df)
        self.trainer = Prophet(changepoint_prior_scale=12)

    def train(self):
        self.trainer.fit(self.train_data)

    def convert_col_name(self, data_df):
        data_df.rename(columns={"Timestamp": "ds", "Value": "y"}, inplace=True)

        print(f"After rename columns \n{data_df.columns}")
        return data_df

    def make_future(self, periods=15):
        future = self.trainer.make_future_dataframe(periods=periods)
        return future

    def predict(self):
        future = self.make_future()
        forecast = self.trainer.predict(future)
        return forecast

    def plot_result(self, forecast):
        fig = self.trainer.plot(forecast, figsize=(15, 6))
        return fig
