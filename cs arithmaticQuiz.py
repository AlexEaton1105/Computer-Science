import random
import time

counter = 1
score = 0
numberOne = 0
numberTwo = 0
operator = 0

while operator <10 :
    numberOne = random.randint(1,10)
    # etc for other number
    operator = rand.randint(1,3)

#operator now needs to be split into an if, elif and else
#so the idea is that if operator = 1, it provides a +, 2 makes it a - and 3 makes it a *
#the idea then is that you make the "result" var to equal numberOne, operator and numberTwo
#you then compare the result var to an answer var you have gained from the user and go through the motions
#at that point you want to screenshot it and start all over again using a list for the operator
