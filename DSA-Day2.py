#linked list
'''
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Slinkedlist:
    def __init(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval

list1= Slinkedlist()
list1.headval=Node("Mon")#contains the address of the first node object
e2=Node("tue")#contains address of the second node
e3=Node("wed")#contains the address of the third node.
                  
#link first node to the second node
list1.headval.nextval=e2 #nextval of head holds the address of second node 
e2.nextval=e3 #nextval of second holds the address of third node
list1.listprint()

#####################insertion of a node at begining########################
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Slinkedlist:
    def __init(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
    def Atbegining(self,newdata):
        newnode=Node(newdata)
        newnode.nextval=self.headval
        self.headval=newnode
list1= Slinkedlist()
list1.headval=Node("Mon")#contains the address of the first node object
e2=Node("tue")#contains address of the second node
e3=Node("wed")#contains the address of the third node.
                  
#link first node to the second node
list1.headval.nextval=e2 #nextval of head holds the address of second node 
e2.nextval=e3 #nextval of second holds the address of third node
list1.listprint()
list1.Atbegining("sun")
print("after insertion")
list1.listprint()

###########################insertion at the end#############################
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Slinkedlist:
    def __init(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
    def AtEnd(self,newdata):
        newnode=Node(newdata)
        if (self.headval is None):
            self.headval=newnode
            return
        addval=self.headval
        while(addval.nextval is not None):
            addval=addval.nextval
        addval.nextval=newnode
list1= Slinkedlist()
list1.headval=Node("Mon")#contains the address of the first node object
e2=Node("tue")#contains address of the second node
e3=Node("wed")#contains the address of the third node.
                  
#link first node to the second node
list1.headval.nextval=e2 #nextval of head holds the address of second node 
e2.nextval=e3 #nextval of second holds the address of third node
list1.listprint()
list1.AtEnd("thur")
print("after insertion at end")
list1.listprint()

######################insertion at any point#################################
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Slinkedlist:
    def __init(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
    ''
    #using datavalue checking
    def AtAnyPoint(self,newdata):
        newnode=Node(newdata)
        if (self.headval is None):
            self.headval=newnode
            return
        addval=self.headval
        while(addval.dataval!="tue"):
            addval=addval.nextval
        newnode.nextval=addval.nextval
        addval.nextval=newnode
    ''
    #using nodevalue checking
    def InBetween(self,middle_node,newdata):
        if(middle_node is None):
            print("This node is absent")
        else:
            newnode=Node(newdata)
            newnode.nextval=middle_node.nextval
            middle_node.nextval=newnode
list1= Slinkedlist()
list1.headval=Node("Mon")
e2=Node("tue")
e3=Node("thus")
                  
#link first node to the second node
list1.headval.nextval=e2 
e2.nextval=e3 
list1.listprint()
#list1.AtAnyPoint("wed")
list1.InBetween(list1.headval.nextval,"wed")
print("after insertion at any point")
list1.listprint()

#####################Deletion from begining######################

class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Slinkedlist:
    def __init(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
    def delete_start(self):
        if(self.headval is None):
            print("There is no node to delete")
        self.headval = self.headval.nextval
list1= Slinkedlist()
list1.headval=Node("Mon")
e2=Node("tue")
e3=Node("wed")
                  
#link first node to the second node
list1.headval.nextval=e2
e2.nextval=e3
list1.listprint()
list1.delete_start()
print("After deleting")
list1.listprint()

#####################Deletion from end######################

class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Slinkedlist:
    def __init(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
    def delete_end(self):
        if(self.headval is None):
            print("There is no node to delete")
            return
        second_val=self.headval
        while(second_val.nextval.nextval!= None):
            second_val=second_val.nextval
        second_val.nextval=None
        
list1= Slinkedlist()
list1.headval=Node("Mon")
e2=Node("tue")
e3=Node("wed")
                  
#link first node to the second node
list1.headval.nextval=e2
e2.nextval=e3
list1.listprint()
list1.delete_end()
print("After deleting")
list1.listprint()

#--------------------Reversing the single Linked list-----------------

class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Slinkedlist:
    def __init(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
    def delete_end(self):
        second_val=self.headval
        if(self.headval.nextval is None):
            exit()
        while(second_val.nextval.nextval!= None):
            second_val=second_val.nextval
        second_val.nextval=None
    def reverse_list(self):
        start=self.headval
        while(start is not None):
            while(start.nextval is not None):
                start=start.nextval
            print(start.dataval)
            start=self.headval
            self.delete_end()
        
list1= Slinkedlist()
list1.headval=Node("Mon")
e2=Node("tue")
e3=Node("wed")
e4=Node("thur")
e5=Node("Fri")
e6=Node("Sat")
e7=Node("sun")
                  
#link first node to the second node
list1.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
list1.listprint()
print("The reversed list is")
list1.reverse_list()

#########searching the item,count index######################################

class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Slinkedlist:
    def __init(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
    def search(self,item):
        start=self.headval
        while(start.nextval):
            if(start.dataval == item):
                return True

            start=start.nextval
        return False
    def count_node(self):
        c=0
        start=self.headval
        while(start.nextval is not None):
            c+=1
            start=start.nextval
        return c+1
list1= Slinkedlist()
list1.headval=Node("Mon")
e2=Node("tue")
e3=Node("wed")
e4=Node("thur")
e5=Node("Fri")
e6=Node("Sat")
e7=Node("sun")
                  
#link first node to the second node
list1.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
list1.listprint()
if(list1.search("Sat")):
    print("Element Found")
else:
    print("Element not found")

print("The number of nodes are",list1.count_node())

#-----------------------student mark problem-------------------------------

class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Slinkedlist:
    def __init(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
    def insert_node(self,pos_insert,val_insert):
        pos=self.headval
        c=1
        while(pos is not None):
            if(c == pos_insert-1):
                break
            else:
                c+=1
                pos=pos.nextval
        newnode=Node(val_insert)
        newnode.nextval=pos.nextval
        pos.nextval=newnode
    def view_node(self,pos):
        pos_node=self.headval
        c=1
        while(pos is not None):
            if(c == pos):
                break
            else:
                c+=1
                pos_node=pos_node.nextval
        return (pos_node.dataval)
list1=Slinkedlist()
list1.headval=Node(89)
e1=Node(78)
e2=Node(99)
e3=Node(76)
e4=Node(77)
e5=Node(67)
e6=Node(99)
e7=Node(98)
e8=Node(90)
#linking the list
list1.headval.nextval=e1
e1.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
e7.nextval=e8
list1.listprint()
n=int(input("Enter the value to be inserted"))
i=int(input("Enter the position"))
list1.insert_node(i,n)
print("After insertion")
list1.listprint()
print("mark of 5th person is",list1.view_node(5))
print("mark of 7th person is",list1.view_node(7))

#---------------------------Assignment 3-----------------------------
#l1=[11,8,23,7,25,15]
#l2=[6,33,50,31,46,78,16,34]
#double=[8,23,25]
#without creating result node
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Slinkedlist:
    def __init(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
        
    def double_check(self):
        start=self.headval
        while(start is not None):
            inlist=list2.headval
            while(inlist is not None):
                if(start.dataval*2 == inlist.dataval):
                    print(start.dataval)
                    break
                else:
                    inlist=inlist.nextval
            start=start.nextval
#list1
list1=Slinkedlist()
list1.headval=Node(11)
e1=Node(8)
e2=Node(23)
e3=Node(7)
e4=Node(25)
e5=Node(15)
#linking the list
list1.headval.nextval=e1
e1.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5

#list2
list2=Slinkedlist()
list2.headval=Node(6)
f1=Node(33)
f2=Node(50)
f3=Node(31)
f4=Node(46)
f5=Node(78)
f6=Node(16)
f7=Node(34)
#linking the list
list2.headval.nextval=f1
f1.nextval=f2
f2.nextval=f3
f3.nextval=f4
f4.nextval=f5
f5.nextval=f6
f6.nextval=f7

print("first list is")
list1.listprint()
print("second list is")
list2.listprint()
print("The list of double is")
list1.double_check()

#------------------------------------Assignment1-------------------------------
#A,n,*,/,a,p,p,l,e,*,a,/,d,a,y,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,r,*,a,w,a,y
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Slinkedlist:
    def __init(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
    def joining(self):
        str1=""
        start=self.headval
        while(start is not None):
            if(start.dataval =='*' or start.dataval == '/'):
                if(start.nextval.dataval=='*' or start.nextval.dataval=='/'):
                    str1+=" "
                    str1+=(start.nextval.nextval.dataval).upper()
                    start=start.nextval.nextval.nextval
                else:
                    str1+=" "
                    start=start.nextval
            else:
                str1+=start.dataval
                start=start.nextval
        return str1
list1=Slinkedlist()
list1.headval=Node('A')
e1=Node('n')
e3=Node('*')
e4=Node('/')
e5=Node('a')
e6=Node('p')
e7=Node('p')
e8=Node('l')
e9=Node('e')
e10=Node('*')
e11=Node('a')
e12=Node('/')
e13=Node('d')
e14=Node('a')
e15=Node('y')
e16=Node('*')
e17=Node('*')
e18=Node('k')
e19=Node('e')
e20=Node('e')
e21=Node('p')
e22=Node('s')
e23=Node('/')
e24=Node('*')
e25=Node('a')
e26=Node('/')
e27=Node('/')
e28=Node('d')
e29=Node('o')
e30=Node('c')
e31=Node('t')
e32=Node('o')
e33=Node('r')
e34=Node('*')
e35=Node('a')
e36=Node('w')
e37=Node('a')
e38=Node('y')
#linking the list
list1.headval.nextval=e1
e1.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
e7.nextval=e8
e8.nextval=e9
e9.nextval=e10
e10.nextval=e11
e11.nextval=e12
e12.nextval=e13
e13.nextval=e14
e14.nextval=e15
e15.nextval=e16
e16.nextval=e17
e17.nextval=e18
e18.nextval=e19
e19.nextval=e20
e20.nextval=e21
e21.nextval=e22
e22.nextval=e23
e23.nextval=e24
e24.nextval=e25
e25.nextval=e26
e26.nextval=e27
e27.nextval=e28
e28.nextval=e29
e29.nextval=e30
e30.nextval=e31
e31.nextval=e32
e32.nextval=e33
e33.nextval=e34
e34.nextval=e35
e35.nextval=e36
e36.nextval=e37
e37.nextval=e38
print(list1.joining())
'''




















































