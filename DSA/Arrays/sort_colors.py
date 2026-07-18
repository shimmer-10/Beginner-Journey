'''
Problem: Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
'''

#Approach
'''
Use three pointers:
1. low -> next position for 0.
2. mid -> current element being checked.
3. high -> next position for 2.

- If nums[mid] == 0, swap it with nums[low] and move both low and mid.
- If nums[mid] == 1, it is already in the correct position, so move mid.
- If nums[mid] == 2, swap it with nums[high] and move high only (do not move mid because the swapped element is still unprocessed).

Time Complexity:O(n)
Space Complexity:O(1)
'''

#Code
def sortColors(nums):
    mid=0
    low=0
    high=len(nums)-1
    while mid<=high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            mid+=1
            low+=1
        elif nums[mid]==2:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
        else:
            mid+=1
    return nums

arr=list(map(int,input("Enter nums:").split(',')))
print(sortColors(arr))