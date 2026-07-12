# Two Sum

'''
Question:1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

def two_sum(nums, target):
    '''
    Return indices of two numbers whose sum is equal to target
    '''
    seen={}    # Dictionary provides average O(1) lookup time.
    for i, num in enumerate(nums):  #enumerate()- return (index,item)
        req=target-num
        if req in seen:
            return [i,seen[req]]
        else:
            seen[num]=i
 
nums=list(map(int,input("Enter Your List of numbers:").split(',')))
tar=int(input("Enter target sum:"))
print(two_sum(nums,tar))