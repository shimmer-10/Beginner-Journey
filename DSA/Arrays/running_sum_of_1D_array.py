'''
Problem: Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
'''
#Approach
'''
Traverse the array once, keep a running sum, and update each
element with the cumulative sum up to that index.

Time Complexity:O(n)
Space Complexity:O(1)
'''
#Code
def runningSum(nums):
    s=0
    for i in range(len(nums)):
        s+=nums[i]
        nums[i]=s
    return nums

arr=list(map(int,input("Enter Array:").split(',')))
print(runningSum(arr))