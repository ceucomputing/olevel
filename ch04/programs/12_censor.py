# Variable declarations
# name : str

name = input("Enter name: ")
if "Evil" in name:
    name = "*** CENSORED ***"
print("You are " + name)
