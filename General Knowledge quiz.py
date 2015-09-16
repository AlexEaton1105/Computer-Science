# date: 16/09/15
# username: Alex
# name: Alex Eaton
# description: Python gneral knowledge quiz

import time    #imports the time module which allows for a pause inbetween printing

score = 0    #defines the user's score before starting

name = input("What is your name?")

print("Welcome to The Quiz, ",name,"\nWe'll be asking a series of general knowledge questions, \nplease answer all questions in lower case.")    #introduces the user to the quiz on two seperate lines
time.sleep(1)    #stops the program for one second

print("Question 1:\nWhich country features a maple leaf on its flag? ")
time.sleep(1)
print("A: Japan")
time.sleep(1)
print("B: Canada")
time.sleep(1)
print("C: France")
time.sleep(1)
answerOne = input("Make your choice: ")
if answerOne == "canada" or answerOne == "b":
    print("Well done! You scored a point! ")
    time.sleep(1)
    score = score + 1
else:
    print("Unlucky! You didnt score ")
    time.sleep(1)

answerTwo = input("Question 2:\nWhich planet did Superman come from?")
time.sleep(1)
if answerTwo == "krypton":
     print("Well done! You scored a point! ")
     time.sleep(1)
     score = score + 1
else:
    print("Unlucky! You didnt score")
    time.sleep(1)

answerThree = input("Question 3:How many syllables make up a haiku? ")
time.sleep(1)
if answerThree == "five" or answerThree == "5":
     print("Well done! You scored a point! ")
     time.sleep(1)
     score = score + 1
else:
    print("Unlucky! You didnt score")
    time.sleep(1)

answerFour = input("Question4:\nWhen was IRN BRU first produced? ")
time.sleep(1)
if answerFour == "1901":
     print("Well done! You scored a point!")
     time.sleep(1)
     score = score + 1
else:
    print("Unlucky! You didnt score")
    time.sleep(1)

answerFive = input("Question 5:\nWhat is the Capital of Turkey? ")
time.sleep(1)
if answerFour == "ankara":
     print("Correct! You scored a point!")
     time.sleep(1)
     score = score + 1
else:
    print("Unlucky! You didnt score")
    time.sleep(1)

print("Question6:\nWho created facebook? ")
 	time.sleep(1)
 	print("A: Mark Zuckerberg")
 	time.sleep(1)
 	print("B: Steve Jobs")
 	time.sleep(1)
 	print("C: Bill Gates")
 	time.sleep(1)
 	answerSix = input("Make your choice: ")
 	if answerSix == "A" or answerSix == "mark zuckerberg" :
    print ("Well done! You scored a point! ")
    time.sleep(1)
    score = score + 1
else:
    print("Unlucky! You didnt score")
    time.sleep(1) 

print("Thats all the questions! your total score was...,")
time.sleep(2)
print(score,"!!!\nAMAZING!")



                 


