# Alex Hurtado
# Date: 2024-08-11

# Function to return a list of unique elements from the provided list
def unique_elements(numbers):
    """
    Return a new list containing unique elements from the original list.

    Parameters:
    numbers (list): A list of numbers which may contain duplicates.

    Returns:
    list: A new list containing only the unique elements from the original list.
    """
    unique_list = []  # Initialize an empty list to store unique elements

    # Loop through each number in the original list
    for num in numbers:
        # If the number is not already in the unique_list, add it
        if num not in unique_list:
            unique_list.append(num)

    return unique_list


# Example usage:
num_list = [1, 3, 3, 3, 6, 2, 3, 5]  # Original list with duplicates
print(f"The list of unique elements is: {unique_elements(num_list)}")