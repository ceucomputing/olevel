# Variable declarations
# input_str : str
# result    : list

# Input and Process
result = []
while True:
    input_str = input("Enter item, blank to end: ")
    if input_str == "":
        break
    result += [input_str]

# Output
print(result)
