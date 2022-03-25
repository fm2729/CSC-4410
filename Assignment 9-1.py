Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
###Assignment 9 Issue 1###
# Revision number BEGIN/ 03/23/22
## Begin Hussein El Sibai
##Read a value from the user
def sphere_volume(R):
    pi = 3.1415926535897931
    V = 4.0/3.0 * pi * R ** 3
    return print("The volume of the sphere is ",V)

def main():
    R = int(input("Enter radius: "))
    sphere_volume(R)

    
main()
Enter radius: 5
The volume of the sphere is  523.5987755982989
## The print statement should go in the sphere_volume function ##
# Revision number 1/ 03/23/22
## End Hussein El Sibai
# HALF-LIFE/ Ron Bass/ John Richards Sr./ project # After-Burner Elite
