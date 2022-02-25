Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
###Assignment 6 Issue 4###
# Revision number BEGIN/ 02/25/22
## Begin Hussein El Sibai
##Read a value from the user
x = "25"
y = "4"
z = int(x) * int(y)
z
100
a = 4.35
b = 5.67
a = "4.35"
b = "5.67"
c = float(a) * float(b)
c
24.664499999999997
string1 = "Hussein"
int1 = 29
prin = str(string1,int1)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    prin = str(string1,int1)
TypeError: str() argument 'encoding' must be str, not int
prin = str(string1 + int1)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    prin = str(string1 + int1)
TypeError: can only concatenate str (not "int") to str
print(str(string1,int1))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(str(string1,int1))
TypeError: str() argument 'encoding' must be str, not int
w = str(29)
print(str(string1,w))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(str(string1,w))
TypeError: decoding str is not supported
print(string1,w)
Hussein 29
num1 = int(input("Enter a number1:"))
Enter a number1:12
num2 = int(input("Enter a number2:"))
Enter a number2:10
results = num1 * num2
print("The product of",num1,"and",num2,"is",results)
The product of 12 and 10 is 120
txt = "Hussein El Sibai Homework"
f = txt.find("Homework")
print(f)
17
# Revision number 1/ 02/25/22
## End Hussein El Sibai
# Zion Worship Cult/ Ram Vuduku/ Rich Eissen/ project # the Zion Project


