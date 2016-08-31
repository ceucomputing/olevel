# Variable declarations
# input_text    : str
# acronym       : str
# index         : int
# previous_char : str
# current_char  : str

# Input
input_text = input("Enter the input text: ")

# Process
acronym = ""
index = 0
previous_char = ' '
while index < len(input_text):
    current_char = input_text[index]
    if previous_char.isspace() and not current_char.isspace():
        acronym += current_char.upper()
    index += 1
    previous_char = current_char

# Output
print(acronym)
