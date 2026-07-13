'''
Problem: Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.
'''

#Approach:
'''
1. Calculate the sum of the first window of size k.
2. Slide the window by removing the leftmost element and adding the next element.
3. Track the maximum window sum.

# Time Complexity: O(n)
# Space Complexity: O(1)
'''

#Code
def max_sum(nums,k):
    '''
    To fing the maximum sum of any contiguous subarray of size k.
    '''
    l=0
    r=k-1
    maximum=0
    for i in range(l,k):
        maximum+=nums[i]
    window_sum=maximum
    while r<len(nums)-1:
        r+=1
        window_sum=window_sum-nums[l]+nums[r]
        l+=1
        if window_sum>maximum:
            maximum=window_sum
    return maximum
arr = list(map(int,input("Enter Array:").split()))
k = int(input("Enter size of subarray:"))
print(max_sum(arr,k))
