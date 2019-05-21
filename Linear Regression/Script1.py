import csv
import random
import math

#opening of reader file
f = open('m1.csv')
csv_f = csv.reader(f)

#creating a list of rows and shuffling it
templist=[]
for rows in csv_f:
	templist.append(rows)
random.shuffle(templist)

#calculating correlation for 100%
sumhi=0.0;sumh=0.0;sumi=0.0;sumh2=0.0;sumi2=0.0;n=len(templist)
for i in range(len(templist)):
	sumhi = sumhi + float(templist[i][1])*float(templist[i][2])
	sumh = sumh + float(templist[i][1])
	sumi = sumi + float(templist[i][2])
	sumh2 = sumh2 + float(templist[i][1])**2
	sumi2 = sumi2 + float(templist[i][2])**2
r = (n*(sumhi)-sumh*sumi)/(math.sqrt(n*sumh2-(sumh**2))*math.sqrt(n*sumi2-(sumi**2)))
print("correlation for the journals data " + str(r))


#taking top 80% data and storing the rest in a list
rest20=[]
count=len(templist)
for i in range(int(0.20*count)):
	rest20.append(templist.pop(-1))


#calculating regression for the 80% removing their values from sumh1 h2 etc.
#training data
for i in range(len(rest20)):
	sumh-=float(rest20[i][1])
	sumi-=float(rest20[i][2])
	sumh2-=float(rest20[i][1])**2
	sumi2-=float(rest20[i][2])**2
	sumhi-=float(rest20[i][1])*float(rest20[i][2])
	n=n-1
print("S.D of the h index "+ str(math.sqrt(sumh2/n)))
print("S.D of the i index "+ str(math.sqrt(sumi2/n)))
print("Regresion line for the i index on h index ")
r = (n*(sumhi)-sumh*sumi)/(math.sqrt(n*sumh2-(sumh**2))*math.sqrt(n*sumi2-(sumi**2)))
a=r*math.sqrt(sumi2/n)/math.sqrt(sumh2/n)
print("a = "+ str(a))
b=sumi/n-a*sumh/n
print("b = "+str(b))


#Test Data
error=0
for i in range(len(rest20)):
	h=float(rest20[i][1])
	initialI=float(rest20[i][2])
	predictedI= a*h + b
	error += (predictedI - initialI)**2
print("prediciting the impact factor for the rest 20% data we get error")
print(math.sqrt(error/len(rest20))) 

f.close()

#Using the regression line obtained we will now predict impact factor of conferences 
f = open('Conferences_organised.csv')
csv_f = csv.reader(f)
count=0
ans=[['Name','H-Index','Impact Factor']]

for row in csv_f:
	if(count!=0):  #skipping first line because it contains name of the columns
		hindex=row[7]
		if(hindex.isnumeric()):
			hindex=float(row[7])
			predictedindex=a*hindex + b
			temp=[]
			temp.append(row[2])
			temp.append(row[7])
			temp.append(predictedindex)
			ans.append(temp)
	count+=1



with open('m2.csv','w',newline='') as w:
	writer = csv.writer(w)
	writer.writerows(ans)

#closing the files
w.close()
