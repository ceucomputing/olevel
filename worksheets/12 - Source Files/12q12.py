menu = "*****Types of operation*****\n\
1. +\n\
2. -\n\
3. *\n\
4. /\n\
****************************\n"

print(menu)

op = int(input("Key in the number for operator (1 to 4): "))
num1 = int(input("Enter your first number? "))
num2 = int(input("Enter your second number? "))

if op == 1:
    print(num1 + num2)
elif op == 2:
    print(num1 - num2)
elif op == 3:
    print(num1 * num2)
elif op == 4:
    print(num1 / num2)
