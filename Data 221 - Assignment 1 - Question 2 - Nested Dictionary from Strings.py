def function_that_receives_list_of_strings_and_returns_nested_dictionary(list_of_strings):
    nested_dictionary_containing_length_and_parity = {}

    for single_string in list_of_strings:
        length_of_each_string = len(single_string)

        if length_of_each_string % 2 == 0:
            parity_of_single_string = "even"
        else:
            parity_of_single_string = "odd"

        nested_dictionary_containing_length_and_parity[single_string] = {
            "length": length_of_each_string,
            "parity": parity_of_single_string
        }

    return nested_dictionary_containing_length_and_parity


print(function_that_receives_list_of_strings_and_returns_nested_dictionary(['data', 'science']))
