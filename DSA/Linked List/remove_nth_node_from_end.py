'''
Problem: Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
#Approach
'''
1. Create a dummy node and connect it before the head.
2. Place both fast and slow pointers at the dummy node.
3. Move the fast pointer (n + 1) steps ahead.
4. Move both pointers together until fast reaches the end.
5. Slow will now be just before the node to delete.
6. Remove the target node by changing pointers.

Time Complexity:O(n)
Space Compexity:O(1)
'''

#code
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#solution
def removeNthfromEnd(head,n):
    dummy=ListNode(None)
    dummy.next=head
    f=dummy
    s=dummy
    for i in range(n+1):
        s=s.next
    while s!=None:
        f=f.next
        s=s.next
    f.next=f.next.next
    return dummy.next
    
#For Testing solution
def linked_list_creator(lst):
    dummy=ListNode(None)
    curr=dummy
    for i in lst:
        curr.next=ListNode(i)
        curr=curr.next
    return dummy.next
def display_head(head):
    curr=head
    while curr!=None:
        print(curr.val,"->" if curr.next!=None else "",end='')
        curr=curr.next

lst = list(map(int, input("Enter list: ").split(',')))
n=int(input("Enter node to be deleted from end:"))
lst_head=linked_list_creator(lst)
head=removeNthfromEnd(lst_head,n)
display_head(head)

