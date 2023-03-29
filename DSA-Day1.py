#the operations in Stack(a linear DS based on LIFO)DS are:
#isempty
#isfull
#top
#push
#pop
'''
class stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*self.__max_size #[None,None,None,None]
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full")
        else:
            self.__top+=1
            self.__element[self.__top]=data

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            data=self.__element[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__element[index])
                index-=1

    def get_max_size(self):
        return self.__max_size


obj=stack(4)
obj.push(1)
obj.push(9)
obj.push(4)
obj.push(11)
obj.display()
print(obj.pop())
obj.display()
print(obj.get_max_size())

#queue(based LIFO)
#isempty
#isfull
#front(return element in the front of the queue)
#enqueue(add data in the rear)
#dequeue(remove data from the front)

class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*self.__max_size #[None,None,None,None]
        self.__rear=-1
        self.__front=0
        
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__front> self.__rear):
            return True
        return False

    def dequeue(self):
        if(self.is_empty()):
            print("The queue is empty")
        else:
            data=self.__element[self.__front]
            self.__front+=1
            return data

    def enqueue(self,data):
        if(self.is_full()):
            print("The queue is full")
        else:
            self.__rear+=1
            self.__element[self.__rear]=data

    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__element[index])

    def get_max_size(self):
        return self.__max_size

obj=Queue(5)
print("Is the queue full",obj.is_full())
print("Is the queue empty",obj.is_empty())
obj.enqueue(100)
obj.display()
obj.enqueue(200)
obj.enqueue(300)
obj.enqueue(400)
obj.enqueue(500)
print("Before deletion")
obj.display()
print("After deleting",obj.dequeue())
obj.display()

#----------------------------problem1-------------------------------

class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*self.__max_size #[None,None,None,None]
        self.__rear=-1
        self.__front=0
        
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__front> self.__rear):
            return True
        return False
    
    def enqueue(self,data):
        if(self.is_full()):
            print("The queue is full")
        else:
            self.__rear+=1
            self.__element[self.__rear]=data
    
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__element[index])

    def check_even(self):
        index=self.__front
        while(index<self.__rear):
            c=0
            for i in range(1,11):
                if(self.__element[index]%i==0):
                    continue
                else:
                    c=1
                    break
            if(c==0):
                el=self.__element[index]
                print(el)
            index+=1
        
max_size=int(input())
obj=Queue(max_size)
for i in range(0,max_size):
    obj.enqueue(int(input()))
obj.check_even()

#--------------------------------problem2-----------------------------------

l1=['A','app','a','d','ke','th','doc','awa']
l2=['y','tor','e','eps','ay',None,'le','n']
l3=l2[::-1]
str1=""
for i in range(0,len(l1)):
    if(l1[i]!=None and l3[i]!=None):
        str1+=l1[i]
        str1+=l3[i]
        str1+=" "
    elif(l1[i]==None):
        str1+=l3[i]
        str1+=" "
    else:
        str1+=l1[i]
        str1+=" "

print(str1)
'''
#--------------------------------problem3-------------------------------------
'''
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*self.__max_size #[None,None,None,None]
        self.__rear=-1
        self.__front=0
        
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__front> self.__rear):
            return True
        return False

    def dequeue(self):
        if(self.is_empty()):
            print("The queue is empty")
        else:
            data=self.__element[self.__front]
            self.__front+=1
            return data

    def enqueue(self,data):
        if(self.is_full()):
            print("The queue is full")
        else:
            self.__rear+=1
            self.__element[self.__rear]=data

    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__element[index])

    def get_max_size(self):
        return self.__max_size

class first_queue(Queue):
    pass
class second_queue(Queue):
    pass
class result_queue(first_queue,second_queue):
    pass

n1=int(input())
n2=int(input())
obj1=first_queue(n1)
obj2=second_queue(n2)
obj3=result_queue(n1+n2)
for i in range(0,n1):
    obj1.enqueue(int(input()))
for i in range(0,n2):
    obj2.enqueue(input())
for i in range(0,min(n1,n2)):
    obj3.enqueue(obj1.dequeue())
    obj3.enqueue(obj2.dequeue())
for i in range(min(n1,n2),max(n1,n2)):
    if(max(n1,n2)==n1):
        obj3.enqueue(obj1.dequeue())
    else:
        obj3.enqueue(obj2.dequeue())
obj3.display()
'''
