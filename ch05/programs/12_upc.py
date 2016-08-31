# This program calculates the check digit of a Universal Product Code
# (UPC-A) based on the first 11 digits of the code.

# Variable declarations
# upc         : str
# odd_sum     : int
# even_sum    : int
# index       : int
# digit       : int
# check_digit : int

# Input
upc = input("Enter first 11 digits of UPC-A: ")

# Process
odd_sum = 0
even_sum = 0
for index in range(11):
    digit = int(upc[index])
    if (index + 1) % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
check_digit = (odd_sum * 3 + even_sum) % 10
if check_digit != 0:
    check_digit = 10 - check_digit

# Output
print(check_digit)
