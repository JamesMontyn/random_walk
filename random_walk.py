import pandas as pd
import mplfinance as mpf
import random

from datetime import date, timedelta


class RandomWalk:
    def __init__(self, seed=1, start_price=100, close_price_deviation=0.02, high_price_deviation=0.02,
                 low_price_deviation=0.02, number_of_days=100):
        self.random_walk_df = None
        self.seed = seed
        random.seed(seed)
        self.start_price = start_price
        self.close_price_deviation = close_price_deviation
        self.high_price_deviation = high_price_deviation
        self.low_price_deviation = low_price_deviation
        self.number_of_days = number_of_days

    def set_seed_random_generator(self, seed):
        self.seed = seed
        random.seed(seed)

    def set_start_price(self, start_price):
        self.start_price = start_price

    def set_close_price_deviation(self, close_price_deviation):
        self.close_price_deviation = close_price_deviation

    def set_high_price_deviation(self, high_price_deviation):
        self.high_price_deviation = high_price_deviation

    def set_low_price_deviation(self, low_price_deviation):
        self.low_price_deviation = low_price_deviation

    def set_number_of_days(self, number_of_days):
        self.number_of_days = number_of_days

    def print_configuration(self):
        print("You have configured the random walk as follows: \n"
              f"Starting price: {self.start_price}\n"
              f"Close price deviation: {self.close_price_deviation}\n"
              f"High price deviation: {self.high_price_deviation}\n"
              f"Low price deviation: {self.low_price_deviation}\n"
              f"Number of days: {self.number_of_days}\n"
              f"Random seed: {self.seed}")

    def generate_random_walk(self):
        curr_date = date.today()
        fictionary_date_list = []  # needed for dataframe index and plotting (x-axis)
        open_price_list = []
        close_price_list = []
        high_price_list = []
        low_price_list = []
        open_price = self.start_price

        for _ in range(self.number_of_days):
            # generating close, high and low prices and going forward one date
            close_price = open_price + open_price * random.uniform(-self.close_price_deviation,
                                                                   self.close_price_deviation)
            high_price = close_price + close_price * random.uniform(0, self.high_price_deviation)
            low_price = close_price - close_price * random.uniform(0, self.low_price_deviation)
            curr_date += timedelta(days=1)

            # storing the generated data in the corresponding lists
            fictionary_date_list.append(curr_date)
            open_price_list.append(open_price)
            close_price_list.append(close_price)
            high_price_list.append(high_price)
            low_price_list.append(low_price)

            open_price = close_price

        # making a pandas dataframe from the lists with the generated data
        self.random_walk_df = pd.DataFrame(index=pd.to_datetime(fictionary_date_list),
                                           data={'Open': open_price_list,
                                                 'High': high_price_list,
                                                 'Low': low_price_list,
                                                 'Close': close_price_list})

    def plot_random_walk(self):
        if self.random_walk_df is None:
            self.generate_random_walk()

        mpf.plot(self.random_walk_df, type='candle', title='Your random walk chart')

    def export_random_walk_to_csv(self, filename):
        if self.random_walk_df is None:
            self.generate_random_walk()

        self.random_walk_df.to_csv(filename)
