# Input
values = [16, 64, 4, 128, 8, 2, 1, 32]

# Process
if len(values) > 0:
    minimum_value = values[0]
    for value in values:
        if value < minimum_value:
            minimum_value = value
else:
    minimum_value = None

# Output
print(minimum_value)
