# Gets input text from the user
def get_text():
    return input("Enter the input text: ")

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
