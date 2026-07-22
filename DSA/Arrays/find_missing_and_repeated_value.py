'''
Problem : You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.
Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
'''
#Approach
'''
1. Keep a candidate and a count. If the count becomes 0, select the current element as the new candidate. 
2. Increment the count if the current element matches the candidate; otherwise, decrement it. 
3. Since the majority element appears more than n/2 times, it remains as the final candidate.

Time Complexity: O(n**2)
Space Complexity: O(1)
'''
#Code
def findMissingAndRepeatedValues(grid):
    n = len(grid)
    N = n*n
    expected_sum = N*(N+1)/2
    expected_sq_sum = N*(N+1)*(2*N+1)/6
    actual_sum = 0
    actual_sq_sum = 0
    for i in grid :
        for j in i :
            actual_sum += j
            actual_sq_sum += j*j
    A = actual_sum - expected_sum
    B = actual_sq_sum - expected_sq_sum
    C = B/A
    twice = ( A + C ) / 2
    missing = ( C - A ) / 2

    return [ twice , missing ]


n=int(input("Enter number of rows : "))
grid=[]
for i in range(n):
    arr=list(map(int,input(f"Enter row {i+1} :").split(',')))
    grid.append(arr)
print(findMissingAndRepeatedValues(grid))