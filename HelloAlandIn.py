#!/usr/bin/env python

# Author: Alejandro Hurtado
# Date: 07/21/2024
# This program computes the area of a circle based on user input for the radius.

import math

# Prompt the user to enter the radius
radius = float(input("Enter the radius of the circle: "))

# Compute the area of the circle
area = math.pi * (radius ** 2)

# Print a message with the computed area
print(f"The area of the circle with radius {radius} is {area:.2f}.")