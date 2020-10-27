# Input
values = [16, 64, 4, 128, 8, 2, 1, 32]

# Process
if len(values) > 0:
    maximum_value = values[0]
    for value in values:
        if value > maximum_value:
            maximum_value = value
else:
    maximum_value = None

# Output
print(maximum_value)
