##############Sorting########################
#######################Selectionsort#########################
#It takes first value as minimum and check for actual minimum and then swaps it
#hence putting the minimum value in the front.
'''
def selectionsort(array,size):
    for step in range(size):
        min_indx=step
        for i in range(step+1,size):
            if(array[i]<array[min_indx]):
                min_indx=i
        array[step],array[min_indx]=array[min_indx],array[step]
    return array
data=[12,10,15,20]
new_data=selectionsort(data,len(data))
print(new_data)
'''
#-------------------------Coorg Fruit Farm------------------------------
'''
class fruit_info:
     def __init__(self,namelist,pricelist):
         self.namelist=namelist #contains names
         self.pricelist=pricelist #contains the price/kg

     def get_fruit_price(self,fruit_name):
        if(fruit_name in self.namelist):
            return self.pricelist[self.namelist.index(fruit_name)]
        else:
            return -1

class purchase:
    count=100
    def calculate_price(self,fruit_name,qnty):
        tot_price=0
        price=f.get_fruit_price(fruit_name)
        if(price != -1):
            if(max(f.pricelist) == price and qnty > 1):
                tot_price=qnty*price
                tot_price=tot_price-(tot_price*0.02)
            elif(min(f.pricelist) == price and qnty > 5):
                tot_price=qnty*price
                tot_price=tot_price-(tot_price*0.05)
            else:
                tot_price=qnty*price
            if(self.typecust == "Wholesale"):
                tot_price=tot_price-(tot_price*0.1)
        else:
            print(fruit_name," Stock Unavailable")
        return tot_price

class customer(purchase):
    def __init__(self,typecust,order,quantity):
        self.typecust=typecust
        self.order=order
        self.quantity=quantity
        self.tot_price=0
        self.cust_id="P"+str(purchase.count)
        purchase.count+=1

    def bill(self):
        for i in range(len(self.order)):
            self.tot_price+=self.calculate_price(self.order[i],self.quantity[i])

    def details(self):
        print("-------Bill--------")
        print("The ID is ",self.cust_id)
        print("The total Bill is ",self.tot_price)


f=fruit_info(["Apple","Guava","Orange","Grapes","Sweet_Lime"]
                 ,[200,80,70,110,60])
while(True):
    type_cust=input("Please enter customer type as wholesale or not wholesale")
    print("Enter the order of fruits")
    l1=[i for i in input().split(" ")]
    print("Enter the corresponding quantities")
    l2=[int(i) for i in input().split(" ")]
    customer_obj=customer(type_cust,l1,l2)
    customer_obj.bill()
    customer_obj.details()
    print("*****************************************************")

'''
#-----------------------Softsystem Ltd-------------------------------
#question incomplete
'''
class Employee:
    def validate_basic_salary(self):
        if(self.salary>3000):
            return True
        else:
            False

    def validate_qualification(self):
        if(self.qualification in ["Bachelors","Masters","bachelors","masters"]):
            return True
        else:
            return False

class Graduate:
    def validate_job_brand(self):
        if(self.brand in ["A","B","C"]):
            return True
        else:
            return False

    def calculate_gross_salary(self):
        pass
'''
#---------------------------BakeHouse----------------------------------
'''
class Table:
    def __init__(self,data):
        self.data=data
        self.next=None
class BakeHouse:
    def __init__(self):
        self.head=None
        self.__occupied_table_list=[]

    def get_occupied_table_list(self):
        return self.__occupied_table_list

    def insert(self,num):
        start=self.head
        newnode=Table(num)
        if(start.data> num):
            newnode.next=self.head
            self.head=newnode
        else:
            while(start is not None):
                if(start.next.data<num):
                    start=start.next
            newnode.next=start.next
            start.next=newnode


    def deletebegin(self):
        self.head=self.head.next
        
    def allocate_table(self):
        start=self.head
        if(start is None):
            print("Housefull")
        else:
            self.__occupied_table_list.append(start.data)
            self.__occupied_table_list.sort()
            self.deletebegin()
            return start.data
            
    def deallocate_table(self,num):
        if(num in self.__occupied_table_list):
            self.__occupied_table_list.remove(num)
            self.__occupied_table_list.sort()
        else:
            print("not found")    
        self.insert(num)

    
tab=BakeHouse()
tab.head=Table(1)
t2=Table(2)
t3=Table(3)
t4=Table(4)
t5=Table(5)
t6=Table(6)
t7=Table(7)
t8=Table(8)
t9=Table(9)
t10=Table(10)

#linking
tab.head.next=t2
t2.next=t3
t3.next=t4
t4.next=t5
t5.next=t6
t6.next=t7
t7.next=t8
t8.next=t9
t9.next=t10

print("Allocated table",tab.allocate_table())
print("Allocated table",tab.allocate_table())
print("Allocated table",tab.allocate_table())
print("Occupied tables are")
print(tab.get_occupied_table_list())
tab.deallocate_table(3)
print("Occupied tables are")
print(tab.get_occupied_table_list())
'''
#---------------------------Teacher Student Camp-----------------------
'''
def rewardchild(t1,l1,sid,extra):
    index=t1.index(sid)
    l1[index]+=extra
    return l1

def total_chocolate(l1):
    return sum(l1)

child_id=(10,20,30,40,50)
choco_received=[12,5,3,4,6]
sid=int(input("Enter the student id"))
extra=int(input("Enter the extra chocolates"))
if(sid not in child_id):
    print("Child ID is invalid")
elif(extra<1):
    print("Extra chocolate is less than 1")
else:
    choco_received=rewardchild(child_id,choco_received,sid,extra)

print("total chocolates",total_chocolate(choco_received))
print("list of chocolates received",choco_received)
'''
####################QUICKSORT################################
#partition using pivot and call quick sort for both the half
#after partition, the pivot element comes to its original position
'''
def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if(array[j]<=pivot):
            i+=1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high]=array[high],array[i+1]
    return i+1

def quicksort(array,low,high):
    if(low<high):
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)

array=[8,7,6,1,0,9,2]
quicksort(array,0,len(array)-1)
print(array)
'''
#----------------------------problem statement--------------------------
'''
str1=input("Enter the string").split(" ")
freq=0
word=""
for i in str1:
    if(str1.count(i)>freq):
        if(len(word)<len(i)):
            word=i
            freq=str1.count(i)

print(word)
 '''
#------------------------anagram------------------------------------
'''
def check_anagram(str1,str2):
    c=0
    if(len(str1)==len(str2)):
        for i in str1:
            if(i in str2 and str1.index(i)!= str2.index(i)):
                continue
            else:
                return False
    else:
        return False
    return True

str1=input("Enter the 1st string")
str2=input("Enter the 2nd string")
print("Are the strings anagrams?",check_anagram(str1,str2))

'''

        
    






















































































                
           
