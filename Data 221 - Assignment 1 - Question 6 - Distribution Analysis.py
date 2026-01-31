# Question 6: Define a function that receives a list of numbers and returns a dictionary.

def distribution_analysis(list_of_numbers):
    returning_dictionary = {}

    total_number_of_count = len(list_of_numbers)

    sorted_list_of_numbers = sorted(set(list_of_numbers))

    for currentValue in sorted_list_of_numbers:
        counter_for_less_or_equal_to_currentValue = 0

        for number in list_of_numbers:
            if number <= currentValue:
                counter_for_less_or_equal_to_currentValue += 1

        percent = (counter_for_less_or_equal_to_currentValue / total_number_of_count) * 100
        returning_dictionary[currentValue] = percent

    return returning_dictionary


numbers = [3, 1, 2, 3, 4, 2]
print(distribution_analysis(numbers))