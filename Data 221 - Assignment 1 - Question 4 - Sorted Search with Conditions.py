# Question 4: Given a list of random values between 0 and 1 and a random value x: sort the list, find indices.

from random import random

list_of_random_values = [random() for count in range(20)]
target_number = random()

list_of_random_values.sort()

matching_indices_list = []

for index in range (len(list_of_random_values)):
    if list_of_random_values[index] >= target_number:
        matching_indices_list.append(index)

print("Sorted list: ")
print(list_of_random_values)
print("Target value of x: ", target_number)

if len(matching_indices_list) > 0:
    print("First index where value >= target number: ", matching_indices_list[0])
else:
    print("No values in the list are greater than or equal to the target number.")