# This program extract the hours, minutes and seconds values (as ints)
# from a “time string” that is provided in the format “HH:MM:SS”.
# It is assumed that input data will always be valid.

# Variable declarations
# time    : str (Input string)
# hours   : int (Hours value)
# minutes : int (Minutes value)
# seconds : int (Seconds value)

# Input
time = input("Enter time string: ")

# Process
hours = int(time[:2])
minutes = int(time[3:5])
seconds = int(time[-2:])

# Output
print(hours)
print(minutes)
print(seconds)
