#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
f=open('Desktop/HW3/dataset2.csv')
csv_f=csv.reader(f)
data=[]
for rows in csv_f:
    data.append(rows)


# In[14]:


def check(data,index):
    success=0
    fail=0;
    for rows in data:
        if(rows[0]=='1'):
            success+=1
        if(rows[0]=='0'):
            fail+=1
    psuccess=success/len(data)
    pfail=fail/len(data)
    successx=[0]*23
    failx=[0]*23
    successo=[0]*23
    failo=[0]*23
    for rows in data:
        for i in range(1,23):
            if(rows[i]=='1' and rows[0]=='1'):
                successx[i]+=1;
            if(rows[i]=='1' and rows[0]=='0'):
                failx[i]+=1;
            if(rows[i]=='0' and rows[0]=='1'):
                successo[i]+=1;
            if(rows[i]=='0' and rows[0]=='0'):
                failo[i]+=1;
    correct=0
    incorrect=0
    psuccess=success
    pfail=fail
    if(data[index][0]=="1"):
        success-=1
    for i in range(1,23):
        if(data[index][i]=='1'):
            successx[i]-=1
        if(data[index][i]=='0'):
            successo[i]-=1
    if(data[index][0]=="0"):
        fail-=1
    for i in range(1,23):
        if(data[index][i]=='1'):
            failx[i]-=1
        if(data[index][i]=='0'):
            failo[i]-=1

    for i in range(1,23):
        if(data[index][i]=='1'):
            pfail*=failx[i]/fail
            psuccess*=successx[i]/success
        if(data[index][i]=='0'):
            pfail*=failo[i]/fail
            psuccess*=successo[i]/success
    if(psuccess>pfail):
        if(data[index][0]=="1"):
            return True
        else:
            return False
    if(psuccess<pfail):
        if(data[index][0]=="0"):
            return True
        else:
            return False
#     for rows in data:
#         psuccess=success
#         pfail=fail
#         for i in range(1,len(rows)):
#             if(rows[i]=='1'):
#                 psuccess*=successx[i]/success
#                 pfail*=failx[i]/fail
#             if(rows[i]=='0'):
#                 psuccess*=successo[i]/success
#                 pfail*=failo[i]/fail
#         if(pfail>psuccess):
#             if(rows[0]=='0'):
#                 correct+=1
#             else:
#                 incorrect+=1
#         if(pfail<psuccess):
#             if(rows[0]=='1'):
#                 correct+=1
#             else:
#                 incorrect+=1


# In[15]:


correct=0
incorrect=0
size=len(data)
for i in range(size):
    n=check(data,i)
    if(n==True):
        correct+=1
    elif(n==False):
        incorrect+=1
print(correct/(incorrect+correct))


# In[4]:





# In[7]:



            
        


# In[8]:


print("Classification Accuracy is "+ str(correct/(incorrect+correct)))


# In[ ]:





# In[ ]:




