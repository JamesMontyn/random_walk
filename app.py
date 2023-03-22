from random_walk import RandomWalk


def start_price_menu():
    start_price = 0
    while True:
        try:
            start_price = float(input("Enter starting price of the stock (e.g. 100): "))
        except ValueError or start_price < 0:
            print("This is not a valid starting price, it must be a positive number.")
        else:
            return start_price


def close_price_deviation_menu():
    close_price_deviation = 0
    while True:
        try:
            close_price_deviation = float(input("Enter maximum deviation of the close price from the open price "
                                                "(e.g. 0.02): "))
        except ValueError or close_price_deviation < 0 or close_price_deviation > 1:
            print("This is not a valid percentile, it must be a positive number.")
        else:
            return close_price_deviation


def high_price_deviation_menu():
    high_price_deviation = 0
    while True:
        try:
            high_price_deviation = float(input("Enter maximum deviation of the high price from the close price "
                                               "(e.g. 0.02): "))
        except ValueError or high_price_deviation < 0 or high_price_deviation > 1:
            print("This is not a valid percentile, it must be a positive number between 0 and 1.")
        else:
            return high_price_deviation


def low_price_deviation_menu():
    low_price_deviation = 0
    while True:
        try:
            low_price_deviation = float(input("Enter maximum deviation of the low price from the close price "
                                              "(e.g. 0.02): "))
        except ValueError or low_price_deviation < 0 or low_price_deviation > 1:
            print("This is not a valid percentile, it must be a positive number.")
        else:
            return low_price_deviation


def random_seed_menu():
    random_seed = 0
    while True:
        try:
            random_seed = int(input("Enter a number to be used as the seed for the random number generator"
                                    "(e.g. 5): "))
        except ValueError or random_seed < 0:
            print("This is not a valid percentile, it must be a positive number.")
        else:
            return random_seed


def number_of_days_menu():
    number_of_days = 0
    while True:
        try:
            number_of_days = int(input("Enter how many days the chart will consist of"
                                       "(e.g. 100): "))
        except ValueError or number_of_days < 0:
            print("This is not a valid number.")
        else:
            return number_of_days


def configure_random_walk_menu(random_walk: RandomWalk):
    while True:
        input_number = 0
        try:
            input_number = int(input("\nWhat would you like to configure?\n"
                                     "\'1\': The whole generator\n"
                                     "\'2\': The random seed\n"
                                     "\'3\': The starting price\n"
                                     "\'4\': The number of days of the random walk\n"
                                     "\'5\': The deviation of the closing prices from the opening prices\n"
                                     "\'6\': The deviation of the high prices from the opening prices\n"
                                     "\'7\': The deviation of the low prices from the opening prices\n"
                                     "\'8\': Go back to main menu\n"))
        except ValueError or not (1 >= input_number <= 7):
            print("This is not a valid input, only numbers between 1 and 8 are valid.")
        else:
            if input_number == 1:
                random_walk.set_seed_random_generator(random_seed_menu())
                random_walk.set_start_price(start_price_menu())
                random_walk.set_number_of_days(number_of_days_menu())
                random_walk.set_close_price_deviation(close_price_deviation_menu())
                random_walk.set_high_price_deviation(high_price_deviation_menu())
                random_walk.set_low_price_deviation(low_price_deviation_menu())
            elif input_number == 2:
                random_walk.set_seed_random_generator(random_seed_menu())
            elif input_number == 3:
                random_walk.set_start_price(start_price_menu())
            elif input_number == 4:
                random_walk.set_number_of_days(number_of_days_menu())
            elif input_number == 5:
                random_walk.set_close_price_deviation(close_price_deviation_menu())
            elif input_number == 6:
                random_walk.set_high_price_deviation(high_price_deviation_menu())
            elif input_number == 7:
                random_walk.set_low_price_deviation(low_price_deviation_menu())
            else:
                break


def filename_csv_menu():
    while True:
        filename = input("Enter a filename to export the random walk to (e.g. \'filename.csv\': ")
        print(filename, filename[-4:])
        if len(filename) <= 4 or filename[-4:] != ".csv":
            print("This is not a valid filename. Make sure it ends in \'.csv\'")
        else:
            return filename


def main():
    random_walk = RandomWalk()
    while True:
        input_number = 0
        try:
            input_number = int(input("\nWhat would you like to do? (input number)\n"
                                     "\'1\': Plot random walk\n"
                                     "\'2\': Generate new random walk\n"
                                     "\'3\': Configure random walk generator\n"
                                     "\'4\': Print current configuration\n"
                                     "\'5\': Export random walk to csv file\n"
                                     "\'6\': Quit program\n"))
        except ValueError or not (1 >= input_number <= 5):
            print("This is not a valid input, only numbers between 1 and 6 are valid.")
        else:
            if input_number == 1:
                random_walk.plot_random_walk()
            elif input_number == 2:
                random_walk.generate_random_walk()
            elif input_number == 3:
                configure_random_walk_menu(random_walk)
            elif input_number == 4:
                random_walk.print_configuration()
            elif input_number == 5:
                random_walk.export_random_walk_to_csv(filename_csv_menu())
            else:
                print("Thank you for trying out the random walk generator!")
                break


if __name__ == "__main__":
    print("--------===== Random Walk Generator =====--------\n"
          "Made by James Montyn at github.com/JamesMontyn\n"
          "\n")
    main()
