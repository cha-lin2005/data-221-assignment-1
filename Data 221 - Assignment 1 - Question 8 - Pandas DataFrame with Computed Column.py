# Question 8: install pandas package and import using the alias pd. create dataframe using provided column data, add new
# column from existing columns, print final data frame.

import pandas as pd

provided_data = {
    "A" : [1, 2, 2, 1],
    "B" : [3.1, 4.2, 1.5, 6.3],
    "C" : [88, 150, 400, 210]
}

data_frame = pd.DataFrame(provided_data)

data_frame ["D"] = data_frame ["A"] + data_frame["B"]

print(data_frame)