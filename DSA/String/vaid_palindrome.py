'''
Problem : A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
'''
#Approach
'''
1. Initate two pointers :
    - left : Pointing at zeroth index
    - right : Pointing at last index
2. Increment left or decrement right by one index if character pointed is not alphanumeric
3. Check if s[left]==s[right].

Time Complexity : O(n)
Space Complexity : O(1)
'''

#Code
def isPalindrome(s):
    left = 0
    right = len(s)-1
    while left <= right :
        if not s[left].isalnum():
            left+=1
            continue
        if not s[right].isalnum():
            right-=1
            continue
        if s[right].lower()!=s[left].lower():
            return False
        left+=1
        right-=1
    return True

str=input("Enter String : ")
print(isPalindrome(str))