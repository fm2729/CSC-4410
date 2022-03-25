Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
###Assignment 9 Issue 2###
# Revision number BEGIN/ 03/23/22
## Begin Hussein El Sibai
##Read a value from the user
def print_range(start,end):
    if start==end:
        print(start)
    else:
        if start<end:
            print(start)
            print_range(start+1,end)
        else:
            print(end)
            print_range(start,end+1)

start=int(input("Enter starting number: "))
end=int(input("Enter ending number: "))
print_range(start,end)
SyntaxError: invalid syntax
def print_range(start,end):
    if start == end:
        print(start)
    else:
        if start < end:
            print(start)
            print_range(start + 1,end)
        else:
            print(end)
            print_range(start,end+1)

            
start = int(input("Enter starting number: "))
Enter starting number: 5
end = int(input("Enter ending number: "))
Enter ending number: 10
print_range(start,end)
5
6
7
8
9
10
## The print statement should go in the sphere_volume function ##
# Revision number 1/ 03/23/22
## End Hussein El Sibai
# HALF-LIFE/ Ron Bass/ John Richards Sr./ project # After-Burner Elite
