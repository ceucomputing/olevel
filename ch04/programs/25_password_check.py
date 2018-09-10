# Variable declarations
# password       : str
# password_again : list

# Input, Process and Output
while True:
    password = input("Enter password: ")
    password_again = input("Enter password again: ")
    if password == password_again:
        break
    print("Invalid")
print("Valid")
