import math

# Variable declarations
# input_txt     : list
# values        : list
# line          : str
# result        : str
# value         : float

# Input
input_txt = open("input.txt").read().splitlines()
values = []
for line in input_txt:
    if line == "":
        continue
    values += [int(line)]

# Process
result = "No"
for value in values:
    if int(math.sqrt(value))**2 == value:
        result = "Yes"
        break

# Output
print(result)
