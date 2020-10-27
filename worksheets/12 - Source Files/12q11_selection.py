# Solution 1: Use of selection

count_neg = 0
count_zero = 0
count_pos = 0

x1 = int(input("Enter an integer: "))
x2 = int(input("Enter an integer: "))
x3 = int(input("Enter an integer: "))
x4 = int(input("Enter an integer: "))
x5 = int(input("Enter an integer: "))
x6 = int(input("Enter an integer: "))
x7 = int(input("Enter an integer: "))
x8 = int(input("Enter an integer: "))
x9 = int(input("Enter an integer: "))
x10 = int(input("Enter an integer: "))

if x1 < 0:
    count_neg = count_neg + 1
elif x1 == 0:
    count_zero = count_zero + 1
else:
    count_pos = count_pos + 1

if x2 < 0:
    count_neg = count_neg + 1
elif x2 == 0:
    count_zero = count_zero + 1
else:
    count_pos = count_pos + 1

if x3 < 0:
    count_neg = count_neg + 1
elif x3 == 0:
    count_zero = count_zero + 1
else:
    count_pos = count_pos + 1

if x4 < 0:
    count_neg = count_neg + 1
elif x4 == 0:
    count_zero = count_zero + 1
else:
    count_pos = count_pos + 1

if x5 < 0:
    count_neg = count_neg + 1
elif x5 == 0:
    count_zero = count_zero + 1
else:
    count_pos = count_pos + 1

if x6 < 0:
    count_neg = count_neg + 1
elif x6 == 0:
    count_zero = count_zero + 1
else:
    count_pos = count_pos + 1

if x7 < 0:
    count_neg = count_neg + 1
elif x7 == 0:
    count_zero = count_zero + 1
else:
    count_pos = count_pos + 1

if x8 < 0:
    count_neg = count_neg + 1
elif x8 == 0:
    count_zero = count_zero + 1
else:
    count_pos = count_pos + 1

if x9 < 0:
    count_neg = count_neg + 1
elif x9 == 0:
    count_zero = count_zero + 1
else:
    count_pos = count_pos + 1

if x10 < 0:
    count_neg = count_neg + 1
elif x10 == 0:
    count_zero = count_zero + 1
else:
    count_pos = count_pos + 1

print("The total number of negative integers are: " + str(count_neg))
print("The total number of zeroes are: " + str(count_zero))
print("The total number of positive integers are: " + str(count_pos))
