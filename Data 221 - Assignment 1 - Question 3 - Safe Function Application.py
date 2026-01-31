# Question 3: define a function that computes x^y. Then gives a list of pairs (x, y):

def function_computing_x_to_the_power_of_y(base_number, exponent_number):
    return base_number**exponent_number

list_of_result = []
listed_pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]

for x, y in listed_pairs:
    if y < 0:
        continue

    resulted_value = function_computing_x_to_the_power_of_y(x, y)
    list_of_result.append(resulted_value)

print(list_of_result)