'''
Problem : Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
'''
#Approach
'''
1. Calculate Total Sum of nums.
2. Derive right sum for every iteration -
    right_sum = total_sum - current_num - left_sum
3. Return current iteration index if left_sum == right_sum 
4. Add num at current index to left_sum during each iteration. 

Time Complexity : O(n)
Space Complexity : O(1)
'''
#Code
def pivotIndex(nums):
    t_sum = sum(nums)
    l_sum = 0
    for i in range(len(nums)):
        r_sum = t_sum - nums[i] - l_sum
        if l_sum == r_sum :
            return i
        l_sum += nums[i]
    return -1

arr = list(map(int , input("Enter nums :").split(',')))
print(pivotIndex(arr))