'''
Created on Mar 5, 2018

@author: BenjaminTherien
'''
from collections import deque
from operator import itemgetter

#find the index of for the first occurence of 
def findI(a):
    for x in range(0,len(a)): 
        if a[x]=='|' :
            return x
    return -1

#converts string input to a tuple
def tokenize(string):
    count = 0
    tup = ()
    ph = string
    while count <= 3:
        if findI(ph)==-1 and count==0 and len(ph)>0 :
            tup = tup + (ph[:len(ph)-1],)
            ph=""
            count=count+1
        elif findI(ph)!=-1 and findI(ph)!=0 :
            tup = tup + (ph[:findI(ph)],)
            ph=ph[findI(ph)+1:len(ph)]
            count=count+1
        elif count != 3 or len(ph) == 0 or ph=="\n" or findI(ph)==0 :
            if count == 0:
                tup = tup + ("NoName",)
            elif count == 1:
                tup = tup + ("Noage",)
            elif count == 2:
                tup = tup + ("Noaddress",)
            elif count == 3:
                tup = tup + ("No#",)
            count = count+1
        else:
            tup = tup + (ph[:findI(ph)],)
            count=count+1
    return tup

#the following class is used to contain customer data
class dat:
    tuple= ()
    
    def __init__(self,tup):
        self.tuple=tup
        
    def __eq__(self, a):
        if self.tuple == a.tuple:
            return True
        return False
        
    def toString(self):
        return str(self.tuple[0])+"|"+str(self.tuple[1])+"|"+str(self.tuple[2])+"|"+str(self.tuple[3])
   
    def setAge(self, newAge):
        self.tuple = (self.tuple[0],newAge,self.tuple[2],self.tuple[3])
    
    def setAddress(self, newAdd):
        self.tuple = (self.tuple[0],self.tuple[1],newAdd,self.tuple[3])
    
    def setNum(self, newNum):
        self.tuple = (self.tuple[0],self.tuple[1],self.tuple[2],newNum)
        
#this method is used to search for a customer by name
def find(key, a):
    count =0
    for element in a:       
        if element.tuple[0] == key:
            return count 
        count=count +1
    return -1
#this method is used to add a customer of a given name to the database 
def addCustomer(nC,a):
    obj=dat(nC)
    for element in a:       
        if element.__eq__(obj):
            return False
    a.append(obj)
    return True
#this method is used to delete a customer of a given name in the database
def delCust(name,a):  
    val= find(name, a)
    if val == -1:
        return False
    else :
        a.rotate(-val)
        a.popleft()
        return True
#this method is used to modify the age of a customer given by name 
def modAge(name, nAge,a):
    val= find(name, a)
    if val == -1:
        return False
    else :
        a.rotate(-val)
        ph= a.popleft()
        ph.setAge(nAge)
        a.appendleft(ph)
        return True
#this method is used to modify the address of a customer given by name 
def modAdd(name, nAdd,a):
    val= find(name, a)
    if val == -1:
        return False
    else :
        a.rotate(-val)
        ph= a.popleft()
        ph.setAddress(nAdd)
        a.appendleft(ph)
        return True
#this method is used to modify the phone number of a customer given by name     
def modNum(name, nNum,a):
    val= find(name, a)
    if val == -1:
        return False
    else :
        a.rotate(-val)
        ph= a.popleft()
        ph.setNum(nNum)
        a.appendleft(ph)
        return True
#this method is used to put the info from the database into a deque  
def getData(file):
    deck = deque()
    fil = open(file,"r", 1)
    for line in fil:
        tup=tokenize(line)
        if tup[0] !="NoName" :
            deck.append(dat(tup)) 
    return deck 
#this method is used to sort a deque alphabetically
def sortDQ(dq):
    l=[]
    for element in dq:
        l.append(element.tuple)
    l.sort(key=itemgetter(0))
    deck =deque()
    for x in range(0,len(l)):
        deck.append(dat(l[x]))        
    return deck
        
