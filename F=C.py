#!/usr/bin/env python

# Author: Alejandro Hurtado
# Date: 07/21/2024
# This program calculates the day of the week on which you will return after a holiday.

# Prompt the user to enter the starting day number (0 to 6) and the length of stay in nights
start_day = int(input("Enter the starting day number (0 for Sunday, 6 for Saturday): "))
length_of_stay = int(input("Enter the length of your stay in nights: "))

# Calculate the return day number
return_day = (start_day + length_of_stay) % 7

# Print the result
print(f"You will return home on day number {return_day}.")