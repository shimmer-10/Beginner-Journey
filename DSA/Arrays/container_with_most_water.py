'''
Problem:You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
'''
#Approach
'''
1. Start by placing two poiters at both end of array.
2. Iterate the poniters while left<right.
3. Calculate water in cointainer(area) each time
4. Move the pointer pointing at lower height.
5. Equate max_water=curr_water, if curr_water>max_water.

Time Complexity:O(n)
Space Complexity:O(1)
'''
#Code
def maxArea(height):
    left,max_water=0,0
    right=len(height)-1
    while left<right:
        curr_water=(right-left)*min(height[left],height[right])
        if max_water<curr_water:
            max_water=curr_water
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return max_water
    
height_arr=list(map(int,input("Enter Heights:").split()))
print(maxArea(height_arr))
