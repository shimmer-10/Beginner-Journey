'''
Problem : You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums.
'''
#Approach
'''
1. Count the frequesncies of each element and store as hash.
2. Calculate sum of all elements having freq == 1.

Time Complexity : O(n)
Space Complexity : O(n)
'''
#Code
def sumOfUnique(nums):
    freq={}
    s=0
    for i in nums:
        freq[i]=freq.get(i,0)+1

    for j in freq:
        if freq[j]==1:
            s+=j
                
    return s

arr=list(map(int,input("Enter array :").split()))
print("Sum of Unique elements:", sumOfUnique(arr))