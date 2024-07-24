import hangmanwordlist
import hangmanart
import random


# Select a random word
choice_word = random.choice(hangmanwordlist.words)
word_len = len(choice_word)

# Generate list of underscores
display = ["_"] * word_len
print(display)
lives=6
art = 0
# Game loop
game_end = False
incorrect_guesses = 0  # Track incorrect guesses (optional)

while not game_end:
    guess = input("Please guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
        
    # Check guess against chosen word
    found = False
    for index, letter in enumerate(choice_word):
        if letter == guess:
            display[index] = guess
            found = True

    if not found:
        print("incorrect, you lose a life")
        lives-=1
        art+=1
          # Update incorrect guesses (optional)
        if lives == 0:
            game_end = True 
            print("You lose")

    print(f"{' '.join(display)}")
    print(display)

    # Check for win condition
    if "_" not in display:
        game_end = True
        print("You Win!")

    print(hangmanart.arts[art]) 
