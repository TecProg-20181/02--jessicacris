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
            print "|      ~      "
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


def load_Words():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def is_Word_Guessed(secret_Word, letters_Guessed):
    secret_Letters = []

#    for letter in secretWord:
#        if letter in secretLetters:
#            secretLetters.append(letter)
#        else:
#            pass

    for letter in secret_Word:
        if letter in letters_Guessed:
            pass
        else:
            return False

    return True

def get_Guessed_Word():

     guessed = ''


     return guessed

def get_Available_Letters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

def hangman(secret_Word):

    guesses = 8
    letters_Guessed = []
    
    hangman = Hangman()

    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secret_Word), ' letters long.'
    print '-------------'

    while  is_Word_Guessed(secret_Word, letters_Guessed) == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        hangman.hangman_man(guesses)

        available = get_Available_Letters()
        for letter in available:
            if letter in letters_Guessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in letters_Guessed:

            guessed = get_Guessed_Word()
            for letter in secret_Word:
                if letter in letters_Guessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secret_Word:
            letters_Guessed.append(letter)

            guessed = get_Guessed_Word()
            for letter in secret_Word:
                if letter in letters_Guessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Good Guess: ', guessed
        else:
            guesses -=1
            letters_Guessed.append(letter)

            guessed = get_Guessed_Word()
            for letter in secret_Word:
                if letter in letters_Guessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if is_Word_Guessed(secret_Word, letters_Guessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secret_Word, '.'




secret_Word = load_Words().lower()
hangman(secret_Word)
