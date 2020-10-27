# Input
input_text = input("Enter input text: ")

# Process
word_list = input_text.split()

for i in range(len(word_list)):
    current_word = ""
    for letter_index in range(len(word_list[i])):
        current_word += word_list[i][-letter_index - 1]
    word_list[i] = current_word

result = ""
for word in word_list:
    result += word + " "
result = result[:-1]

# Output
print(result)
