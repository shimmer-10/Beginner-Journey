'''
Problem: Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
'''
#Approach
'''
1. Use two pointers, one at the beginning and one at the end of the array.
2. Swap the characters at both pointers and move them towards each other until they meet.

Time Complexity: O(n)
Space Complexity: O(1)
'''
#Code
def reverseString(s):
    left,right=0,len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return s

str=input("Enter string:")
print(reverseString(list(str)))
        