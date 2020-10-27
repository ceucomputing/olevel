# Solution 2: Use of iteration loops

count_neg = 0
count_zero = 0
count_pos = 0

for i in range(10):
    x = int(input("Enter an integer: "))
    if x < 0:
        count_neg = count_neg + 1
    elif x == 0:
        count_zero = count_zero + 1
    else:
        count_pos = count_pos + 1

print("The total number of negative integers are: " + str(count_neg))
print("The total number of zeroes are: " + str(count_zero))
print("The total number of positive integers are: " + str(count_pos))
