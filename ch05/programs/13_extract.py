# Input
original = input("Enter a string of characters: ")

# Process
extract = ""
for character in original:
    # In this example, str.isalnum() is used for test()
    if character.isalnum():
        extract += character

# Output
print(extract)
