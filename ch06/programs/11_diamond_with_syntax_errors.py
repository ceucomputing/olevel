# Variable declarations
# input_text : str
# n          : int
# index      : int

# Input and input validation
while True:
    input_text = input("Enter n: ")
    if input_text.isdigit()
        n = int(input_text)
        if n >= 1 and n <= 19 and n % 2 == 1:
            break
        else:
            print("Data validation failed!")
            print("n should be odd and between 1 and 19 inclusive")
    else:
        print("Data validation failed!')
        print("n should be a positive integer")

# Process and output
for index in range(n // 2):
    print(' ' * (n // 2 - index) + '*' * (2 * index + 1))
for index in range(n // 2 + 1):
    print(' ' * index + '*' * (n - index * 2)))
