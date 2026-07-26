'''
Problem : Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
'''
#Approach
'''

Time Complexity:O(n)
Space Complexity:O(1)
'''
#Code
def numSubarrayProductLessThanK(nums, k):
    end,start=0,0
    product=1
    res=0
    for end in range(len(nums)):
        product*=nums[end]
        while product>=k:
            product//=nums[start]
            start+=1
        res+=end-start+1
    return res

arr=list(map(int,input("Enter Array : ").split(',')))
k=int(input("Enter k : "))
print(numSubarrayProductLessThanK(arr,k))