"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    #return false if 2 divides the number
    if x % 2 == 0:
        return False

    #return false if the input is not an integer
    elif type(x) != int:
        return False

    #return true if not either of these two things
    else:
        return True


def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    isPalindrome = True

    #Ran a while loop that breaks whenever two matched characters aren't the same
    while isPalindrome:
        for index, letter in enumerate(word):
            #constantly reading at opposite ends of the string
            if word[index] == word[-(index+1)]:
                continue

            #In case the input isn't a string
            elif type(word) != str:
                isPalindrome = False
                break

            #If the two characters aren't the same
            else:
                isPalindrome = False
                break


        if isPalindrome:
            break

    #returns the final boolean value
    return isPalindrome

def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    #Initialised an empty list
    numbers = []

    #Looped through list of numbers and appended only if current number was odd
    for i, num in enumerate(numlist):
        if (num % 2 != 0):
            numbers.append(numlist[i])
    return numbers

def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    #Initialised an empty dictionary to count words
    wordCount = {}

    #Made all words lowercase
    text = text.lower()

    #Ran a loop through the string to update the dictionary when it hits whitespace
    word = ""
    for letter in text:

        #Write to word if the character isn't writespace
        if (letter != " " and letter.isalnum()):
            word = word + letter

        #End the writing and add a count for the word that was just written
        else:
            #Create new dictionary item if it's not already in it
            if word in wordCount:
                wordCount[word] += 1
                word = ""
            else:
                wordCount[word] = 1
                word = ""
    return wordCount


#Wrote some rudimentary unit tests to see if the functions worked
print(is_odd(5))
print(is_palindrome("racecar"))
print(count_words("How much wood would a woodchuck chuck"
                " if a woodchuck could chuck wood?"))
print(only_odds([1, 2, 3, 4, 5, 6, 7]))
