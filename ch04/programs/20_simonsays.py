# Constants
MAGIC_WORDS = "Simon says "
QUIT_COMMAND = "Quit"

print("Enter \"" + QUIT_COMMAND + "\" to end game.")
while True:
    command = input("Enter command: ")
    if command == QUIT_COMMAND:
        break
    elif command[:len(MAGIC_WORDS)] != MAGIC_WORDS:
        print("We ignore the command")
        continue
    print("We " + command[len(MAGIC_WORDS):])
print("Thanks for playing!")
