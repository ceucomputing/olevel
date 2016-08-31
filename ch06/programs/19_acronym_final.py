# Variable declarations
# input_text     : str
# acronym        : str
# index          : int
# input_is_valid : bool

# Input and input validation
input_is_valid = False
while not input_is_valid:
    input_text = input("Enter the input text: ")
    input_is_valid = True
    for c in input_text:
        if not (c.isalpha() or c.isspace()):
            print("Data validation failed!")
            print("Input text should only contain letters and spaces")
            input_is_valid = False
            break

# Process
acronym = ""
index = 0
while index < len(input_text):
    if (input_text[index - 1].isspace() or index == 0) and (
            not input_text[index].isspace()):
        acronym += input_text[index]
    index += 1
acronym = acronym.upper()

# Output
print(acronym)
