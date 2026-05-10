import random
from nltk.corpus import words
def main():
    print("Welcome to Hangman!")
    word_list=words.words()
    filtered_word_list=[word.lower() for word in word_list if word.isalpha() and 6<= len(word) <=9]
    word=random.choice(filtered_word_list)
    guess=6
    print(f'lives: {guess}')
    result=['_']*len(word)
    print("".join(result))
    incorrect_letters=[]
    correct_letters=[]
    hangman = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /   |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]
    print(hangman[0])
    while(guess>0):
        letter=input("Guess a letter:").lower()
        if not letter.isalpha():
            print('Invalid input!')
            continue 
        if letter in word:
            for i,ch in enumerate(word):
                if ch==letter:
                    result[i]=letter
                    correct_letters.append(letter)
        else:
            print('Wrong letter!')
            guess-=1
            print(f'lives: {guess}')
            print(hangman[6-guess])
            incorrect_letters.append(letter)
        print("".join(result))
        print(f'Incorrect letters: {', '.join(incorrect_letters)}')
        print(f'Correct letters: {", ".join(correct_letters)}')
        if '_' not in result:
            print('You win!')
            break
    else:
        print('You lost!')
        print(f'The word was {word}')
if __name__=='__main__':
    main()