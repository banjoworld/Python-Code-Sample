# Alex Hurtado
# Date: 2024-08-11


# Function to multiply all the numbers in a list
def multiply_list(numbers):
    """
    Multiply all the numbers in the provided list.

    Parameters:
    numbers (list): A list of numbers to be multiplied.

    Returns:
    int or float: The product of all the numbers in the list.
    """
    # Initialize the product variable to 1 (since we're multiplying)
    product = 1

    # Loop through each number in the list and multiply it with the product variable
    for num in numbers:
        product *= num

    return product


# Example usage:
num_list = [5, 2, 7, -1]  # List of numbers to multiply
print(f"The product of the numbers in the list {num_list} is {multiply_list(num_list)}")