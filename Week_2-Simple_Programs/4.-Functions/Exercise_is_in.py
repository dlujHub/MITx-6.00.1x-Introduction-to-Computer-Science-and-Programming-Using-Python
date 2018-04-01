# Exercise: is in

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 18 minutes

# We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical
# order. First, test the middle character of a string against the character you're looking for (the "test character"). If they are the
# same, we are done - we've found the character we're looking for!
# If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower
# half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's
# < function.)

# Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single
# character and aStr will be a string that is in alphabetical order. The function should return a boolean value.

# As you design the function, think very carefully about what the base cases should be.


def isIn(char, aStr):
    # Base case: If aStr is empty, we did not find the char.
    if aStr == '':
        return False

    # Base case: if aStr is of length 1, just see if the chars are equal
    if len(aStr) == 1:
        return aStr == char

    # Base case: See if the character in the middle of aStr equals the
    #   test character
    midIndex = len(aStr)//2
    midChar = aStr[midIndex]
    if char == midChar:
        # We found the character!
        return True

    # Recursive case: If the test character is smaller than the middle
    #  character, recursively search on the first half of aStr
    elif char < midChar:
        return isIn(char, aStr[:midIndex])

    # Otherwise the test character is larger than the middle character,
    #  so recursively search on the last half of aStr
    else:
        return isIn(char, aStr[midIndex+1:])
