# Variable declarations
# values        : list
# minimum_value : float

# Input
values = [16, 64, 4, 128, 8, 2, 1, 32]

# Process
if len(values) > 0:
    minimum_value = min(values)
else:
    minimum_value = None

# Output
print(minimum_value)
