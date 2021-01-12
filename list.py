#!/usr/bin/env python3

# Created by Gabriel A
# Created on Jan 2021
# This program generates random integers

import random


def main():
    # this function uses an array

    random_number = []
    summ = 0

    # input
    for loop_counter in range(0, 10):
        a_single_number = random.randint(0, 100)
        random_number.append(a_single_number)

    print("Here are 10 completely random numbers:\n")

    for loop_counter in range(0, 10):
        print("{0} ".format(random_number[loop_counter]), end="")

    for loop_counter in range(0, 10):
        summ += random_number[loop_counter]

    average = summ / 10

    print("\n\nThe average of the 10 numbers is: {0}".format(average))


if __name__ == "__main__":
    main()
