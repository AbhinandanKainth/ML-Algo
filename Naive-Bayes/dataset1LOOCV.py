#!/usr/bin/env python
# coding: utf-8

# In[21]:


import csv
f=open('Desktop/HW3/Tic-Tac.csv')
csv_f=csv.reader(f)
data=[]
for rows in csv_f:
    data.append(rows)
data[0][0]='x'


# In[22]:


def check(data,index):
    wins=0
    loss=0;
    for rows in data:
        if(rows[9]=='positive'):
            wins+=1
        if(rows[9]=='negative'):
            loss+=1

    winx=[0]*9
    lossx=[0]*9
    #print(winx)
    for rows in data:
        for i in range(9):
            if(rows[i]=='x' and rows[9]=='positive'):
                winx[i]+=1;
            if(rows[i]=='x' and rows[9]=='negative'):
                lossx[i]+=1;

    wino=[0]*9
    losso=[0]*9
    #print(winx)
    for rows in data:
        for i in range(9):
            if(rows[i]=='o' and rows[9]=='positive'):
                wino[i]+=1;
            if(rows[i]=='o' and rows[9]=='negative'):
                losso[i]+=1;

    winb=[0]*9
    lossb=[0]*9
    #print(winx)
    for rows in data:
        for i in range(9):
            if(rows[i]=='b' and rows[9]=='positive'):
                winb[i]+=1;
            if(rows[i]=='b' and rows[9]=='negative'):
                lossb[i]+=1;

    winbayes=0
    lossbayes=0
    correct=0
    incorrect=0
    pwin=wins
    ploss=loss
    if(data[index][9]=="positive"):
        wins-=1
        for i in range(9):
            if(data[index][i]=='x'):
                winx[i]-=1
            if(data[index][i]=='o'):
                wino[i]-=1
            if(data[index][i]=='b'):
                winb[i]-=1
    if(data[index][9]=="negative"):
        loss-=1
        for i in range(9):
            if(data[index][i]=='x'):
                lossx[i]-=1
            if(data[index][i]=='o'):
                losso[i]-=1
            if(data[index][i]=='b'):
                lossb[i]-=1
            
    for i in range(9):
        if(data[index][i]=='x'):
            ploss*=lossx[i]/loss
            pwin*=winx[i]/wins
        if(data[index][i]=='o'):
            ploss*=losso[i]/loss
            pwin*=wino[i]/wins
        if(data[index][i]=='b'):
            ploss*=lossb[i]/loss
            pwin*=winb[i]/wins
    if(pwin>ploss):
        if(data[index][9]=="positive"):
            return True
        else:
            return False
    if(pwin<ploss):
        if(data[index][9]=="negative"):
            return True
        else:
            return False


# In[ ]:


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




