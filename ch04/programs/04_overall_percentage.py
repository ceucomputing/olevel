# This program calculates the overall percentage score of a
# class with three students.

# Constants
MAX_SCORE = 80      # Maximum possible score
CLASS_SIZE = 3      # Number of students in the class

# Variable declarations
# score_1 : int     (Score of first student)
# score_2 : int     (Score of second student)
# score_3 : int     (Score of third student)
# total   : int     (Total score of class)
# result  : float   (Overall percentage score)

# Input
score_1 = 65
score_2 = 75
score_3 = 70

# Process
total = score_1 + score_2 + score_3
result = total / (CLASS_SIZE * MAX_SCORE) * 100

# Output
print(result)
