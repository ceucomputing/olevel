# Program that generates 3 random register numbers

import random
counter = 0

total = int(input("Enter number of students in your class: "))

while counter < 3:
    register_num = random.randint(1, total)
    print("Register number", counter + 1, "is:", register_num)
    counter += 1
