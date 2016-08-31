# Variable declarations
# length        : int
# values        : list
# i             : int
# value         : float
# sum_values    : float
# num_positive  : int
# average       : float

# Input
length = int(input("Enter length: "))
values = []
for i in range(length):
    value = float(input("Enter item: "))
    values += [value]

# Process
if len(values) > 0:
    sum_values = 0
    num_positive = 0
    for value in values:
        if value > 0:
            sum_values += value
            num_positive += 1
    average = round(sum_values / num_positive, 2)
else:
    average = None

# Output
print(average)
