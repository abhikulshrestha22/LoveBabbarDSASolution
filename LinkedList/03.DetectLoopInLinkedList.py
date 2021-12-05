# Problem Link
# https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        low = head
        high = head
        
        while ( high is not None and high.next is not None):
            high = high.next.next
            low = low.next
            if high == low:
                return True
        return False