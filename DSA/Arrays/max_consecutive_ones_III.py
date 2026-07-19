'''
Problem: Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
'''
#Approach
'''
1. Use a sliding window with two pointers (left and right).
2. Expand the window by moving the right pointer.
3. Whenever a 0 is encountered, increment the zero counter.
4. If the number of zeros exceeds k, shrink the window from the left
   until the window again contains at most k zeros.
   - If a 0 leaves the window, decrement the zero counter.
5. After every valid window, calculate its length and update the
   maximum length obtained.
6. Continue until the right pointer reaches the end of the array.

Time Complexity: O(n)
Space Complexity: O(1)
'''

#Code
def longestOnes(nums, k):
    left,right=0,0
    zeroes=0
    max_len=0
    while right<len(nums):
        if nums[right]==0:
            zeroes+=1
        while zeroes>k:
            if nums[left]==0:
                zeroes-=1
            left+=1
        right+=1
        curr_len=right-left
        max_len=max(curr_len,max_len)
    return max_len

arr=list(map(int,input("Enter array:").split(',')))
k=int(input("Enter no. of flips:"))
print(longestOnes(arr,k))                


            