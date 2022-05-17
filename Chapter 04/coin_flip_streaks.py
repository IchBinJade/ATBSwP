# Write a program to find out how often a streak of 6 heads
# or a streak of 6 tails occurs in a randomly generated list
# of heads and tails

import random

number_of_streaks = 0
streak_count = 0

for experiment_number in range(10000):
    # Part 1: Generate list of 100 H/T values
    coin_list = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            coin = "H"
        else:
            coin = "T"

        coin_list.append(coin)

    # Part 2: Check for a streak
    for j in range(len(coin_list)):
        # Ignore the first index
        if j == 0:
            pass
        elif coin_list[j] == coin_list[j - 1]:
            streak_count += 1
        else:
            streak_count = 0

        if streak_count == 6:
            number_of_streaks += 1

print("Chance of streak: {}".format(number_of_streaks / 100))
