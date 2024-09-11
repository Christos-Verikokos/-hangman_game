# Include necessary methods and libraries
import random
import string
from pathlib import Path
import json

# Read and load files that contains hangman paints and list of available words
path_ascii = Path('/Users/macbook/Documents/python projects/pcc doc/code_pieces/hangman/hangman_ascii.json')
list_ascii_hang = json.loads(path_ascii.read_text())
path_words = Path('/Users/macbook/Documents/python projects/pcc doc/code_pieces/hangman/words_list')
contents_words = path_words.read_text().split()

# Define a function that it print corresponding life level
def hangman_paint(stage):
    temp = list_ascii_hang['hangman_stages'][stage]['drawing']
    for line in temp:
            print(line)

lives = 6
available_letters = list(string.ascii_lowercase)
word = random.choice(contents_words)
placeholder = list(word.replace(word, '_' * len(word)))

# Main 
while '_' in placeholder and lives != 0:   
    hangman_paint(lives)
    print(f"\n({' '.join(placeholder)})")
    print(f"Available letters: {' '.join(available_letters).upper()}")
    
    # Check whether given letter includes in word.
    while True:
        given_letter = input("Guess a letter:").lower()
        if given_letter not in available_letters:
            print("This letter have typed or is invalid . Select another form available letters that showed.") 
        else:
            available_letters.remove(given_letter) 
            break

    if given_letter in word:
        count = 0
        for letter in word:
            if letter == given_letter.lower():
                placeholder[count] = letter    
            count += 1
    else:
        lives -= 1

#Final check condition.
if lives == 0:
    hangman_paint(lives)
    print("GAME OVER!")
elif '_' not in placeholder:
    print(f"YOU WIN!\nThe word is: {word.upper()}")