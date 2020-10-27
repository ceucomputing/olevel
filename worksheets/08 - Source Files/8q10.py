# This program calculates the hypotenuse of a right-angled triangle
import math
base = float(input("Enter base of right-angled triangle: "))
height = float(input("Enter height of right-angled triangle: "))
hypo = math.sqrt((base**2) + (height**2))
print("The hypotenuse of the triangle is: " + str(hypo))
