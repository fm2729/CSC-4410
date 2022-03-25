Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
###Assignment 9 Issue 3###
# Revision number BEGIN/ 03/23/22
## Begin Hussein El Sibai
##Read a value from the user
def gcd(a,b):
        #getting the remainder of a and b
        rem = a % b
        #checking if remainder is 0 then GCD is b
        if (rem == 0):
                #returns b
                return b
        #if remainder is not 0 again calling gcd function
        else:
                return gcd(b,rem)

gcd(12,8)
4
gcd(20,24)
4
## The print statement should go in the sphere_volume function ##
# Revision number 1/ 03/23/22
## End Hussein El Sibai
# HALF-LIFE/ Ron Bass/ John Richards Sr./ project # After-Burner Elite
