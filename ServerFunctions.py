from BaseFunctions import *

#this method returns the result of searching for a given customer
def findC(name,a):
    n= find(name,a)
    if n == -1:
        return name+" not found in database"
    else:
        a.rotate(-n)
        ph=a.popleft()
        a.appendleft(ph)
        return ph.toString()
 #this method returns the result of adding a customer to the database
def addC(nC, a):
    b=addCustomer(nC,a)
    if b :
        return"Customer Added"
    else:
        return "Customer Already Exists"
#this method returns the result of the deletion of a customer given by name    
def delC(name,a):
    b=delCust(name, a)
    if b :
        return"Customer Deleted"
    else:
        return"Customer does not exist"
#this method returns the result of a customer age update
def updAge(name,age,a):   
    b=modAge(name,age,a)
    if b :
        return"Customer's age modified"
    else:
        return"Customer not found"
#this method returns the result of a customer address update       
def updA(name,add,a):
    b=modAdd(name,add,a)
    if b :
        return"Customer's address modified"
    else:
        return"Customer not found"
#this method returns the result of a customer phone number update        
def updN(name,num,a):
    b=modNum(name,num,a)
    if b :
        return"Customer's Phone Number has been modified"
    else:
        return"Customer not found"
#this method returns a string holding containing all the records in the database        
def printReport(a):
    string = ""
    a= sortDQ(a)
    for element in a:
        string= string + element.toString() + "\n"
    return string
        