#!/usr/bin/env python
# coding: utf-8

# ## Medical Shop : 

# In[11]:


medicana = {
    1 : {"medical":"Paracetamol", 'quantity':100,'costperstrip':35},
    
    2 : {"medical":"Cetzine", 'quantity':200,'costperstrip':20},
    
    3 : {"medical":"Azithral", 'quantity':120,'costperstrip':80},
    
    4 : {"medical":"Karvol", 'quantity':70,'costperstrip':30},
    
    5 : {"medical":"Cefix", 'quantity':100,'costperstrip':70},
    
    6 : {"medical":"Sarridon", 'quantity':200,'costperstrip':45},
    
    7 : {"medical":"Sinarest", 'quantity':100,'costperstrip':120},
    
    8 : {"medical":"EyeDrop", 'quantity':70,'costperstrip':70},}
   
def detail():
    
    name = input("please share your name = ")
    address = input("Confirm your address,Please : ")
    distance = int(input("Enter distance from Medical shop : "))
    return check,name,address,distance

def store():
    print("\nNamaste Madam/Sir , Welcome to Medicana Mediacal-Store!")
    print("\nI am here to help you :----\n")
    print("\nAvailable Medicines Stocks here : \n")
    print("%10s %15s %10s %10s"%("sr_no","Medicine","Strips","MRP"))
    print("%10s %15s %10s %10s"%("1",medicana[1]['medical'],medicana[1]['quantity'],medicana[1]['costperstrip']))
    print("%10s %15s %10s %10s"%("2",medicana[2]['medical'],medicana[2]['quantity'],medicana[2]['costperstrip']))
    print("%10s %15s %10s %10s"%("3",medicana[3]['medical'],medicana[3]['quantity'],medicana[3]['costperstrip']))
    print("%10s %15s %10s %10s"%("4",medicana[4]['medical'],medicana[4]['quantity'],medicana[4]['costperstrip']))
    print("%10s %15s %10s %10s"%("5",medicana[5]['medical'],medicana[5]['quantity'],medicana[5]['costperstrip']))
    print("%10s %15s %10s %10s"%("6",medicana[6]['medical'],medicana[6]['quantity'],medicana[6]['costperstrip']))
    print("%10s %15s %10s %10s"%("7",medicana[7]['medical'],medicana[7]['quantity'],medicana[7]['costperstrip']))
    print("%10s %15s %10s %10s"%("8",medicana[8]['medical'],medicana[8]['quantity'],medicana[8]['costperstrip'])) 

def requirements():
    print("\nPlease , tell me your requirements : ")
    Paracetamol = int(input("How many Paracetamol strips are required : "))
    Cetzine = int(input("How many Cetzine strips are required : "))
    Azithral = int(input("How many Azithral strips are required : "))
    Karvol = int(input("How many Karvol strips are required : "))
    Cefix = int(input("How many Cefix strips are required : "))
    Sarridon = int(input("How many Sarridon strips are required : "))
    Sinarest = int(input("How many Sinarest strips are required : "))
    EyeDrop = int(input("How many EyeDrop are required : "))
    return Paracetamol,Cetzine,Azithral,Karvol,Cefix,Sarridon,Sinarest,EyeDrop
def cost():
    Paracetamol_amount = 35*Paracetamol
    Cetzine_amount = 20*Cetzine
    Azithral_amount=80*Azithral
    Karvol_amount=30*Karvol
    Cefix_am = 70*Cefix
    Sarridon_am = 45*Sarridon
    Sinarest_am = 120*Sinarest
    EyeDrop_am = 70*EyeDrop
    
    return Paracetamol_amount,Cetzine_amount,Azithral_amount,Karvol_amount,Cefix_am,Sarridon_am,Sinarest_am,EyeDrop_am
