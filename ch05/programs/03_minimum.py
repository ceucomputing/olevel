# Variable declarations
# values        : list
# minimum_value : float
# minimum_index : int
# index         : int

# Input
values = [16, 64, 4, 128, 8, 2, 1, 32]

# Process
if len(values) > 0:
    minimum_value = values[0]
    minimum_index = 0
    for index in range(len(values)):
        if values[index] < minimum_value:
            minimum_value = values[index]
            minimum_index = index
else:
    minimum_value = None
    minimum_index = None

# Output
print(minimum_value)
print(minimum_index)
