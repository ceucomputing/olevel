words = ["Code", "Computing", "Future", "Cow", "Thinking"]
index = 0
while index < len(words):
    if words[index][0] != 'C':
        index = index + 1
        continue
    print("C is for " + words[index])
    index = index + 1
