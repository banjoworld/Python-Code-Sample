
import math

# Initialize approximation variable
pi_approximation = 0

# Number of iterations for the approximation (more iterations = better accuracy)
iterations = 1000000

# Leibniz formula: Pi is approximated as 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 ...)
for i in range(iterations):
    pi_approximation += ((-1)**i) / (2*i + 1)

# Multiply by 4 to get the approximation of Pi
pi_approximation *= 4

# Print the approximated value and the actual value from math module
print(f"Approximated Pi: {pi_approximation}")
print(f"math.pi: {math.pi}")