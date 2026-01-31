# Question 7 : write a function that converts given number of seconds since midnight to hours, minutes, seconds,
# and am pm, returning formatted string, and if invalid input.

def time_converter(number_of_seconds_before_midnight):
    if (
        not isinstance(number_of_seconds_before_midnight, int)
        or number_of_seconds_before_midnight < 0
        or number_of_seconds_before_midnight > 86399
    ):
        return "Invalid time: Seconds should be a positive integer from 0 to 86399"

    hours_in_a_day = number_of_seconds_before_midnight // 3600
    remaining_seconds_in_a_day = number_of_seconds_before_midnight % 3600

    minutes_in_a_day = remaining_seconds_in_a_day // 60
    remaining_seconds_in_a_day = remaining_seconds_in_a_day % 60

    if hours_in_a_day < 12:
        time_period = "AM"
    else:
        time_period = "PM"

    displayed_hours = hours_in_a_day % 12
    if displayed_hours == 0:
        displayed_hours = 12

    return f"{displayed_hours} {minutes_in_a_day} {remaining_seconds_in_a_day} {time_period}"


print(time_converter(52789))
print(time_converter(12456))