#########################Doubly Linked list#############################
#operations->isempty,length,insert,delete
'''
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Dlinkedlist:
    def __init__(self):
        self.head=None
        
    def listprint(self):
        start=self.head
        while(start is not None):
            print(start.data)
            start=start.next

    def isempty(self):
        if(self.head is None):
            return True
        else:
            return False

    def insert_begining(self,newdata):
        newnode=Node(newdata)
        if(self.isempty()):
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode

    def insert_end(self,newdata):
        newnode=Node(newdata)
        end=self.head
        while(end.next is not None):
            end=end.next
        end.next=newnode
        newnode.prev=end

    def list_length(self):
        c=1
        start=self.head
        while(start.next is not None):
            c+=1
            start=start.next
        return c

    def insert_mid(self,index,newdata):
        if(self.list_length() < index):
            print("Out of bound")
            return
        if(index ==1):
            self.insert_begining(newdata)
        elif(index== self.list_length()):
            self.insert_end(newdata)
        else:
            newnode=Node(newdata)
            i=1
            start=self.head
            while(start.next is not None):
                if(i == index-1):
                    break
                else:
                    i+=1
                    start=start.next
            newnode.prev=start
            newnode.next=start.next
            start.next=newnode
    def delete_begin(self):
        if(self.head is None):
            print("No node to delete")
        elif(self.head.next is None):
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None

    def delete_end(self):
        if(self.isempty()):
            print("No Nodes to delete")
        elif(self.head.next is None):
            self.head=None
        else:
            end=self.head
            while(end.next.next is not None):
                end=end.next
            end.next=None
    def delete_inbetween(self,index):
        if(index > self.list_length()):
            print("The node dont exist")
        elif(index == 1):
            self.delete_begin()
        elif(index == self.list_length()):
            self.delete_end()
        else:
            i=1
            start=self.head
            while(start.next is not None):
                if(i == index-1):
                    break
                else:
                    i+=1
                    start=start.next
            start.next=start.next.next
            start.next.prev=start
            
list1=Dlinkedlist()
print(list1.isempty())
list1.insert_begining(5)
list1.insert_begining(6)
list1.listprint()
print("after insertion in end")
list1.insert_end(7)
list1.listprint()
list1.list_length()
list1.insert_mid(2,10)
print("After insertion")
list1.listprint()
print("The length is",list1.list_length())
list1.delete_begin()
print("After deleteing from the begining")
list1.listprint()
list1.delete_end()
print("After deleting from the last")
list1.listprint()
list1.insert_begining(9)
list1.insert_begining(11)
list1.insert_mid(4,18)
print("current list")
list1.listprint()
list1.delete_inbetween(4)
print("After deleteing")
list1.listprint()

#-----------------Deleting duplicacy from the doubly linked list---------------

class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Dlinkedlist:
    def __init__(self):
        self.head=None
        
    def listprint(self):
        start=self.head
        while(start is not None):
            print(start.data)
            start=start.next
    def delete_end(self):
        end=self.head
        while(end.next.next is not None):
            end=end.next
        end.next=None
        return

    def remove_duplicate(self):
        start=self.head
        while(start is not None):
            dup=start.next
            while(dup is not None):
                if(dup.data == start.data):
                    if(dup.next is not None):
                        start.next=dup.next
                        dup.next.prev=start
                        dup=dup.next
                        continue
                    else:
                        self.delete_end()
                        break
                dup=dup.next
            start=start.next
            
list1=Dlinkedlist()
list1.head=Node(11)
n2=Node(10)
n3=Node(3)
n4=Node(7)
n5=Node(7)
n6=Node(10)
#linking the nodes
list1.head.next=n2
n2.prev=list1.head
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3
n4.next=n5
n5.prev=n4
n5.next=n6
n6.prev=n5

print("The list is")
list1.listprint()
print("After removing duplicacy")
list1.remove_duplicate()
list1.listprint()

####################postfix expression###############################
class Evaluate:
    def __init__(self,capacity):
        self.array=[]
        self.top=-1
        self.capacity=capacity
    def isempty(self):
        if(self.top==-1):
            return True
        else:
            return False
    def pop(self):
        if(not self.isempty()):
            self.top-=1
            return self.array.pop()
        else:
            return ("$")
    def push(self,op):
        self.top+=1
        self.array.append(op)
    
    def postfixevaluation(self,exp):
        for i in exp:
            if(i.isdigit()):
                self.push(i)
            else:
                val1=self.pop()
                val2=self.pop()
                self.push(str(eval(val2+i+val1)))
        return int(self.pop())

if __name__=="__main__":
    exp="231*+9-"
    obj=Evaluate(len(exp))
    print(obj.postfixevaluation(exp))
    

#--------smaller number is in bottom and greater number is in the top-----------
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*self.__max_size #[None,None,None,None]
        self.__top=-1
        self.__array=[]
    def isempty(self):
        if(self.__top==-1):
            return True
        else:
            return False
    def pop(self):
        n=self.__element[self.__top]
        self.__top-=1
        return n

    def push(self,op):
        self.__top+=1
        self.__element[self.__top]=op
            
    def get_max_size(self):
        return self.__max_size
    
    def arrange(self):
        index=self.__top
        while(index>=0):
            n=self.pop()
            self.__array.append(n)
            index-=1
        self.__array.sort()
        for i in self.__array:
            self.push(i)

    def display(self):
        index=self.__top
        while(index >=0):
            print(self.__element[index])
            index-=1
        return

s1=Stack(5)
s1.push(5)
s1.push(66)
s1.push(5)
s1.push(8)
s1.push(7)
print("The stack is ")
s1.display()
print("The sorted stack is")
s1.arrange()
s1.display()
'''






























































