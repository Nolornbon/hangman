# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    
    for i in secret_word:
      if i not in letters_guessed:
        return False
    return True



def get_guessed_word(secret_word, letters_guessed):
     
    res = ''

    for i in secret_word:
        if i in letters_guessed:
            res += i
        else: res += '_ '
    return res



def get_available_letters(letters_guessed):
    
    res = ''
    for i in string.ascii_lowercase:
      if i not in letters_guessed:
        res += i
    return res
    
    

def hangman(secret_word):
  letters_guessed = []
  guesses_left = 6
  warnings = 3
  print("Hangman")
  print("Word length:", len(secret_word))
  print("___________________")  
  while is_word_guessed(secret_word,letters_guessed) == False and guesses_left != 0:
    print("Progress:",get_guessed_word(secret_word,letters_guessed))
    print("Guesses left:", guesses_left)
    print("Available letters", {get_available_letters(letters_guessed)})
    print("_" * 20)
    print("Choose letter from available")
    while 1:
      letter = str(input("Your letter:")).lower()
      if len(letter) == 1:
        break
      else:
        warnings -= 1
        if warnings == 0:
          guesses_left -= 1
          print("-1 attempt")
        continue
    
    else:
      if letter in secret_word:
        print('The letter is in the word')
      else:
        print("\nThe letter isn't in the word")
        guesses_left = guesses_left - 2 if letter in ['a','e','i','o','u'] else guesses_left - 1
        letters_guessed += letter
  if guesses_left == 0:
    print("You lost. Secret word was:", secret_word)
  else:
    print("You won. Secret word was:", secret_word)

# -----------------------------------

def match_with_gaps(my_word, other_word):
  my_word = my_word.replace("" "", "")
  if len(my_word) != len(other_word):
    return False
  else:  
    for i in range(len(my_word)):
      if my_word[i] != "_": result = result and (my_word[i] == other_word[i])
  return result  
    


def show_possible_matches(my_word):
  matches = ""
  for word in wordlist: 
    if match_with_gaps(my_word, word): 
      matches += " "
      matches += word    
  if matches == "":  
    print("No matches")
  else: 
    print("Possible word matches: "+ matches)





# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
  print("_" * 20) 
  secret_word = choose_word(wordlist)
  print("_" * 20)
 
    
  secret_word = choose_word(wordlist)
  hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