def bill_statement():
    print("\n----------------------------Your bill statement-------------------------------\n")
    print("Name = ",name)
    print("Address = ",address)
    print("\nLocation from Medical shop = {}km\n".format(distance))
    print("%10s %15s %15s %10s"%("sr_no","Medicine","Quantity","Amount"))
    print("%10s %15s %15d %10d"%("1","Paracetamol",Paracetamol,Paracetamol_amount))
    print("%10s %15s %15d %10d"%("2","Cetzine",Cetzine,Cetzine_amount))
    print("%10s %15s %15d %10d"%("3","Azithral",Azithral,Azithral_amount))
    print("%10s %15s %15d %10d"%("4","Karvol",Karvol,Karvol_amount))
    print("%10s %15s %15d %10d"%("5","Cefix",Cefix,Cefix_am))
    print("%10s %15s %15d %10d"%("6","Sarridon",Sarridon,Sarridon_am))
    print("%10s %15s %15d %10d"%("7","Sinarest",Sinarest,Sinarest_am))
    print("%10s %15s %15d %10d"%("8","EyeDrop",EyeDrop,EyeDrop_am))
    
    Total_cost = Paracetamol_amount+Cetzine_amount+Azithral_amount+Karvol_amount+Cefix_am+Sarridon_am+Sinarest_am+EyeDrop_am
    print("\nTotal Cost = ",Total_cost)
    return Paracetamol_amount,Cetzine_amount,Azithral_amount,Karvol_amount,Cefix_am,Sarridon_am,Sinarest_am,EyeDrop_am,Total_cost

def extra_charge():
    delivery = 0
    if distance>0 and distance<=2:
        delivery = 0
        print("No Delivery charges for {}km".format(distance))
        Total_bill_amount = Total_cost+0
        print("\nTotal Bill Amount = ",Total_bill_amount)
    elif distance>=3 and distance<10:
        delivery = delivery + 25
        Total_bill_amount = Total_cost+delivery
        print("Delivery Charges for {}km = ".format(distance),delivery)
        print("\nTotal Bill Amount (Total Amount + Delivery Charges) = ",Total_bill_amount)
    elif distance>=10 and distance<20:
        delivery = delivery + 50
        Total_bill_amount = Total_cost+delivery
        print("Delivery Charges for {}km = ".format(distance),delivery)
        print("\nTotal Bill Amount (Total Amount + Delivery Charges) = ",Total_bill_amount)
    else:
        delivery = delivery + 100
        Total_bill_amount = Total_cost+delivery
        print("Delivery Charges for {}km = ".format(distance),delivery)
        print("\nTotal Bill Amount (Total Amount + Delivery Charges) = ",Total_bill_amount)
    return delivery

while True:
    store()
    check = input("\nDo you have prescription  yes/no ? = ")
    if check == 'yes' or check=='Yes' or check == 'YES':
        check,name,address,distance=detail()
        Paracetamol,Cetzine,Azithral,Karvol,Cefix,Sarridon,Sinarest,EyeDrop=requirements()
        Paracetamol_amount,Cetzine_amount,Azithral_amount,Karvol_amount,Cefix_am,Sarridon_am,Sinarest_am,EyeDrop_am=cost()
        Paracetamol_amount,Cetzine_amount,Azithral_amount,Karvol_amount,Cefix_am,Sarridon_am,Sinarest_am,EyeDrop_am,Total_cost=bill_statement()
        delivery=extra_charge()
        print("\n{} ,Please pay your bill and We will deliver your medicine at your doorstep".format(name))
        print("\n------------Thank you for Choosing Medicana Medical-Store------------")
    else:
        print("\nSorry Sir/Madam , Please come with Doctor Prescription")
        break
    break
        
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


def square(num):      # close to square and use shift+tab for know about docstring.
    '''square():squaring my integer number'''
    x = num*num
    print(x)
square(7)


# In[ ]:


list = [2,4,7,8,2,1,3]
def sorting(list):
    list.sort()
    print(list)
sorting(list)


# In[ ]:





# In[ ]:


a = [2,4,7,8,2,1,3]
a.insert(6,35)
print(a)


# In[ ]:


lst = []
a = [2,4,7,8,2,1,3]
for i in a:
    lst.append(i)
print(lst)


# In[ ]:


b = []
a = [2,4,7,8,2,1,3]
b=a
#print(id(a))
#print(id(b))
b=a.copy()
print(b)


# In[ ]:


list4 = [1,2,3,4,5,6]
a = [i for i in list4 if i%2==0]
print(a)


# In[ ]:




