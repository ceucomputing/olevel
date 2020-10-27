text = input("Enter text: ")
if text == "":
    print("Blank Input Not Allowed")
else:
    if text == "P@55w0rd":
        print("Yes")
        print("Correct Password")
    else:
        print("No")
        print("Wrong Password")
print("Goodbye")
