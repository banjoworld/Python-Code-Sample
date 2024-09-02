# Alex Hurtado
# Date: 2024-09-01
# Problem 4: Create a while loop that initializes a counter at 0 and runs until the counter reaches 50.
# If the value of the counter is divisible by 10, append it to the list called tens.

tens = []
counter = 0

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print("List of tens:", tens)