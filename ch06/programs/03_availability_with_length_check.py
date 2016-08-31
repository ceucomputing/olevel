import sys  # For sys.exit()

# Variable declarations
# titles       : list
# availability : list
# search       : str
# index        : int
# result       : str

# Input and input validation
titles = open("titles.txt").read().splitlines()
availability = open("availability.txt").read().splitlines()
if len(titles) != len(availability):
    print("Data validation failed!")
    print("Input files should have the same number of lines")
    sys.exit()  # Quits immediately
search = input("Enter title of book to check: ")

# Process
result = "Book Not Found"
index = 0
while index < len(titles):
    if titles[index] == search:
        result = availability[index]
    index = index + 1

# Output
print(result)
