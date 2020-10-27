# Input and input validation
while True:
    time = input("Enter time: ")
    if len(time) == 5:
        hours = time[:2]
        minutes = time[-2:]
        if time[2] == ":" and hours.isdigit() and minutes.isdigit():
            break
    print("Data validation failed!")
    print("Time should be in HH:MM format")

# Process
hours = int(hours)
if hours < 5:
    greeting = "Good Night"
elif hours < 12:
    greeting = "Good Morning"
elif hours < 18:
    greeting = "Good Afternoon"
elif hours < 22:
    greeting = "Good Evening"
else:
    greeting = "Good Night"

# Output
print(greeting)
