# This program calculates body mass index

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))

bmi = weight/(height ** 2)
print("Your body mass index is {}.".format(bmi))
