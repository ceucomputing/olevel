# Input
length = int(input("Enter length: "))
values = []
for i in range(length):
    value = float(input("Enter item: "))
    values += [value]

# Process
average = None
sum_values = 0
num_positive = 0
for value in values:
    if value > 0:
        sum_values += value
        num_positive += 1
if num_positive > 0:
    average = round(sum_values / num_positive, 2)

# Output
print(average)
