import random

WORDLIST_FILENAME = "words.txt"
#----------------------------------------------------------
#First block
def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)


#-----------------------------------------------------------
def isWordGuessed(secretWord, lettersGuessed):
    a = 0
    for i in secretWord:
        for j in lettersGuessed:
            if i == j:
                a += 1
                break
    return a == len(secretWord)
#-----------------------------------------------------------

def getGuessedWord(secretWord, lettersGuessed):
    a = ""
    for i in secretWord:
        isin = False
        for j in lettersGuessed:
            if i == j:
                a = a + i
                isin = True
                break
        if isin == False:
            a += "_ "

    return a


def getAvailableLetters(lettersGuessed):
    global strings
    strings = "abcdefghijklmnopqrstuvwxyz"
    strings_new = ''
    for i in strings:
        switcher = False
        for j in lettersGuessed:
            if i == j:
                switcher = True
                break
        if switcher == False:
            strings_new += i
    return strings_new


def hangman(isWordGuessed, getGuessedWord, getAvailableLetters, secretWord, lettersGuessed, guesses):
    if guesses > 0:
        print("You have " + str(guesses) + " guesses left.")
        print("Available Letters: " + getAvailableLetters(lettersGuessed))
        newGues = input("Please guess a letter: ")
        if newGues.lower() in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
            return hangman(isWordGuessed, getGuessedWord, getAvailableLetters, secretWord, lettersGuessed, guesses)
        else:
            lettersGuessed = lettersGuessed + newGues.lower()

        if isWordGuessed(secretWord, lettersGuessed):
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
            if getGuessedWord(secretWord, lettersGuessed) == secretWord:
                return print("Congratulations, you won!")
            return hangman(isWordGuessed, getGuessedWord, getAvailableLetters, secretWord, lettersGuessed, guesses)
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
            return hangman(isWordGuessed, getGuessedWord, getAvailableLetters, secretWord, lettersGuessed, guesses - 1)
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord +".")

    return print(getGuessedWord(secretWord, lettersGuessed));

lettersGuessed, guesses = "", 8
secretWord = "ohlo" #chooseWord(wordlist) #secret word
print("Welcome to the game, Hangman!")
print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
print("-------------")
hangman(isWordGuessed, getGuessedWord, getAvailableLetters, secretWord, lettersGuessed, guesses)
