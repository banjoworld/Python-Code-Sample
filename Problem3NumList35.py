# Alex Hurtado
# Date: 2024-09-01
# Problem 3: Using a while loop, ask the user to enter a number.
# Append each entered number to a list and add them together until the sum is greater than 100.

numbers = []
total_sum = 0

while total_sum <= 100:
    num = int(input("Enter a number: "))
    numbers.append(num)
    total_sum += num

print("List of entered numbers:", numbers)
print("Total sum:", total_sum)