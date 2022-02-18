Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
###Assignment 5 Issue 1###
# Revision number BEGIN/ 02/09/21
## Begin Hussein El Sibai
firstName = "hussein"
lastName = "EL SIBAI"
firstName = firstName.upper()
lastName = lastName.lower()
print("Hello,",firstName,lastName)
Hello, HUSSEIN el sibai
print()

print()

fullName = "Hussein El Sibai"
print(fullName[8:16])
El Sibai
print(fullName[8:16],"Walsh College Student")
El Sibai Walsh College Student
print("Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi")
Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi
print('"Start by doing what',"'","s necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi"')
      
SyntaxError: unterminated string literal (detected at line 1)
print('"Start y doing what',"'","s necessary; then do what","'",'s possible; and suddenly you are doing the impossible - Francis of Assisi"')
      
"Start y doing what ' s necessary; then do what ' s possible; and suddenly you are doing the impossible - Francis of Assisi"
num1 = 2.3
      
num2 = 3.5
      
add = num1 + num2
      
subtract = num1 - num2
      
multiply = num1 * num2
      
divide = num1/num2
      
print(num1,"plus",num2,"equals",add)
      
2.3 plus 3.5 equals 5.8
print(num1,"minus",num2,"equals"subtract)
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(num1,"minus",num2,"equals",subtract)
      
2.3 minus 3.5 equals -1.2000000000000002
print(num1,"multiply",num2,"equals",multiply)
      
2.3 multiply 3.5 equals 8.049999999999999
print(num1,"divide",num2,"equals",divide)
      
2.3 divide 3.5 equals 0.6571428571428571
import math
sq_root = math.sqrt(multiply)
print("{:.2f}".format(sq_root))
2.84
print("The square root of",multiply,"equals","{:.2f}".format(sq_root))
The square root of 8.049999999999999 equals 2.84
month = "February"
day = 17
print("Today is day",day,"day of the month of",month)
Today is day 17 day of the month of February
# Revision number 2/ 02/17/21
## End Hussein El Sibai
#The Omega-Cypress International Equity Division/ Ram Fujitsu/ Rich Alderman/ project # grant $370
