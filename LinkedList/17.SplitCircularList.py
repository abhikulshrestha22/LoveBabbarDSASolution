class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def splitList(self, head, head1, head2):
        slow = head
        fast = head
        while(fast.next):
            slow = slow.next
            fast = fast.next.next
            if head == fast.next:
                break
        head2 = slow.next
        fast.next = head2
        head1 = head
        slow.next = head1
        
        
        
        
        #this is to emulate pass by reference in python please don't delete below line.
        return head1,head2

soln = Solution()
a = Node(1)
a.next = Node(5)
a.next.next = Node(7)
a.next.next.next = a
head1 = None
head2 = None
soln.splitList(a, head1, head2)
print(head1)
print(head2)