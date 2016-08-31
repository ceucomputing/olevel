# Variable declarations
# values     : list
# input_str  : str
# sum_values : float
# index      : int
# average    : float

# Input
values = []
while True:
    input_str = input("Enter integer, blank to end: ")
    if input_str == "":
        break
    values += [int(input_str)]

# Process
if len(values) > 0:
    sum_values = 0
    index = 0
    while index < len(values):
        sum_values += values[index]
        index += 1
    average = sum_values / len(values)
else:
    average = None

# Output
print(average)
