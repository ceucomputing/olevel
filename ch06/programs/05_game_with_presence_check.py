import random  # For random.randint()

# List of possible secret words
WORDS = ['add', 'bug', 'cat', 'dog', 'eye', 'for', 'sky', 'zip']

# Choose a random secret word
random_index = random.randint(0, len(WORDS) - 1)
secret_word = WORDS[random_index]

# Main loop to keep repeating until secret word is guessed
while True:

    # Input and input validation
    while True:
        guess = input("Enter guess of length 3: ")
        if guess != '':
            break
        print("Data validation failed!")
        print("Guess is required and must not be left blank")

    # Process and output
    if guess == secret_word:
        print('Correct')
        break                  # Exit main loop here 
    print('Wrong')
