#!/usr/bin/env python

# Author: Alejandro Hurtado
# Date: 07/21/2024
# This program converts degrees Fahrenheit to degrees Celsius.

# Prompt the user to enter the temperature in Fahrenheit
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Print the result
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")