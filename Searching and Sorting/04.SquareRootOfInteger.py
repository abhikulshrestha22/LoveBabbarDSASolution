# Problem link - https://practice.geeksforgeeks.org/problems/count-squares3649/1#


import math 

class Solution:
    def countSquares(self, N):
       a = int(math.sqrt(N))
       if a*a==N:
           return a-1
       return a