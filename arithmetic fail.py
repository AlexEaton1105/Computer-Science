import random
import time

counter = 0
score = 0
numberOne = 0
numberTwo = 0
operator = 0

def add(x, y):
  return x + y;

def subtract (x, y):
  return x - y;

def multiply (x, y):
  return x * y;

name = input("What is your name?  ")
print("Welcome to the quiz, ",name,)

for counter in range(0,10):
    counter = counter + 1
    numberOne = random.randint(1,10)
    numberTwo = random.randint(1,10)
    operator = random.randint(1,3)

    if operator == 1:
      print("Question ",counter,"What is ",numberOne, "+", numberTwo)
      ans = add(numberOne, numberTwo)
    elif operator == 2:
      print("Question ",counter,"What is ",numberOne, "-",numberTwo)
      ans = subtract(numberOne, numberTwo)
    else:
      print("Question ",counter,"What is ",numberOne, "*",numberTwo)
      ans = multiply(numberOne, numberTwo)

    res = int(input("Please write answer here: "))

    if res == ans:
      print("Well done, ",name,"! 1 point scored.")
      time.sleep(1)
      score = score + 1
    else:
      print("Unlucky, ",name,". No points scored.")

print("That's it! the quiz is over. Your overall score was: ",score,"Well done!")
#now you need to make it so that if they got less than 5, you tell them to improve,  less than 7 they could try harder and more they have done very well.
#do this by replacing this comment with an if, elif and else

if score <= 4:
    print("That's it! the quiz is over. Your overall score was: ",score,"Better luck next time!!")
elif score <= 7:
    print("That's it! the quiz is over. Your overall score was: ",score," Good try!")
else:
    print ("That's it! the quiz is over. Your overall score was: ",score," Well done!")
