#Linear Search
#Going through the array sequentially(good for unsorted data)
'''
def linearsearch(array,data):
    for i in range(0,len(array)):
        if(array[i]==data):
            return(i)
    return -1

array=[1,5,3,6,8,9,3,4,93]
data=6
result=linearsearch(array,data)
if(result == -1):
    print("Element not found")
else:
    print("The value is found in ",result)
'''

#Binary Search
#getting the mid value and searching the item
'''
def binarysearch(array,low,high,data):
    while(low<=high):
        mid=high+low//2
        if(array[mid]==data):
            return mid
        elif(array[mid]< data):
            low=mid+1
        else:
            high=mid-1
    return -1
        
            
array=[1,5,3,6,8,9,3,4,93]#[1,3,3,4,5,6,8,9,93]
data=9
array.sort()
result=binarysearch(array,0,len(array)-1,data)
if(result==-1):
    print("Element not found")
else:
    print("The value is found at ",result)
'''

#Binary Tree
#inserting,searching,removing,deleting
########################Tree traversing#######################3
'''
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

    def preorder(self,root):
        if(root):
            #printing the root
            print(str(root.val),"->",end=' ')
            #traversing the left node
            self.preorder(root.left)
            #traversing the right
            self.preorder(root.right)

    def inorder(self,root):
        if(root):
            self.inorder(root.left)
            print(str(root.val),"->",end=" ")
            self.inorder(root.right)

    def postorder(self,root):
        if(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(str(root.val),"->",end=" ")
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("Preorder Traversal")
root.preorder(root)#root-left-righ
print("\nInorder Traversal")
root.inorder(root)#left-root-right
print("\nPostorder Traversal")
root.postorder(root)#left-right-root
'''

#Binary Search Tree
#properties
#1=> left node has value less than the root node
#2=>right node has value greater than the root node
#3=>left and right subtree must also be a binary search tree
'''
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

def insert(node,key):
    if(node is None):
        return Node(key)
    if(key<node.key):
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def preorder(root):
    if(root):
        #printing the root
        print(str(root.key),"->",end=' ')
        #traversing the left node
        preorder(root.left)
        #traversing the right
        preorder(root.right)
    

root=None
root=insert(root,6)
root=insert(root,5)
root=insert(root,7)
root=insert(root,4)
preorder(root)
'''

#-------------------problem statement--------------------------------------
class Node:
    def __init__(self,name,people,seat):
        self.name=name
        self.seat=seat
        self.people=people
        self.nextval=None
class Compartment:
    def __init__(self):
        self.headval=None

    def display(self):
        start=self.headval
        while(start is not None):
            print(start.name)
            start=start.nextval
        
class Train:
    def __init__(self,name,comp_list):
        self.__name=name
        self.__l1=comp_list#listsof compartments

    def get_train_name(self):
        return self.__name

    def get_comp_list(self):
        start=self.__l1.headval
        while(start is not None):
            print(start.name)
            start=start.nextval
        
    def count_comp(self):
        start=self.__l1.headval
        c=0
        while(start is not None):
            c+=1
            start=start.nextval
        return c
    
    def check_vacancy(self):
        start=self.__l1.headval
        c=0
        while(start is not None):
            if(start.seat-start.people > start.seat*0.5):
                c+=1
            start=start.nextval
        return c

Comparts=Compartment()
Comparts.headval=Node("SL",250,400)
e2=Node("2AC",125,280)
e3=Node("3AC",120,300)
e4=Node("FC",160,300)
e5=Node("1AC",100,210)
#linking the nodes
Comparts.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5

t1=Train("Train1",Comparts)
print("The number of compartments are ",t1.count_comp())
print("The vacancy are ",t1.check_vacancy())


























































