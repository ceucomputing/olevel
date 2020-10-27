def good_example(num1, num2):   # num1 and num2 are local
    return num1 + num2          # OK

def bad_example():              # num1 and num2 are global
    return num1 + num2          # Don't do this!

num1 = 19
num2 = 65
print(good_example(20, 17))
print(bad_example())
