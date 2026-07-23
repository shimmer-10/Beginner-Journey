'''
Problem : Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
#Approach
'''
Use XOR(^)
a^a=0
a^0=a

Time Complexity: O(n)
Space Complexity: O(1)
'''
#Code
def SingleNumber(nums):
    ans=0
    for i in nums:
        ans^=i
    return ans

nums=list(map(int,input("Enter Array:").split(',')))
print(SingleNumber(nums))