class DLLNode:
    def __init__(self,d):
        self.prev = None
        self.data = d
        self.next = None

class MyStack:
    def __init__(self):
        self.count =0
        self.head = None
        self.mid = None
        
    
    def push(self,data):
        print(str(data)+ "is pushed")
        node = DLLNode(data)
        if self.head is None:
            self.head = node
            self.mid = node
            self.count+=1
            return
        prev = self.head
        self.head = node
        prev.next = node
        node.prev = prev
        self.count+=1
        
        if self.count==1:
            self.mid = self.head
        else:
            if self.count %2 !=0:
                self.mid = self.mid.next



    def pop(self):
        if self.head is None:
            return -1
        current = self.head
        prev = current.prev
        current.prev = None
        self.head = prev
        self.count -= 1
        if prev is not None:
            prev.next = None
        
        if self.head == None:
            self.mid = None
        else:
            if self.count%2==0:
                self.mid = self.mid.prev
        return current.data
    
    def find_mid(self):
        if self.mid:
            return self.mid.data
        else:
            return -1
    
    def delete_mid(self):
        if self.mid is None:
            return -1
        if self.count == 0:
            return -1
        if self.count==1:
            temp = self.mid
            self.mid = None
            self.head = None
            self.count -=1
            return temp.data
        if self.count ==2:
            temp = self.mid.data
            self.head = self.head.prev
            self.mid = self.mid.prev
            self.head.next = None
            self.count -=1
            return temp.data

        else:
            temp = self.mid.data
            midprev = self.mid.prev
            midnext = self.mid.next
            midprev.next = midnext
            midnext.prev = midprev
            self.count-=1
            if self.count%2!=0:
                self.mid = self.mid.next
            else:
                self.mid = self.mid.prev
            return temp

    def print_stack(self):
        current = self.head
        res = []
        while current is not None:
            res.insert(0, current.data)
            current = current.prev
        return res




        

    

stack = MyStack()
stack.push(2)
stack.push(3)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.print_stack())
print('item mid is' + str(stack.find_mid()))
# # print('item popped is' + str(stack.pop()))
stack.push(6)
print('item mid is' + str(stack.find_mid()))
# print('item popped is' + str(stack.pop()))
# print('item mid is' + str(stack.find_mid()))
print(stack.print_stack())
print('item mid deleted is ' + str(stack.delete_mid()))
print(stack.print_stack())
print(stack.find_mid())



