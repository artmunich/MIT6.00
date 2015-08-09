# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------

#---------------------------------------------
lower_cases = string.ascii_lowercase
upper_cases = string.ascii_uppercase

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    For punctuation and digits, just ignore them.
    """
    assert type(shift) == int and shift >= 0 and shift <= 26
    cipher_cases = {}
    turn = 26 - shift
    for i in range(0,turn):
        cipher_cases[lower_cases[i]] = lower_cases[i+shift]
        cipher_cases[upper_cases[i]] = upper_cases[i+shift]
        
    for i in range(turn,26):
        cipher_cases[lower_cases[i]] = lower_cases[i+shift-26]
        cipher_cases[upper_cases[i]] = upper_cases[i+shift-26]
    
    return cipher_cases

def applyCoder(text,coder):
    """
    Apply coder to the text and return encoded text.
    """
    puncs = string.punctuation
    digits = string.digits
    
    ignore = puncs + digits
    
    encoded_text = ''
    
    for char in text:
        if coder.__contains__(char):
            encoded_text += coder[char]
        else:
            encoded_text += char
    return encoded_text
    
def applyShift(text,shift):
    """
    Given a text, returns a new text Ceasar shifted by the given shift offset.
    """
    return applyCoder(text,buildCoder(shift))
    
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    match_number = {}
    for i in range(26):
        text_decrypt = applyShift(text,26-i)
        words = text_decrypt.split(' ')
        cnt = 0
        for word in words:
            if wordList.__contains__(word):
                cnt += 1
        match_number[i] = cnt
    most = 0
    for i in match_number.iterkeys():
        if match_number[i] > most:
            best_shift = match_number[i]
    return best_shift
    
    
    
    
    
    
    
    
    
    
    
    
    
    
