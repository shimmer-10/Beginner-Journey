'''
Problem : Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''
#Approach
'''
1. Use Kadane's Algorithm to find the maximum subarray sum in a single pass.
2. Track the running sum ('s') and the maximum sum found so far ('m').
3. Reset the running sum to 0 whenever it becomes negative, as it would only reduce the sum of subsequent elements.

Time Complexity : O(n)
Space complexity : O(1)
'''
#Code
def maxSubArray(nums):
    s=0
    m=-float('inf')
    for i in nums :
        s+=i
        m=max(s,m)
        if s < 0:
            s=0
    return m

arr=list(map(int,input("Enter Array :").split(',')))
print(maxSubArray(arr))