from random import randint

# Generates a number from 1 through 6 inclusive
random_number = randint(1, 6)

guesses_left = 3
# Start your game!
while guesses_left > 0 and guesses_left <= 6:
    guess = int(input("Your guess: (1-6)"))
    guesses_left -= 1
    # trying to set boundaries for the input for it to not be a string, an int > 6, or an int < 0.
    if guess > 6 or guess < 0:
        input("Enter a number between 1 and 6 nibba. Try again: ")
    elif guess == random_number:
        print ("U dead nibba")
        break
    print("You've got %s guesses left nibba" %guesses_left) #can also use:("you've got ", guesses_left, "guesses left /
    # nibba")
else:
    print ("U safe nibba")
