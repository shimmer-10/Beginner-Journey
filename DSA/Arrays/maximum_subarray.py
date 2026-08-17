'''
Problem :
'''
#Approach
'''
1.

Time Complexity :
Space complexity :
'''
#Code
def maxSubArray(nums):
    s=0
    m=-float('inf')
    for i in nums :
        s+=i
        m=max(s,m)
        if s < 0:
            s=0
    return m

arr=list(map(int,input("Enter Array :").split(',')))
print(maxSubArray(arr))