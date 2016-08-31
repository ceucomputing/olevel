# Variable declarations
# isbn        : str
# check_sum   : int
# index       : int
# remainder   : int
# check_digit : int or str

# Input
isbn = input("Enter first 9 digits of ISBN: ")

# Process
check_sum = 0
for index in range(9):
    check_sum += (10 - index) * int(isbn[index])
remainder = check_sum % 11
if remainder == 0:
    check_digit = 0
else:
    check_digit = 11 - remainder
    if check_digit == 10:
        check_digit = "X"

# Output
print(check_digit)
