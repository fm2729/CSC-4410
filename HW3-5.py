Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
###Assignment 3 Issue 5###
# Revision number BEGIN/ 02/04/21
## Begin Hussein El Sibai
######### WELCOME TO AHOY MATEY TREASURE CHEST GAME ##########
import random
array = [0]
count = 10 # total treasure chest money
high = 50
low = 1

for i in range(count):
    array.append(random.randint(low,high)) # Generating random numbers and adding it to array.

    
position = random.randint(1,10) # Generating random number between 1,10
array[position] = -1  # assign -1
money = 0 # total money
chances = 0 # total chances

print("Game has started. Enter a value from 1 to 10 to open a treasure chest for each attempt. You have 10 chests to open. If you open a treasure chest with -1 then you lose the game and your money.If you open 10 chests with money you get to keep it!")
Game has started. Enter a value from 1 to 10 to open a treasure chest for each attempt. You have 10 chests to open. If you open a treasure chest with -1 then you lose the game and your money.If you open 10 chests with money you get to keep it!
winFlag = True
while (chances < 10):
     treasure_position = int(input("Enter a chest number from 1 to 10:"))
     if not(treasure_position >= 1 and treasure_position <= 15): # checking the user input
          continue
        if (array[treasure_position] > 0):
            
SyntaxError: unindent does not match any outer indentation level
while (chances < 10):
    treasure_position = int(input("Enter a chest number from 1 to 10:"))
    if not(treasure_position >= 1 and treasure_position <= 15): # checking the user input
        continue
    if (array[treasure_position] > 0):
         money += array[treasure_position]
         print(f"You just opened a chest with {array[treasure_position]} dollars!")
     elif(array[treasure_position] == -1):
         
SyntaxError: unindent does not match any outer indentation level
while (chances < 10):
    treasure_position = int(input("Enter a chest number from 1 to 10:"))
    if not(treasure_position >= 1 and treasure_position <= 15): # checking the user input
        continue
    if (array[treasure_position] > 0):
        money += array[treasure_position]
        print(f"You just opened a chest with {array[treasure_position]} dollars!")
    elif(array[treasure_position] == -1):
        print("Oops! you lost the game :(")
        winFlag = False
        break
     chances += 1
     
SyntaxError: unindent does not match any outer indentation level
while (chances < 10):
    treasure_position = int(input("Enter a chest number from 1 to 10:"))
    if not(treasure_position >= 1 and treasure_position <= 15): # checking the user input
        continue
    if (array[treasure_position] > 0):
        money += array[treasure_position]
        print(f"You just opened a chest with {array[treasure_position]} dollars!")
    elif(array[treasure_position] == -1):
        print("Oops! you lost the game :(")
        winFlag = False
        break
    chances += 1

    
Enter a chest number from 1 to 10:1
You just opened a chest with 25 dollars!
Enter a chest number from 1 to 10:2
You just opened a chest with 25 dollars!
Enter a chest number from 1 to 10:3
You just opened a chest with 28 dollars!
Enter a chest number from 1 to 10:4
You just opened a chest with 40 dollars!
Enter a chest number from 1 to 10:5
You just opened a chest with 15 dollars!
Enter a chest number from 1 to 10:6
You just opened a chest with 12 dollars!
Enter a chest number from 1 to 10:7
You just opened a chest with 43 dollars!
Enter a chest number from 1 to 10:8
You just opened a chest with 30 dollars!
Enter a chest number from 1 to 10:9
You just opened a chest with 27 dollars!
Enter a chest number from 1 to 10:10
Oops! you lost the game :(
while (chances < 10):
    treasure_position = int(input("Enter a chest number from 1 to 10:"))
    if not(treasure_position >= 1 and treasure_position <= 15): # checking the user input
        continue
    if (array[treasure_position] > 0):
        money += array[treasure_position]
        print(f"You just opened a chest with {array[treasure_position]} dollars!")
    elif(array[treasure_position] == -1):
        print("Oops! you lost the game :(")
        winFlag = False
        break
    chances += 1
if (winFlag == True):
    
SyntaxError: invalid syntax
while (chances < 10):
    treasure_position = int(input("Enter a chest number from 1 to 10:"))
    if not(treasure_position >= 1 and treasure_position <= 15): # checking the user input
        continue
    if (array[treasure_position] > 0):
        money += array[treasure_position]
        print(f"You just opened a chest with {array[treasure_position]} dollars!")
    elif(array[treasure_position] == -1):
        print("Oops! you lost the game :(")
        winFlag = False
        break

Enter a chest number from 1 to 10:1
You just opened a chest with 25 dollars!
Enter a chest number from 1 to 10:2
You just opened a chest with 25 dollars!
Enter a chest number from 1 to 10:
Traceback (most recent call last):3
  File "<pyshell#59>", line 2, in <module>
    treasure_position = int(input("Enter a chest number from 1 to 10:"))
ValueError: invalid literal for int() with base 10: ''
while (chances < 10):
    treasure_position = int(input("Enter a chest number from 1 to 10:"))
    if not(treasure_position >= 1 and treasure_position <= 15): # checking the user input
        continue
    if (array[treasure_position] > 0):
        money += array[treasure_position]
        print(f"You just opened a chest with {array[treasure_position]} dollars!")
    elif(array[treasure_position] == -1):
        print("Oops! you lost the game :(")
        winFlag = False
        break
if (winFlag == True):
    
SyntaxError: invalid syntax
while (chances < 10):
    treasure_position = int(input("Enter a chest number from 1 to 10:"))
    if not(treasure_position >= 1 and treasure_position <= 15): # checking the user input
        continue
    if (array[treasure_position] > 0):
        money += array[treasure_position]
        print(f"You just opened a chest with {array[treasure_position]} dollars!")
    elif(array[treasure_position] == -1):
        print("Oops! you lost the game :(")
        winFlag = False
        break
    if (winFlag == True):
        print(f"You won {money} dollars!")

        
Enter a chest number from 1 to 10:1
You just opened a chest with 25 dollars!
Enter a chest number from 1 to 10:2
You just opened a chest with 25 dollars!
Enter a chest number from 1 to 10:3
You just opened a chest with 28 dollars!
Enter a chest number from 1 to 10:4
You just opened a chest with 40 dollars!
Enter a chest number from 1 to 10:5
You just opened a chest with 15 dollars!
Enter a chest number from 1 to 10:6
You just opened a chest with 12 dollars!
Enter a chest number from 1 to 10:7
You just opened a chest with 43 dollars!
Enter a chest number from 1 to 10:8
You just opened a chest with 30 dollars!
Enter a chest number from 1 to 10:9
You just opened a chest with 27 dollars!
Enter a chest number from 1 to 10:10
Oops! you lost the game :(
# Revision number 1/ 02/04/21
## End Hussein El Sibai
# Omega Group/ Ram Valud/ Michael Walker/ project # greenwood321