# This program checks the availability of a book using its title.

# Variable declarations
# titles       : list
# availability : list
# search       : str
# index        : int
# result       : str

# Input
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
