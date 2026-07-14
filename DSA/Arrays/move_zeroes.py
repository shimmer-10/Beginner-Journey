'''
Problem:Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''
#Approach
'''
1.Create two pointers read and write(say).
2.Write will tell position of where to place next non zero digit.
3.Read will trace whole array.
4.When any non zero digit is found , swap it to position of write and move write one place forward. 

Time Complexity:O(n)
Space ComplexityO(1)
'''

#Code
def move_zero(nums):
    read=0
    write=0
    if nums:
        while read<len(nums):
            if nums[read]!=0:
                nums[read],nums[write]=nums[write],nums[read]
                write+=1
            read+=1
        return nums
    else:
        return "Empty Array!"
arr=list(map(int,input("Enter Array: ").split(',')))
print(move_zero(arr))
