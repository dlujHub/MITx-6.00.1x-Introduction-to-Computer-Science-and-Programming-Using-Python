# Hangman game

import random
import string

WORDLIST_FILENAME = "words"


def load_words():
    """
    Returns a list of valid words (lowercase letters).

    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    for c in secret_word:
        if c not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    """
    guessed_so_far = ""
    for c in secret_word:
        if c in letters_guessed:
            guessed_so_far += c
        else:
            guessed_so_far += " _ "
    return guessed_so_far


def get_available_letters(letters_guessed):
    """
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    available = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available += letter
    return available


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

      Rules:
    * At the start of the game, let the user know how many
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    """
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is %i letters long." % len(secret_word))
    print("-------------")

    letters_guessed = []
    nr_of_guesses = 8
    mistakes_made = 0

    while True:
        print("You have %i guesses left." % (nr_of_guesses - mistakes_made))
        available_letters = get_available_letters(letters_guessed)
        print("Available letters:", available_letters)
        guessed = str(input("Please guess a letter: "))
        guessed.lower()

        if len(guessed) == 1 and guessed in string.ascii_lowercase:
            if guessed in letters_guessed:
                print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))

            elif guessed not in secret_word:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                mistakes_made += 1
                letters_guessed.append(guessed)
                if mistakes_made > 8:
                    print("-------------")
                    print("Sorry, you ran out of guesses. The word was else.")
                    return
            else:
                letters_guessed.append(guessed)
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                if is_word_guessed(secret_word, letters_guessed):
                    print("-------------")
                    print("Congratulations, you won!")
                    break

        print("-------------")
        if mistakes_made == 8:
            print("Sorry, you ran out of guesses. The word was else. ")
            break


secret_word = choose_word(wordlist).lower()
hangman(secret_word)
