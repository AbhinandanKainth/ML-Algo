#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
f=open('Desktop/HW3/dataset4.csv')
csv_f=csv.reader(f)
data=[]
for rows in csv_f:
    data.append(rows)


# In[20]:


def check(data,index):
    for rows in data:
        for i in range(len(rows)):
            if(rows[i]=='*'):
                rows[i]='1'
    auto=0
    noauto=0
    for rows in data:
        if(rows[0]=='1'):
            noauto+=1
        else:
            auto+=1
    auto1=[0]*7
    auto2=[0]*7
    auto3=[0]*7
    auto4=[0]*7
    noauto1=[0]*7
    noauto2=[0]*7
    noauto3=[0]*7
    noauto4=[0]*7
    for rows in data:
        for i in range(1,len(rows)):
            if(rows[i]=='1' and rows[0]=='1'):
                noauto1[i]+=1
            if(rows[i]=='2' and rows[0]=='1'):
                noauto2[i]+=1
            if(rows[i]=='3' and rows[0]=='1'):
                noauto3[i]+=1
            if(rows[i]=='4' and rows[0]=='1'):
                noauto4[i]+=1
            if(rows[i]=='1' and rows[0]=='2'):
                auto1[i]+=1
            if(rows[i]=='2' and rows[0]=='2'):
                auto2[i]+=1
            if(rows[i]=='3' and rows[0]=='2'):
                auto3[i]+=1
            if(rows[i]=='4' and rows[0]=='2'):
                auto4[i]+=1
    correct=0
    incorrect=0
    pwin=auto
    ploss=noauto
    if(data[index][0]=="1"):
        auto-=1
        for i in range(1,len(rows)):
            if(data[index][i]=='1'):
                auto1[i]-=1
            if(data[index][i]=='2'):
                auto2[i]-=1
            if(data[index][i]=='3'):
                auto3[i]-=1
            if(data[index][i]=='4'):
                auto4[i]-=1
    if(data[index][0]=="0"):
        noauto-=1
        for i in range(1,len(rows)):
            if(data[index][i]=='1'):
                noauto1[i]-=1
            if(data[index][i]=='2'):
                noauto2[i]-=1
            if(data[index][i]=='3'):
                noauto3[i]-=1
            if(data[index][i]=='4'):
                noauto4[i]-=1
            
    for i in range(1,len(rows)):
        if(data[index][i]=='1'):
            ploss*=noauto1[i]/noauto
            pwin*=auto1[i]/auto
        if(data[index][i]=='2'):
            ploss*=noauto2[i]/noauto
            pwin*=auto2[i]/auto
        if(data[index][i]=='3'):
            ploss*=noauto3[i]/noauto
            pwin*=auto3[i]/auto
        if(data[index][i]=='4'):
            ploss*=noauto4[i]/noauto
            pwin*=auto4[i]/auto
        
    if(pwin>ploss):
        if(data[index][0]=="1"):
            return False
        else:
            return True
    if(pwin<ploss):
        if(data[index][0]=="0"):
            return False
        else:
            return True
                
#     incorrect=0
#     correct=0
#     for rows in data:
#         pauto=auto
#         pnoauto=noauto
#         for i in range(1,len(rows)):
#             if(rows[i]=='1'):
#                 pauto*=auto1[i]
#                 pnoauto*=noauto1[i]
#             if(rows[i]=='2'):
#                 pauto*=auto2[i]
#                 pnoauto*=noauto2[i]
#             if(rows[i]=='3'):
#                 pauto*=auto3[i]
#                 pnoauto*=noauto3[i]
#             if(rows[i]=='4'):
#                 pauto*=auto4[i]
#                 pnoauto*=noauto4[i]
#         if(pauto>pnoauto):
#             if(rows[0]=='2'):
#                 correct+=1
#             else:
#                 incorrect+=1
#         else:
#             if(rows[0]=='1'):
#                 correct+=1
#             else:
#                 incorrect+=1
    #print(correct)
    #print(incorrect)


# In[21]:


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


# In[ ]:




