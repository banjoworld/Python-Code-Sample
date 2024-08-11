
# Alex Hurtado
# Date: 2024-08-11
# Problem 3: Select a random day of the week from a list and print that day.

import random

# List of days in a week
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# random.choice selects a random element from the days_of_week list
random_day = random.choice(days_of_week)
print(random_day)