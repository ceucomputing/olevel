# Input
titles = [
    # The following data is copied from the given text file.
    "How to Solve a Mystery", "Vacant Memories", 
    "The Cybersnake Chronicles", "Music History", 
    "Like Tears in Rain", "Out of the Abyss"
]
availability = [
    # The following data is copied from the given text file.
    "Not Available", "Available", "Available", "Not Available",
    "Not Available", "Available"
]
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
