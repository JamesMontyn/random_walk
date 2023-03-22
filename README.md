# Random Walk
This simple program will generate a random walk that is able to look exactly like a real stock chart.
The idea is inspired by the book "A random walk down wall street", where Burton Malkiel mentions an experiment where
he created an artificial stock chart just by deciding if the price goes up or down on a day based on a coinflip.
With this he tried to show that the price movement in the stock market is highly unpredictable.

With this program I take Malkiel's experiment further. This program will generate an artificial stock chart based on
choosing a closing, high, and low price of each day within a configurable maximum deviation uniformly. Say, I have an
opening price of today of 100, and I configured my maximum deviation of the closing prices to be 0.02 or 2% of the
opening price, then my range of prices to choose from is \[98,102\]. The program will uniformly choose a price from this
range to generate the closing price of today. Eventually, we will have the data of the artificial stock chart, and we
can plot it as a bar chart. You will be surprised how much it will look just like an actual stock chart and will make
you think twice about your conception on technical analysis and the overall price movement of stock markets.

# How it works
The program consists of a main menu and submenu's, which act as the interface to the `RandomWalk` class that implements
the random walk generating. The menus are used to configure the generator, plot the random walk, generate a new
random walk with the same configuration and to plot the random walk to a csv file. When plotting your generated random
walk a window will pop up with the bar chart of the random walk.

# Running the program
To run the program you will need Python3 and the modules in `requirements.txt`.
If you have everything installed you can simply execute the following command to run the program:
```python3 app.py```
