# Input
values = ["Alex", "Bala", "Siti", "Zee"]
search = input("Enter name: ")

# Process
search_index = None
for index in range(len(values)):
    if values[index] == search:
        search_index = index
        break

# Output
print(search_index)
