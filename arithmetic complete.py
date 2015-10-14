import random #this imports the random module which allows for random numbers to be generated.
import time #this imports the random odule which allows for pauses in the code.

counter = 0 #this defines the counter, which counts to 10 after each question asked.
score = 0 #this defines the score and tells them how many questions they've got right.
numberOne = 0 #this is the variable for the first number in each question.
numberTwo = 0 #this is the variable for the first second in each question.
operator = 0 #this is the variable thst stores the number to be assigned to the operator in each question.

def add(x, y): #this defines the add variable.
  return x + y; #tells the computer what to do when the subtract variable is called

def subtract (x, y): #this defines the subtract varible.
  return x - y; #tells the computer what to do when the subtract variable is called

def multiply (x, y): #this defines the multiply variable.
  return x * y; #tells the computer what to do when the subtract variable is called

name = input("PLese tell me your name ") #asks for users name so it can be used elsewhere in the code.
whichClass = input("and also are you in class one, class two or class three?) #asks the user for their class number.
if whichClass == "class one" or whichClass == "1" or whichClass =="Class One":
  classOne = open("classOne.txt","a")
elif whichClass == "class two" or whichClass == "2" or whichClass == "Class Two":
  classTwo = open("classTwo.txt","a")
else:
  classThree = open("classThree.txt","a")   

print("Welcome to the quiz, ",name,) #welcomes the user to the quiz, this makes the experience more personal for the user.

for counter in range(0,10): #when the variable is in range of 1 to 10 it runs all the indented code.
    counter = counter + 1
    numberOne = random.randint(1,10) #randomly generates a number to be used in the question.
    numberTwo = random.randint(1,10) #randomly generates a number to be used in the question.
    operator = random.randint(1,3)   #randomly generates a number to be used in the question.

  if operator == 1: #when the random operator is 1 it runs the indented code.
    print("Question ",counter,"What is ",numberOne, "+", numberTwo) #prints the question using the add variable.
    ans = add(numberOne, numberTwo) #defines the question to be compared to the users input.
  elif operator == 2: #when the random operator is 2 it runs the indented code.
    print("Question ",counter,"What is ",numberOne, "-",numberTwo) #prints the question using the subtract variable.
     ans = subtract(numberOne, numberTwo) #defines the question to be compared to the users input.
  else: #when the random operator is 3 it runs the indented code.
    print("Question ",counter,"What is ",numberOne, "*",numberTwo) #prints the question using the multiply variable.
    ans = multiply(numberOne, numberTwo) #defines the question to be compared to the users input.

      res = int(input("Please write answer here: ")) #this is where the user enters their answer so the code can check if it's the right answer.
  if res == ans: #when the result is the same as the answer, the indented code runs
    print("Well done, ",name,"! 1 point scored.") #prints a well done message to the user.
    time.sleep(1) #pauses the code for 1 second.
    score = score + 1 #adds one to the score variable
  else: #when the result isn't the same as the answer, the indented code runs.
    print("Unlucky, ",name,". No points scored.") #prints an unlucky message ot the user.

#make it so that if they got less than 4, you tell them to improve,  less than 7 they could try harder and more they have done very well.
#do this by replacing this comment with an if, elif and else

if score <= 4: #if the score is less than 4 the indented code runs.
    print("That's it! the quiz is over. Your overall score was: ",score,"Better luck next time!!") #ends the program telling the user's final score.
elif score <= 7: #if the score is less than 7 the indented code runs.
    print("That's it! the quiz is over. Your overall score was: ",score," Good try!") #ends the program telling the user's final score.
else: #if the score is different to the other variables the indented code runs.
    print ("That's it! the quiz is over. Your overall score was: ",score," Well done!") #ends the program telling the user's final score.
time.sleep(1)
file.write("\n"name,":",score)
print("Your score has been saved to your class' file.")
time.sleep(1)
