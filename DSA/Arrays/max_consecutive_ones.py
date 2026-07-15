'''
Problem : Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''
#Approach
'''
1. Traverse array ones.
2. If the current element is 1, increment count.
3. Otherwise, reset count to 0.
4. After each element, update res if count is greater than res.
5. Return res.

Time Complexity:O(n)
Space Complexity:O(1)
'''

#Code
def MaxConsecutiveCount(nums):
    curr=0
    count=0
    res=0
    while curr<len(nums):
        if nums[curr]==1:
            curr+=1
            count+=1
        else:
            curr+=1
            count=0
        if res<count:
            res=count
    return res