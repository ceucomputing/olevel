sides = int(input("Enter number of regular polygon sides (3 to 8): "))
while sides < 3 or sides > 8:
    sides = int(input("Enter number of regular polygon sides (3 to 8): "))

if sides == 3:
    print("This is a triangle.")
elif sides == 4:
    print("This is a square.")
elif sides == 5:
    print("This is a pentagon.")
elif sides == 6:
    print("This is a hexagon.")
elif sides == 7:
    print("This is a heptagon.")
else:
    print("This is an octagon.")
