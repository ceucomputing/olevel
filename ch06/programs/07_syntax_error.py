# Input
values = []
while True:
    input_str = input("Enter integer, blank to end: ")
    if input_str = "":
        break
    values += [int(input_str)]

# Process
if len(values) > 0:
    sum_values = sum(values)
    average = sum_values / len(values)
else:
    average = None

# Output
print(average)
