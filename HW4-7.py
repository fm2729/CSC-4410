Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
###Assignment 4 Issue 7###
# Revision number BEGIN/ 02/09/21
## Begin Hussein El Sibai
lst=["Ben","Roger","Barak Obama"]
location="Charger Union"
time="Friday,January 28th at 8pm"
for i in range(len(lst)):
print(lst[i]+", you're invited to dinner at "+location+" on "+time)
SyntaxError: expected an indented block after 'for' statement on line 1
for i in range(len(lst)):
    print(lst[i]+", you're invited to dinner at "+location+" on "+time)

    
Traceback (most recent call last):
  File "<pyshell#4>", line 2, in <module>
    print(lst[i]+", you're invited to dinner at "+location+" on "+time)
NameError: name 'location' is not defined
lst = ["Ben","Roger","Barak Obama"]
location = "Charger Union"
time = "Friday,January 28th at 8pm"
for i in range(len(lst)):
    print(lst[i]+", you're invited to dinner at "+location+" on "+time)

    
Traceback (most recent call last):
  File "<pyshell#7>", line 2, in <module>
    print(lst[i]+", you're invited to dinner at "+location+" on "+time)
NameError: name 'location' is not defined
for i in range(len(lst)):
    print(lst[i],", you're invited to dinner at ",location," on ",time)

    
Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    print(lst[i],", you're invited to dinner at ",location," on ",time)
NameError: name 'location' is not defined
lst = ["John","Jacob","Joe Biden"]
location = "Charger Union"
time = "Friday, January 26th at 8pm"
for i in range(len(lst)):
    print(lst[i],", you're invited to dinner at ",location," on ",time)

    
John , you're invited to dinner at  Charger Union  on  Friday, January 26th at 8pm
Jacob , you're invited to dinner at  Charger Union  on  Friday, January 26th at 8pm
Joe Biden , you're invited to dinner at  Charger Union  on  Friday, January 26th at 8pm
del lst[1]
lst.append("Giovanni")
print("Giovanni",", you're invited to dinner at ",location," on ",time)
Giovanni , you're invited to dinner at  Charger Union  on  Friday, January 26th at 8pm
lst.insert(0,"Dr. Doom")
print("Dr. Doom",", you're invited to dinner at ",location," on ",time)
Dr. Doom , you're invited to dinner at  Charger Union  on  Friday, January 26th at 8pm
lst.insert(len(lst)//2,"Peter")
lst.append("James")
print("Peter",", you're invited to dinner at ",location," on ",time)
Peter , you're invited to dinner at  Charger Union  on  Friday, January 26th at 8pm
print("James",", you're invited to dinner at ",location," on ",time)
James , you're invited to dinner at  Charger Union  on  Friday, January 26th at 8pm
for i in range(2):
    x = lst.pop()

    
print("I'm sorry ",x,", But you can't come to my house for dinner")
I'm sorry  Giovanni , But you can't come to my house for dinner
lst = sorted(lst)
for i in range(len(lst)):
    print(lst[i],", you're invited to dinner at ",location," on ",time)

    
Dr. Doom , you're invited to dinner at  Charger Union  on  Friday, January 26th at 8pm
Joe Biden , you're invited to dinner at  Charger Union  on  Friday, January 26th at 8pm
John , you're invited to dinner at  Charger Union  on  Friday, January 26th at 8pm
Peter , you're invited to dinner at  Charger Union  on  Friday, January 26th at 8pm
# Revision number 2/ 02/09/21
## End Hussein El Sibai
# Omega Group/ Ram Valud/ Michael Walker/ project # greenwood321