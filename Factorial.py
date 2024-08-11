
# Alex Hurtado
# Date: 2024-08-11
# Problem 6: Calculate the factorial of a user input value using a for loop and compare with math.factorial().

import math

# Get user input for the number
n = int(input("Enter a number: "))

# Initialize factorial variable
factorial = 1

# Calculate factorial using a for loop
for i in range(1, n + 1):
    factorial *= i

# Calculate factorial using the math module
calculated_factorial = math.factorial(n)

# Print both results for comparison
print(f"Factorial (using for loop): {factorial}")
print(f"math.factorial() value: {calculated_factorial}")