# Alex Hurtado
# Date: 2024-08-11


import math


# Function to calculate the area of a circle given its radius
def areaOfCircle(r):
    """
    Calculate and return the area of a circle with radius r.

    Parameters:
    r (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    # Use the math.pi constant for π and calculate the area using the formula A = π * r^2
    area = math.pi * (r ** 2)
    return area


# Example usage:
radius = 5.0  # You can change this value to test with different radii
print(f"The area of a circle with radius {radius} is {areaOfCircle(radius)}")