# (a)
a = 0
while a < 10:
    a = a + 1
    print(a)

# (b)
x = 10
while x != 0:
    print(x)
    x = x - 1
print("Counting down ...")

# (c)
x = input("Enter a countdown number between 1 to 20. ")
x = int(x)
while x != 0:
    print(x)
    x = x - 1
print("Countdown completed!")
