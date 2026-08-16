'''
Problem : There is a biker going on a road trip. The road trip consists of n + 1 points at various altitudes. The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
'''
#Approach
'''
1. Maintain the current altitude using a running sum.
2. After each gain, update the highest altitude.
3. Return the highest altitude.

Time Complexity : O(n)
Space Complexity :O(1)
'''
#Code
def largestAltitude(gain) :
    curr=0
    h=0
    for i in gain:
        curr+=i
        h=max(curr,h)
    return h

gain=list(map(int,input("Enter gain :").split()))
print(largestAltitude(gain))