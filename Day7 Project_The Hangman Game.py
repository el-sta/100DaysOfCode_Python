import random
from hangman_words import word_list
from hangman_art import stages, logo


#  Create a variable called 'lives' to keep track of the number of lives left.

lives= 6

print(logo)
chosen_word = random.choice(word_list)

#Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""

for letter in chosen_word:
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    # Tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    #  If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

#Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

    display=""

    for letter in chosen_word:
        if letter==guess:
            display+= letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display+="_"

    print("Word to guess: " + display)

    #  If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        #  If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
        #  If lives goes down to 0 then the game should stop and it should print "You lose."
        if lives==0:
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
            game_over=True

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    #  print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    for i in range(7):
        if lives==i:
            print(stages[i])
