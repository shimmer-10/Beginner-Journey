#Palindrome Number
'''
Problem : Given an integer x, return true if x is a palindrome, and false otherwise.
'''
#Code
def isPalindrome(x):
    if x < 0 or (x!=0 and x%10==0):
        return False
    rev = 0
    while x > rev :
        rev = rev*10 + x%10
        x//=10
    return x == rev or x == rev//10

num = int(input("Enter number :"))
print(isPalindrome(num))