# Alex Hurtado
# Date: 2024-08-11


# Function to check if a number is in the specified range
def check_in_range(number):
    """
    Check whether a given number is in the range 1 to 9 (inclusive).

    Parameters:
    number (int): The number to check.

    Returns:
    str: A message indicating whether the number is in the range or not.
    """
    # range(1, 10) generates numbers from 1 to 9 (1 is inclusive, 10 is exclusive)
    if number in range(1, 10):
        return f"{number} is in the range."
    else:
        return f"{number} is not in the range."


# Example usage:
num = 7  # You can change this value to test with different numbers
print(check_in_range(num))