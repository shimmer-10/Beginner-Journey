'''
Problem : Given a string s, return true if the s can be palindrome after deleting at most one character from it.
'''
#Approach
'''
1. Initiate two pointers :
    - l pointing at index 0
    - r pointing at last index
2. While l <= r:
   - If s[l] == s[r], move both pointers inward.
   - Otherwise, check whether either:
       - s[l+1:r+1] is a palindrome (delete left character), or
       - s[l:r] is a palindrome (delete right character).
3. Return True if either check succeeds; otherwise False.

Time Complexity : O(n)
Space Complexity : O(n)
'''
#Code
def validPalindrome(s):
    l=0
    r=len(s)-1
    while l<=r:
        if s[l]!=s[r]:
            return s[l+1:r+1]==s[l+1:r+1][::-1] or s[l:r]==s[l:r][::-1]
        l+=1
        r-=1
    return True

str=input("Enter String : ")
print(validPalindrome(str))