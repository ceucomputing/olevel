import os   # For os.path.isfile()
import sys  # For sys.exit()

# Variable declarations
# titles       : list
# availability : list
# search       : str
# index        : int
# result       : str

# Input and input validation
if (not os.path.isfile("titles.txt")) or (
        not os.path.isfile("availability.txt")):
    print("Data validation failed!")
    print("Both titles.txt and availability.txt should exist")
    sys.exit()
titles = open("titles.txt").read().splitlines()
availability = open("availability.txt").read().splitlines()
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
