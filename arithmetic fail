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

for cunter in range(0,20):
    counter = counter + 1
    numberOne = random.randint(0,20)
    numberTwo = random.randint(0,20)
    operator = random.randint(0,4)

    if operator == 1:
        print("Question ",counter,"What is ",numberOne, "+", numberTwo,)
        ans = add(numberOne, numberTwo)
    elif operator == 2:
              print("Question ",counter,"What is ",numberOne, "-",numberTwo,)                                          
              ans = subtract(numberOne, numberTwo)

    res = int(input("Please write answer here: "))

    if res == ans:
        print("Well done, ",name,"! 1 point scored.")
        time.sleep(1)

