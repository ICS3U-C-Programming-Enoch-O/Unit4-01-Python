#!/usr/bin/env python3
# Created by: Enoch O
# Created on: March 28, 2025
# This program will calculate the sum of the numbers the user inputs using loop.
def main():
    # This Function uses a while loop
    loop_counter = 0
    total_sum = 0

    # Get user number
    while True:
        try:
            positive_integer_str = input("Enter a positive integer:")
            positive_integer = int(positive_integer_str)
            if positive_integer >= 0:
                break
            else:
                print("please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. please enter an integer ")
            print("")

    # Ask user for their input
    positive_integer = int(input("Enter amount of times to repeat:"))
    print("")

    # process users input and Display total sum
    while loop_counter < positive_integer:
        print("{0} time through loop".format(loop_counter))
        loop_counter = loop_counter + 1

    print(f"The sum of numbers from 0 to {positive_integer} is: {total_sum}")


if __name__ == "__main__":
    main()
