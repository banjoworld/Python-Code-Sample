
# Alex Hurtado
# Date: 2024-08-11
# Problem 5: Convert a user input value from radians to degrees and compare with math.degrees().

import math

# Get user input for the value in radians
radians = float(input("Enter the value in radians: "))

# Convert radians to degrees manually
degrees = radians * (180 / math.pi)

# Use math.degrees to convert radians to degrees
calculated_degrees = math.degrees(radians)

# Print both results for comparison
print(f"Converted degrees: {degrees}")
print(f"math.degrees() value: {calculated_degrees}")