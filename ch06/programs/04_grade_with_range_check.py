# Variable declarations
# score : int
# grade : str

# Input and input validation
score = None
while score == None:
    score = int(input("Enter score: "))
    if score < 0 or score > 100:
        print("Data validation failed!")
        print("Your score should be between 0 to 100 inclusive")
        score = None

# Process
if score >= 75:
    grade = "A1"
elif score >= 70:
    grade = "A2"
elif score >= 65:
    grade = "B3"
elif score >= 60:
    grade = "B4"
elif score >= 55:
    grade = "C5"
elif score >= 50:
    grade = "C6"
elif score >= 45:
    grade = "D7"
elif score >= 40:
    grade = "E8"
else:
    grade = "F9"

# Output
print(grade)
