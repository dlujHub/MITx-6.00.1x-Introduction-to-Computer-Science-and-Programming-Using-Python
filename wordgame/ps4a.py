import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    total_score = 0
    for c in word:
        curr_score = SCRABBLE_LETTER_VALUES.get(c)
        total_score += curr_score
    total_score *= len(word)
    if len(word) == n:
        total_score += 50
    return total_score


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")  # print all on the same line
    print()  # print an empty line


def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    numVowels = n // 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updated_hand = hand.copy()

    for letter in word:
        if updated_hand.get(letter) == 1:
            del updated_hand[letter]
        else:
            updated_hand[letter] = updated_hand.get(letter) - 1
    return updated_hand


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand_copy = hand.copy()
    for letter in word:
        if letter in hand_copy and hand_copy[letter] > 0:
            hand_copy[letter] = hand_copy.get(letter) - 1
        else:
            return False
    if word in wordList:
        return True
    return False


def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    sum = 0
    for letter in hand:
        sum += hand.get(letter)
    return sum


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """

    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while len(hand) > 0:
        # Display the hand
        print("Current Hand:  ", end="")
        display_hand(hand)
        # Ask user for input
        word = str(input("Enter word, or a \".\" to indicate that you are finished: "))
        # If the input is a single period:
        if word == '.':
            # End the game (break out of the loop)
            print("Goodbye! ", end="")
            break
        # Otherwise (the input is not a single period):
        #  If the word is not valid:
        if not isValidWord(word, hand, wordList):
            # Reject invalid word (print a message followed by a blank line)
            print("Invalid word, please try again.")
        else:  # Otherwise (the word is valid):
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a
            # blank line
            curr_score = get_word_score(word, n)
            total_score += curr_score
            print("\" %s \" earned %i points. Total: %i points" % (word, curr_score, total_score))
            # Update the hand
            hand = updateHand(hand, word)
        if len(hand) == 0:
            print("\nRun out of letters. ", end="")
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score

    print("Total score: %i points.\n" % total_score, end="")


#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    command = str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
    hand = {}
    word = random.choice(wordList)
    while command != 'e':
        if command == 'n':
            word = random.choice(wordList)
            hand = get_frequency_dict(word)
            playHand(hand, wordList, HAND_SIZE)
        elif command == 'r':
            if len(hand) == 0:
                print("You have not played a hand yet. Please play a new hand first!")
            else:
                playHand(hand, wordList, HAND_SIZE)
        else:
            print("Invalid command.")
        command = str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))


if __name__ == '__main__':
    wordList = load_words()
    playGame(wordList)
