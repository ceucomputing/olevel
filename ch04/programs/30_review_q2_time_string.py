# This program extracts the hour, minute and second values (as ints)
# from a time string that is provided in the format "HH:MM:SS".
# It is assumed that input data will always be valid.

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
