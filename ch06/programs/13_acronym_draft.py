# Input
input_text = input("Enter the input text: ")

# Process
acronym = ""
for index in range(len(input_text)):
    if input_text[index - 1].isspace():
        acronym += input_text[index]

# Output
print(acronym)
