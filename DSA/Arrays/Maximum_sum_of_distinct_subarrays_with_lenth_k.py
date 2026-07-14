'''Problem:
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

'''

#Approach
'''
1.Build first window
2.Calculate first sum
3.Build frequency map
4.If len(freq)==k
    answer = first sum
5.Now slide by Removing left and Adding right
6.Update sum
7.If len(freq)==k
    update answer

Time Complexity:O(n)
Space Complexity:O(k)
'''

#Code
def max_sum_of_distinct_subarray_with_length_k(nums,k):
    win_s=0
    max_s=0
    freq={}
    for i in range(k):
        win_s+=nums[i]
        freq[nums[i]]=freq.get(nums[i],0)+1
    if len(freq)==k:
        max_s=win_s
    
    for i in range(k,len(nums)):
        left=nums[i-k]
        win_s-=left
        freq[left]=freq.get(left,0)-1
        if freq[left]==0:
            del freq[left]
        right=nums[i]
        win_s+=right
        freq[right]=freq.get(right,0)+1

        if len(freq)==k:
            if max_s<win_s:
                max_s=win_s
    return max_s
    
arr=list(map(int,input("Enter Array: ").split(',')))
k=int(input("Enter length of subarray: "))
print(max_sum_of_distinct_subarray_with_length_k(arr,k))