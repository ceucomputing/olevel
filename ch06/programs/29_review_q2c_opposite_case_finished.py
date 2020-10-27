# Returns True if s has alphabetical letters only
def is_letters_only(s):
    for c in s:
        if not c.isalpha():
            return False
    return True 

# Converts single letter to opposite case
def convert_letter(l):
    if l.islower():
        return l.upper()
    return l.lower()

# Converts string of letters to opposite case
def convert_string(s):
    result = ''
    for c in s:
        result = result + convert_letter(c)
    return result

while True:
    s = input('Enter string: ')
    if is_letters_only(s):
        break
    print('String must have alphabetical letters only')

print(convert_string(s))
