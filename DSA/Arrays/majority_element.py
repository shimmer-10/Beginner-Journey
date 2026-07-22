'''
Problem : Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
#Approach
'''
Maintain a candidate and a count.
- If count becomes 0, choose the current element as the new candidate.
- If the current element matches the candidate, increment count.
- Otherwise, decrement count.
Since the majority element appears more than n/2 times, it cannot be completely cancelled out by other elements. Therefore, the remaining candidate at the end is the majority element.

Time Complexity: O(n)
Space Complexity: O(1)
'''
#Code
def MajorityElement(nums):
    #Boyer-Moore Algorithm
    count = 0
    candidate = None
    for num in nums :
        if count == 0 :
            candidate = num
        if candidate == num :
            count += 1
        else :
            count -= 1
    return candidate

arr=list(map(int,input("Enter Array : ").split(',')))
print(MajorityElement(arr))
