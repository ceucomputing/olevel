# Input
input_text = input("Enter the input text: ")

# Process
acronym = ""
previous_char = ' '
for char in input_text:
    if previous_char.isspace() and not char.isspace():
        acronym += char.upper()
    previous_char = char

# Output
print(acronym)
