#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
f=open('Desktop/HW3/dataset5.csv')
csv_f=csv.reader(f)
data=[]
for rows in csv_f:
    data.append(rows)
data[0][0]='1'


# In[20]:


def check(data):
    monk11=[0]*7
    monk12=[0]*7
    monk13=[0]*7
    monk14=[0]*7
    monk01=[0]*7
    monk02=[0]*7
    monk03=[0]*7
    monk04=[0]*7
    monk1=0
    monk0=0
    for rows in data:
        if(rows[0]=='1'):
            monk1+=1
        else:
            monk0+=1
    for rows in data:
        for i in range(1,7):
            if(rows[i]=='1'):
                if(rows[0]==1):
                    monk11[i]+=1
                else:
                    monk01[i]+=1
            if(rows[i]=='2'):
                if(rows[0]==1):
                    monk12[i]+=1
                else:
                    monk02[i]+=1
            if(rows[i]=='3'):
                if(rows[0]==1):
                    monk13[i]+=1
                else:
                    monk03[i]+=1
            if(rows[i]=='4'):
                if(rows[0]==1):
                    monk14[i]+=1
                else:
                    monk04[i]+=1
    incorrect=0
    correct=0
    f=open('Desktop/HW3/dataset5test.csv')
    csv_f=csv.reader(f)
    test=[]
    for rows in csv_f:
        test.append(rows)
    test[0][0]='1'
    for rows in test:
        p1=monk1
        p0=monk0
        for i in range(1,7):
            if(rows[i]=='1'):
                p0*=monk01[i]
                p1*=monk11[i]
            if(rows[i]=='2'):
                p0*=monk02[i]
                p1*=monk12[i]
            if(rows[i]=='3'):
                p0*=monk03[i]
                p1*=monk13[i]
            if(rows[i]=='4'):
                p0*=monk04[i]
                p1*=monk14[i]
        if(p1>=p0):
            if(rows[0]=='1'):
                correct+=1
            else:
                incorrect+=1
        else:
            if(rows[0]=='0'):
                correct+=1
            else:
                incorrect+=1
    print(correct/(correct+incorrect))
    
    


# In[21]:


check(data)


# In[ ]:





# In[ ]:




