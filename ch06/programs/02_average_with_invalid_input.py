# Input
values = ["16", "64", "4", "128", "8", "2", "1", "32"]

# Process
if len(values) > 0:
    sum_values = sum(values)
    average = sum_values / len(values)
else:
    average = None

# Output
print(average)
