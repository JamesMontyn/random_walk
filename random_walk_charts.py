import pandas as pd
import mplfinance as mpf
import random
from datetime import date, timedelta

random_seed = 0
open_price = 0  # first open price
close_price = 0
high_price = 0
low_price = 0
close_price_deviation = 0  # deviation from open price
high_price_deviation = 0  # deviation from close price
low_price_deviation = 0  # deviation from close price
number_of_days = 0

# TODO: generic function for gathering user input
while True:
    try:
        open_price = float(input("Enter starting price of the stock: "))
    except ValueError or open_price < 0:
        print("This is not a valid starting price, it must be a positive number.")
    else:
        break

while True:
    try:
        close_price_deviation = float(input("Enter maximum deviation of the close price from the open price in "
                                            "percentile: "))
    except ValueError or close_price_deviation < 0:
        print("This is not a valid percentile, it must be a positive number.")
    else:
        break

while True:
    try:
        high_price_deviation = float(input("Enter maximum deviation of the high price from the close price in "
                                           "percentile: "))
    except ValueError or high_price_deviation < 0:
        print("This is not a valid percentile, it must be a positive number.")
    else:
        break

while True:
    try:
        low_price_deviation = float(input("Enter maximum deviation of the low price from the close price in "
                                          "percentile: "))
    except ValueError or low_price_deviation < 0:
        print("This is not a valid percentile, it must be a positive number.")
    else:
        break

while True:
    try:
        random_seed = int(input("Enter a number to be used as the seed for the random number generator"
                                ": "))
    except ValueError or random_seed < 0:
        print("This is not a valid percentile, it must be a positive number.")
    else:
        break

while True:
    try:
        number_of_days = int(input("Enter how many days the chart will consist of"
                                   ": "))
    except ValueError or number_of_days < 0:
        print("This is not a valid number.")
    else:
        break

# TODO: being able to use other than uniform distributions?

print("You have configured the random walk chart as follows: \n"
      f"Starting price: {open_price}\n"
      f"Close price deviation: {close_price_deviation}\n"
      f"High price deviation: {high_price_deviation}\n"
      f"Low price deviation: {low_price_deviation}\n"
      f"Number of days: {number_of_days}\n"
      f"Random seed: {random_seed}")

random.seed(random_seed)

date = date.today()
fictionary_date_list = []
open_price_list = []
close_price_list = []
high_price_list = []
low_price_list = []

for _ in range(number_of_days):
    close_price = open_price + open_price * random.uniform(-close_price_deviation, close_price_deviation)
    high_price = close_price + close_price * random.uniform(0, high_price_deviation)
    low_price = close_price - close_price * random.uniform(0, low_price_deviation)
    date += timedelta(days=1)
    fictionary_date_list.append(date)
    open_price_list.append(open_price)
    close_price_list.append(close_price)
    high_price_list.append(high_price)
    low_price_list.append(low_price)
    open_price = close_price

chart_data = pd.DataFrame(index=pd.to_datetime(fictionary_date_list),
                          data={'Open': open_price_list,
                                'High': high_price_list,
                                'Low': low_price_list,
                                'Close': close_price_list})
print(chart_data)
mpf.plot(chart_data)
