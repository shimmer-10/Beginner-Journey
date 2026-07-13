'''
Problem:1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

#Approach:
'''
1. Create an empty dictionary (seen) to store numbers and their indices.
2. Traverse the array once.
3. For each number, calculate the required complement:
    required = target - current_number
4. If the complement already exists in the dictionary,return the current index and the stored index.
5. Otherwise, store the current number with its index in the dictionary.
6. Since dictionary lookup takes O(1) on average, the solution finds the answer in a single traversal.


Time Complexity: O(n)
Space Complexity: O(n)
'''



#Code
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
