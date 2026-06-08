# math

# math
import math

math.sqrt(196)
# keywords
# keyword
import keyword
print(keyword.kwlist)
# random
# random
import random
print(random.randint(1,100))
# datetime
# datetime
import datetime
print(datetime.datetime.now())


help('modules')

# While loop example -> program to print the table
# Program -> Sum of all digits of a given number
# Program -> keep accepting numbers from users till he/she enters a 0 and then find the avg


number = int(input('enter the number'))

i = 1

while i<11:
  print(number,'*',i,'=',number * i)
  i += 1


  # while loop with else

x = 1

while x < 3:
  print(x)
  x += 1

else:
  print('limit crossed')


  # Guessing game

# generate a random integer between 1 and 100
import random
jackpot = random.randint(1,100)

guess = int(input('guess karo'))
counter = 1
while guess != jackpot:
  if guess < jackpot:
    print('galat!guess higher')
  else:
    print('galat!guess lower')

  guess = int(input('guess karo'))
  counter += 1

else:
  print('correct guess')
  print('attempts',counter)

  # For loop demo

for i in {1,2,3,4,5}:
  print(i)

#   Program - The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years.

curr_pop = 10000

for i in range(10,0,-1):
  print(i,curr_pop)
  curr_pop = curr_pop - 0.1*curr_pop

