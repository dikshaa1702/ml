# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:41:38 2019

@author: DiPu
"""
import random
words=['apple','banana','orange','papaya','grapes','pomengranate','watermelon']
while True:
    ip=input("enter letter or q to quit:")
    if ip.lower()=='q':
        break
    guess=random.choice(words)
    bad_guesses=[]
    good_guesses=[]
    while len(bad_guesses)<7 and len(good_guesses)!=len(list(guess)):
        ip1= input ("Guess a letter : ").lower()
        if  len(ip1) != 1:
            print ("You can only guess a single letter !") 
            continue
        elif ip1 in bad_guesses or guess in good_guesses:
            print("You have already guess that letter")
            continue
        elif not ip1.isalpha():
            print ("You can only guess letters !")
            continue
        if ip1 in guess:
            good_guesses.append(ip1)
        if len(good_guesses) == len ( list(ip1)):
            print ("You win : The word was ",guess)
            break
        else:
            bad_guesses.append(ip1)
    
    else:
        print ("You didn't guess it: my secret word was {}". format(guess))


    

