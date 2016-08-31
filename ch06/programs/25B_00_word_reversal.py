# Variable declarations
# input_text   : str
# word_list    : list
# current_word : str
# index        : int
# letter_index : int
# result       : str

# Input
input_text = input("Enter input text: ")

# Process
word_list = []
current_word = ""
index = 0
while index < len(input_text):
    if not input_text[index].isspace():
        current_word += input_text[index]
    else:
        if current_word != "":
            word_list += [current_word]
            current_word = ""
    index += 1
if current_word != "":
    word_list += [current_word]

index = 0
while index < len(word_list):
    current_word = ""
    letter_index = 0
    while letter_index < len(word_list[index]):
        current_word += word_list[index][-letter_index - 1]
        letter_index += 1
    word_list[index] = current_word
    index += 1

result = ""
index = 0
while index < len(word_list):
    result += word_list[index] + " "
    index += 1
result = result[:-1]

# Output
print(result)
