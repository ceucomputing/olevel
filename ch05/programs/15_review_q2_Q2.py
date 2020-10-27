# Input
values = []
while True:
    item = input("Enter item, blank to end: ")
    if item == "":
        break
    values += [int(item)]

# Process
if len(values) >= 2:
    # For the basic sub-problem, only consider the first
    # two items in values.
    if values[0] < values[1]:
        minimum_value = values[0]
        second_minimum_value = values[1]
    else:
        minimum_value = values[1]
        second_minimum_value = values[0]
    # Start considering beyond the first two items.
    for value in values[2:]:
        if value < minimum_value:
            # If there will be a new minimum value, the second
            # minimum value will be the old minimum value.
            second_minimum_value = minimum_value
            minimum_value = value
else:
    minimum_value = None
    second_minimum_value = None

# Output
if minimum_value == None:
    print("None")
else:
    print(minimum_value, second_minimum_value)
