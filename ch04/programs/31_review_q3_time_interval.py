# This program calculates the number of seconds between a start time
# and an end time, both provided in the format "HH:MM:SS". It is
# assumed that input data will always be valid.

# Input
start_time = input("Enter start time string: ")
end_time = input("Enter end time string: ")

# Process
hours = int(start_time[:2])
minutes = int(start_time[3:5])
seconds = int(start_time[-2:])
start_total = hours * 60 * 60 + minutes * 60 + seconds

hours = int(end_time[:2])
minutes = int(end_time[3:5])
seconds = int(end_time[-2:])
end_total = hours * 60 * 60 + minutes * 60 + seconds

interval = end_total - start_total

# Output
print(interval)
