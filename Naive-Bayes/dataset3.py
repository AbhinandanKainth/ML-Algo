#!/usr/bin/env python
# coding: utf-8

# In[10]:


import csv
f=open('Desktop/HW3/dataset3.csv')
csv_f=csv.reader(f)
data=[]
for rows in csv_f:
    data.append(rows)
    #print(rows)
data[0][0]=4
print(len(data[0]))


# In[17]:


def check(data,index):
    D1=0;D3=0;D2=0;D4=0
    for rows in data:
        if(rows[35]=='D1'):
            D1+=1
        if(rows[35]=='D2'):
            D2+=1
        if(rows[35]=='D3'):
            D3+=1
        if(rows[35]=='D4'):
            D4+=1
    D11=[0]*(len(data[0])-1)
    D12=[0]*(len(data[0])-1)
    D13=[0]*(len(data[0])-1)
    D14=[0]*(len(data[0])-1)
    D15=[0]*(len(data[0])-1)
    D16=[0]*(len(data[0])-1)
    D21=[0]*(len(data[0])-1)
    D22=[0]*(len(data[0])-1)
    D23=[0]*(len(data[0])-1)
    D24=[0]*(len(data[0])-1)
    D25=[0]*(len(data[0])-1)
    D26=[0]*(len(data[0])-1)
    D31=[0]*(len(data[0])-1)
    D32=[0]*(len(data[0])-1)
    D33=[0]*(len(data[0])-1)
    D34=[0]*(len(data[0])-1)
    D35=[0]*(len(data[0])-1)
    D36=[0]*(len(data[0])-1)
    D41=[0]*(len(data[0])-1)
    D42=[0]*(len(data[0])-1)
    D43=[0]*(len(data[0])-1)
    D44=[0]*(len(data[0])-1)
    D45=[0]*(len(data[0])-1)
    D46=[0]*(len(data[0])-1)
    for rows in data:
        for i in range(len(rows)-1):
            if rows[i]=='1':
                if(rows[-1]=='D1'):
                    D11[i]+=1
                if(rows[-1]=='D2'):
                    D21[i]+=1
                if(rows[-1]=='D3'):
                    D31[i]+=1
                if(rows[-1]=='D4'):
                    D41[i]+=1
            if rows[i]=='2':
                if(rows[-1]=='D1'):
                    D12[i]+=1
                if(rows[-1]=='D2'):
                    D22[i]+=1
                if(rows[-1]=='D3'):
                    D32[i]+=1
                if(rows[-1]=='D4'):
                    D42[i]+=1
            if rows[i]=='3':
                if(rows[-1]=='D1'):
                    D13[i]+=1
                if(rows[-1]=='D2'):
                    D23[i]+=1
                if(rows[-1]=='D3'):
                    D33[i]+=1
                if(rows[-1]=='D4'):
                    D43[i]+=1
            if rows[i]=='4':
                if(rows[-1]=='D1'):
                    D14[i]+=1
                if(rows[-1]=='D2'):
                    D24[i]+=1
                if(rows[-1]=='D3'):
                    D34[i]+=1
                if(rows[-1]=='D4'):
                    D44[i]+=1
            if rows[i]=='5':
                if(rows[-1]=='D1'):
                    D15[i]+=1
                if(rows[-1]=='D2'):
                    D25[i]+=1
                if(rows[-1]=='D3'):
                    D35[i]+=1
                if(rows[-1]=='D4'):
                    D45[i]+=1
            if rows[i]=='6':
                if(rows[-1]=='D1'):
                    D16[i]+=1
                if(rows[-1]=='D2'):
                    D26[i]+=1
                if(rows[-1]=='D3'):
                    D36[i]+=1
                if(rows[-1]=='D4'):
                    D46[i]+=1


    if(data[index][-1]=="D1"):
        D1-=1
        for i in range(len(rows)-1):
            if(data[index][i]=='1'):
                D11[i]-=1
            if(data[index][i]=='2'):
                D12[i]-=1
            if(data[index][i]=='3'):
                D13[i]-=1
            if(data[index][i]=='4'):
                D14[i]-=1
            if(data[index][i]=='5'):
                D15[i]-=1
            if(data[index][i]=='6'):
                D16[i]-=1
    if(data[index][-1]=="D2"):
        D2-=1
        for i in range(len(rows)-1):
            if(data[index][i]=='1'):
                D21[i]-=1
            if(data[index][i]=='2'):
                D22[i]-=1
            if(data[index][i]=='3'):
                D23[i]-=1
            if(data[index][i]=='4'):
                D24[i]-=1
            if(data[index][i]=='5'):
                D25[i]-=1
            if(data[index][i]=='6'):
                D26[i]-=1
    if(data[index][-1]=="D3"):
        D3-=1
        for i in range(len(rows)-1):
            if(data[index][i]=='1'):
                D31[i]-=1
            if(data[index][i]=='2'):
                D32[i]-=1
            if(data[index][i]=='3'):
                D33[i]-=1
            if(data[index][i]=='4'):
                D34[i]-=1
            if(data[index][i]=='5'):
                D35[i]-=1
            if(data[index][i]=='6'):
                D36[i]-=1
    if(data[index][-1]=="D4"):
        D4-=1
        for i in range(len(rows)-1):
            if(data[index][i]=='1'):
                D41[i]-=1
            if(data[index][i]=='2'):
                D42[i]-=1
            if(data[index][i]=='3'):
                D43[i]-=1
            if(data[index][i]=='4'):
                D44[i]-=1
            if(data[index][i]=='5'):
                D45[i]-=1
            if(data[index][i]=='6'):
                D46[i]-=1
                
    pD1=D1
    pD2=D2
    pD3=D3
    pD4=D4
    
    
    for i in range(len(rows)-1):
        if(data[index][i]=='1'):
            pD1*=D11[i]/D1
            pD2*=D21[i]/D2
            pD3*=D31[i]/D3
            pD4*=D41[i]/D4
        if(data[index][i]=='2'):
            pD1*=D12[i]/D1
            pD2*=D22[i]/D2
            pD3*=D32[i]/D3
            pD4*=D42[i]/D4
        if(data[index][i]=='3'):
            pD1*=D13[i]/D1
            pD2*=D23[i]/D2
            pD3*=D33[i]/D3
            pD4*=D43[i]/D4
        if(data[index][i]=='4'):
            pD1*=D14[i]/D1
            pD2*=D24[i]/D2
            pD3*=D34[i]/D3
            pD4*=D44[i]/D4
        if(data[index][i]=='5'):
            pD1*=D15[i]/D1
            pD2*=D25[i]/D2
            pD3*=D35[i]/D3
            pD4*=D45[i]/D4
        if(data[index][i]=='6'):
            pD1*=D16[i]/D1
            pD2*=D26[i]/D2
            pD3*=D36[i]/D3
            pD4*=D46[i]/D4
    if(max(pD1,pD2,pD3,pD4)==pD1):
        if(data[index][-1]=='D1'):
            return True
        else:
            return False
    if(max(pD1,pD2,pD3,pD4)==pD2):
        if(data[index][-1]=='D2'):
            return True
        else:
            return False
    if(max(pD1,pD2,pD3,pD4)==pD3):
        if(data[index][-1]=='D3'):
            return True
        else:
            return False
    if(max(pD1,pD2,pD3,pD4)==pD4):
        if(data[index][-1]=='D4'):
            return True
        else:
            return False
    
    
        
        


# In[18]:


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




