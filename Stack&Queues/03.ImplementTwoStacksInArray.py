#Program link - https://practice.geeksforgeeks.org/problems/implement-two-stacks-in-an-array/1#



#Function to push an integer into the stack1.
def push1(a,x):
    global top1
    global top2
    if top1+1 == top2:
        return
    top1 +=1
    a[top1] = x
    
#Function to push an integer into the stack2.
def push2(a,x):
    global top1
    global top2
    if top1+1 == top2:
        return
    top2 -=1
    a[top2] = x
    
#Function to remove an element from top of the stack1.    
def pop1(a):
    global top1
    global top2
    if top1==-1:
        return -1
    temp = a[top1]
    a[top1] = None
    top1 -=1
    return temp
    
    
    
#Function to remove an element from top of the stack2.    
def pop2(a):
    global top1
    global top2
    if top2==101:
        return -1
    temp = a[top2]
    a[top2] = None
    top2+=1
    return temp
    