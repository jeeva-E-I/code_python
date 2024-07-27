import random
import hangman_words
import hangman_arts

                 
print(hangman_arts.logo)
chosen_word = random.choice(hangman_words.word_list)
display = []
for item in range(0, len(chosen_word)):
    display.append("_")
lives = 6

while "_" in display:
    guess = input("Enter a letter:").lower()
    if guess in display:
        print("You have already entered the letter")
        guess = input("Enter different letter:").lower()
    for letter in chosen_word:
        if letter == guess:
            index = chosen_word.index(letter)
            display[index] = guess
            print(display)
        
    if "_" not in display:
        print("YOU WON")
    else:
        print(hangman_arts.stages[lives])
        print("You have entered the wrong text")
        lives -= 1
        print(f"{lives} chances are left")
    if lives == 0:
            print(hangman_arts.stages[lives])
            print("YOU LOST")
            break
        