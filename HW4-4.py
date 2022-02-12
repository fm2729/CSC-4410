Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
###Assignment 4 Issue 4###
# Revision number BEGIN/ 02/09/21
## Begin Hussein El Sibai
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('a'))
SyntaxError: invalid syntax

================================ RESTART: Shell ================================
def vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels

print(vowel('a'))
True
print(vowel('b'))
False
print(vowel('c'))
False
print(vowel('d'))
False
print(vowel('e'))
True
# Revision number 2/ 02/09/21
## End Hussein El Sibai
# Omega Group/ Ram Valud/ Michael Walker/ project # greenwood321