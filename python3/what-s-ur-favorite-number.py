#-*- coding:utf-8 -*-
#this is code by python, not python3
#2019.3.7   I write this for two hours......
#homework for 6.00.1x week 2 lecture 3 problem 9
l = 0
r = 99
mid = 50
print 'Please think of a number between 0 and 100!'
print 'Is your secret number ' + str(mid) + '?'
guess = raw_input("Enter 'h' to indicate the guess is too high. \
    Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

while guess != 'c':
    if guess != 'h' and guess != 'l':
        print 'Sorry, I did not understand your input.\n'
        print 'Is your secret number ' + str(mid) + '?\n'
        guess = raw_input("Enter 'h' to indicate the guess is too high. \
    Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    elif guess == 'h':
        r = mid
        mid = int((l + r) / 2)
        print 'Is your secret number ' + str(mid) + '?'
        guess = raw_input("Enter 'h' to indicate the guess is too high. \
    Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    elif guess == 'l':
        l = mid
        mid = int((l + r) / 2)
        print 'Is your secret number ' + str(mid) + '?'
        guess = raw_input("Enter 'h' to indicate the guess is too high. \
    Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

print 'Game over. Your secret number was: ' + str(mid)

