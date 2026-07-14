'''
Problem:Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

'''
#Approach
'''
1. Sort the array.
2. Fix one element at a time using index i.
3. Use two pointers:
   left = i + 1
   right = n - 1
4. If the sum is:
   less than 0 → move left forward.
   greater than 0 → move right backward.
   equal to 0 → store the triplet, move both pointers, and skip duplicate values.
5. Skip duplicate values of i to avoid repeated triplets.

Time Complexity: O(n²)
Space Complexity: O(1) (excluding the output list)
'''


#Code
def three_sum(nums) :
    n=len(nums)
    res=[]
    for i in range(n-2):
        f=i+1
        s=n-1
        if i>0 and nums[i]==nums[i-1]:
            continue
        while f<s:
            if nums[i]+nums[f]+nums[s]<0:
                f+=1
            elif nums[i]+nums[f]+nums[s]>0:
                s-=1
            else:
                res.append([nums[i],nums[f],nums[s]])
                f+=1
                s-=1
                while f<s and nums[f]==nums[f-1]:
                    f+=1
                while f<s and nums[s]==nums[s+1]:
                    s-=1
        return res 

arr=list(map(int,input("Enter Array:").split(',')))
print(three_sum(arr))