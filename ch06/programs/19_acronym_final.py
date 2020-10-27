# Gets input text from the user
def get_text():
    while True:
        input_text = input("Enter the input text: ")
        input_is_valid = True
        for c in input_text:
            if not (c.isalpha() or c.isspace()):
                print("Data validation failed!")
                print("Input text should only contain " +
                    "letters and spaces")
                input_is_valid = False
                break
        if input_is_valid:
            return input_text

# Returns whether text[i] should be included in the acronym
def should_include(text, i):
    return (text[i - 1].isspace() or i == 0) and not text[i].isspace()

# Input
input_text = get_text()

# Process
acronym = ""
for index in range(len(input_text)):
    if should_include(input_text, index):
        acronym += input_text[index]
acronym = acronym.upper()

# Output
print(acronym)
