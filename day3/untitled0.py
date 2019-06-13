# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:42:04 2019

@author: DiPu
"""

import random 

# make a list if word
words = ['apple','banana','orange','coconut','strawberry','lime','grapefruit','lemon','kumquat','blueberry','melon']

while True:

    start = input("Press enter / return to start, or enter Q to quit:")

    if start.lower() == 'q':
        break

# pick a random word
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len (list( secret_word)):
        # draw  spaces
        # draw guessed letters, spaces and strikes
        for letter in secret_word:
            if letter in good_guesses:
                print ( letter , end='')
            else:
                print('_', end='')
                print ('')

        print('Strikes : {} / 7'.format(len(bad_guesses)))
        print ('')

        # take guess
        guess = input ("Guess a letter : ").lower()

        # draw guessed letters and strikes
        if  len(guess) != 1:
            print ("You can only guess a single letter !") 
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You have already guess that letter")
            continue
        elif not guess.isalpha():
            print ("You can only guess letters !")
            continue
        # print out win / lose

        if guess in secret_word:
            good_guesses.append(guess)

        if len (good_guesses) == len ( list(secret_word)):
            print ("You win : The word was {}". format(secret_word))
            break
        else:
            bad_guesses.append(guess)
    
    else:   # else for the while 
        print ("You didn't guess it: my secret word was {}". format(secret_word))



"""
Challenge 2
    Screen is messy and rolls ups
    Convert the code into function 

    MAJOR REFACTORING OF THE CODE
"""

import os
import random 
import sys

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def draw(bad_guesses, good_guesses, secret_word):
    clear()
    print('Strikes : {} / 7'.format(len(bad_guesses)))

    print ('')

    for letter in bad_guesses :
        print(letter, end = ' ')
        print("\n\n")

    for letter in secret_word:
        if letter in good_guesses:
            print ( letter , end='')
        else:
            print('_', end='')
            print ('')


def get_guess(bad_guesses,good_guesses):
    while True:
        # take guess
        guess = input ("Guess a letter : ").lower()
        # draw guessed letters and strikes
        if  len(guess) != 1:
            print ("You can only guess a single letter ") 
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You have already guess that letter")
            continue
        elif not guess.isalpha():
            print ("You can only guess letters !")
            continue
        else:
            return guess