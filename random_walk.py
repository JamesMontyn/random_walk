#!/usr/bin/env python
"""Random walk class.

This file contains the RandomWalk class that will generate a random walk from set configuration.
"""

import pandas as pd
import mplfinance as mpf
import random as random

from datetime import date, timedelta

__author__ = "James Montyn"
__version__ = "1.0"
__maintainer__ = "James Montyn"
__email__ = "JamesMontyn@gmail.com"
__status__ = "Production"


class RandomWalk:
    """Random walk generator class

    Private variables
    -----------------
    _random_walk_df: Pandas Dataframe
        holds the current random walk data

    _seed: int
        the seed for the random generator

    _start_price: float
        the starting price of the random walk (price at day 0)

    _close_price_deviation: float
        the maximum deviation of the closing price on a day from the opening price,
        the random walk generator will uniformly choose a closing price that is within this deviation

    _high_price_deviation: float
        the maximum deviation of the highest price on a day from the opening price,
        the random walk generator will uniformly choose a high price that is within this deviation

    _low_price_deviation: float
        the maximum deviation of the lowest price on a day from the opening price,
        the random walk generator will uniformly choose a low price that is within this deviation

    _number_of_days: int
        number of days the random walk generator will create data,
        this is how many days are on the x-axis of the plot of the random walk
    """

    def __init__(self, seed: int = 1, start_price: float = 100, close_price_deviation: float = 0.02,
                 high_price_deviation: float = 0.02, low_price_deviation: float = 0.02,
                 number_of_days: int = 100):
        """Initiates all the private variables

        :param seed: int
        :param start_price: float
        :param close_price_deviation: float
        :param high_price_deviation: float
        :param low_price_deviation: float
        :param number_of_days: int
        """
        self._random_walk_df = None
        self._seed = seed
        random.seed(seed)
        self._start_price = start_price
        self._close_price_deviation = close_price_deviation
        self._high_price_deviation = high_price_deviation
        self._low_price_deviation = low_price_deviation
        self._number_of_days = number_of_days

    def set_seed_random_generator(self, seed: int) -> None:
        """Setter for _seed

        :param seed: int
        :return: None
        """
        self._seed = seed
        random.seed(seed)

    def set_start_price(self, start_price: float) -> None:
        """Setter for _start_price

        :param start_price: float
        :return: None
        """
        self._start_price = start_price

    def set_close_price_deviation(self, close_price_deviation: float) -> None:
        """Setter for _close_price_deviation

        :param close_price_deviation: float
        :return: None
        """
        self._close_price_deviation = close_price_deviation

    def set_high_price_deviation(self, high_price_deviation: float) -> None:
        """Setter for _high_price_deviation

        :param high_price_deviation: float
        :return: None
        """
        self._high_price_deviation = high_price_deviation

    def set_low_price_deviation(self, low_price_deviation: float) -> None:
        """Setter for _low_price_deviation

        :param low_price_deviation: float
        :return: None
        """
        self._low_price_deviation = low_price_deviation

    def set_number_of_days(self, number_of_days: int) -> None:
        """Setter for _number_of_days

        :param number_of_days: int
        :return: None
        """
        self._number_of_days = number_of_days

    def print_configuration(self) -> None:
        """Prints the current values of all the private variables

        :return: None
        """
        print("You have configured the random walk as follows: \n"
              f"Starting price: {self._start_price}\n"
              f"Close price deviation: {self._close_price_deviation}\n"
              f"High price deviation: {self._high_price_deviation}\n"
              f"Low price deviation: {self._low_price_deviation}\n"
              f"Number of days: {self._number_of_days}\n"
              f"Random seed: {self._seed}")

    def generate_random_walk(self) -> None:
        """Generates the random walk according to the configured private variables

        :return: None
        """
        curr_date = date.today()
        fictionary_date_list = []  # fictionary dates are needed for dataframe index and plotting (x-axis)
        open_price_list = []
        close_price_list = []
        high_price_list = []
        low_price_list = []
        open_price = self._start_price

        # will randomly generate a closing price, high price and low price for each day
        for _ in range(self._number_of_days):
            # generating close, high and low prices and going forward one date
            close_price = open_price + open_price * random.uniform(-self._close_price_deviation,
                                                                   self._close_price_deviation)
            high_price = close_price + close_price * random.uniform(0, self._high_price_deviation)
            low_price = close_price - close_price * random.uniform(0, self._low_price_deviation)
            curr_date += timedelta(days=1)

            # storing the generated data in the corresponding lists
            fictionary_date_list.append(curr_date)
            open_price_list.append(open_price)
            close_price_list.append(close_price)
            high_price_list.append(high_price)
            low_price_list.append(low_price)

            open_price = close_price

        self._random_walk_df = pd.DataFrame(index=pd.to_datetime(fictionary_date_list),
                                            data={'Open': open_price_list,
                                                  'High': high_price_list,
                                                  'Low': low_price_list,
                                                  'Close': close_price_list})

    def plot_random_walk(self) -> None:
        """Plots the random walk that is stored in the data frame

        :return: None
        """
        # first generate a random walk if none has been generated yet
        if self._random_walk_df is None:
            self.generate_random_walk()

        mpf.plot(self._random_walk_df, type='candle', title='Your random walk chart')

    def export_random_walk_to_csv(self, filename: str) -> None:
        """Exports the random walk that is stored in the data frame to a csv file with the given filename

        :param filename: str
        :return: None
        """
        # first generate a random walk if none has been generated yet
        if self._random_walk_df is None:
            self.generate_random_walk()

        self._random_walk_df.to_csv(filename)
