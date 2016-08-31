# Variable declarations
# values        : list
# maximum_value : float
# maximum_index : int
# index         : int

# Input
values = [16, 64, 4, 128, 8, 2, 1, 32]

# Process
if len(values) > 0:
    maximum_value = values[0]
    maximum_index = 0
    for index in range(len(values)):
        if values[index] > maximum_value:
            maximum_value = values[index]
            maximum_index = index
else:
    maximum_value = None
    maximum_index = None

# Output
print(maximum_value)
print(maximum_index)
