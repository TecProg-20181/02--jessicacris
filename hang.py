# -*- coding: utf-8 -*-

import random
import string

WORDLIST_FILENAME = "palavras.txt"

class Hangman():
    def hangman_man(self, guesses):

        if guesses == 8:
			print "________      "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
        elif guesses == 7:
            print "________      "
            print "|      |      "
            print "|             "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 6:
            print "________      "
            print "|      |      "
            print "|           "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 5:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 4:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|      |      "
            print "|             "
            print "|             "
        elif guesses == 3:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|     /|      "
            print "|             "
            print "|             "
        elif guesses == 2:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|     /|\     "
            print "|             "
            print "|             "
        elif guesses == 1:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|     /|\     "
            print "|     /       "
            print "|             "
        else:
            print "________      "
            print "|      |      "
            print "|     \õ/     "
            print "|      |      "
            print "|     / \     "
            print "|             "


def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'read', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def isWordGuessed(secretWord, letters_guessed):
    secret_Letters = []

    for letter in secretWord:
        if letter in letters_guessed:
            pass
        else:
            return False

    return True

def get_available_letters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

def count_letters(secretWord):

    letters = []

    for letter in secretWord:
        if letter not in letters:
            letters.append(letter)

    return len(letters)

def validatedWord (secretWord, guesses):
    maximum_tries = 20
    tries = 0
    validated_Word = False

    while not validated_Word:
        unique_letters = count_letters(secretWord)
        print 'There are', unique_letters, 'unique Letters in this word'

        if guesses < unique_letters:
            print 'The secret Word have too many unique letters, reloading the letters'
            secretWord = loadWords()
            tries += 1
            if tries >= maximum_tries:
                print'Maximum of tries, exiting program'
                return None
        else:
            validated_Word = True
    return secretWord

def number_of_words(secretWord, letters_guessed):
    guessed = ''
    for letter in secretWord:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += '_ '

def hangman(secretWord):
    guesses = 8
    secretWord = validatedWord(secretWord, guesses)

    if secretWord == None:
        return

    letters_guessed = []

    hangman = Hangman()

    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

    while  isWordGuessed(secretWord, letters_guessed) == False and guesses >= 0:
        print 'You have ', guesses, 'guesses left.'

        hangman.hangman_man(guesses)

        if guesses == 0:
            return

        available = get_available_letters()
        for letter in available:
            if letter in letters_guessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in letters_guessed:
            guessed = ''
            guessed = number_of_words(secretWord, letters_guessed)

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            letters_guessed.append(letter)

            guessed = ''
            guessed = number_of_words(secretWord, letters_guessed)

            print 'Good Guess: ', guessed
        else:
            guesses -=1
            letters_guessed.append(letter)

            guessed = ''
            guessed = number_of_words(secretWord, letters_guessed)

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if isWordGuessed(secretWord, letters_guessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'




secretWord = loadWords().lower()
hangman(secretWord)
