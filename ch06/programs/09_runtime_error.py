# Input
values = []
while True:
    input_str = input("Enter integer, blank to end: ")
    if input_str == "":
        break
    values += [int(input_str)]

# Process
sum_values = sum(values)
average = sum_values / len(values)

# Output
print(average)
