# Problem 4 - The Game

# (15/15 points)
# Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an
# interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions,
# isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

# Hints:
# You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a
# random one. Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. When
# you enter in your solution in the tutor, you only need to give your hangman function.

# Consider using lower() to convert user input to lower case. For example:
# guess = 'A'
# guessInLowerCase = guess.lower()
# Consider writing additional helper functions if you need them!

# There are four important pieces of information you may wish to store:
# secretWord: The word to guess.
# lettersGuessed: The letters that have been guessed so far.
# mistakesMade: The number of incorrect guesses made so far.
# availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed
# from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've
# already guessed that - so try again!).

# Note that if you choose to use the helper functions isWordGuessed, getGuessedWord, or getAvailableLetters, you do not need to
# paste your definitions in the box. We have supplied our implementations of these functions for your use in this part of the
# problem. If you use additional helper functions, you will need to paste those definitions here.

# Your function should include calls to input to get the user's guess.


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


def hangman(letters_guessed):
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

# Correct
