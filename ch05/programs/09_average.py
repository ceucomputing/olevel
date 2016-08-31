# Variable declarations
# values     : list
# sum_values : float
# average    : float

# Input
values = [16, 64, 4, 128, 8, 2, 1, 32]

# Process
if len(values) > 0:
    sum_values = 0
    for value in values:
        sum_values += value
    average = sum_values / len(values)
else:
    average = None

# Output
print(average)
