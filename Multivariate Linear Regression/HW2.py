import csv
import random
import math
from itertools import combinations
from numpy.linalg import inv
from numpy import asarray
import numpy


#opening of reader file
f = open('m3.csv')
csv_f = csv.reader(f)

#creating a list of rows
mdata=[]
for rows in csv_f:
	mdata.append(rows)
ans=[['Combinations','Absolute Error','Root Mean Square Error']] #this global list will store the required answers



def getval(tup): #we have to use the formula ((inp`)(inp)^(-1))(inpw`)Y
	inc=[]
	x=[]
	l80=int(0.80*len(mdata))
	for i in range(l80):
		x=[]
		for j in tup:
			if(not mdata[i][j].isnumeric()):
				x=[]
				continue
			else:
				x.append(float(mdata[i][j]))
		if x!=[]:
			inc.append(x)
	if(len(inc)>1):
		inp=asarray(inc)
		inptranpose = inp.T 
		t=inv(numpy.matmul(inptranpose,inp))
		t1=numpy.matmul(t,inptranpose)
		y=[]
		for i in range(l80):
			y.append(float(mdata[i][20]))
		coeff=numpy.matmul(t1,y)
		
		#done the training and testing on the remaining 20%
		testdata=[];testi=[]
		for i in range(l80,len(mdata)):
			x=[]
			for j in tup:
				if(not mdata[i][j].isnumeric()):
					x=[]
					continue
				else:
					x.append(float(mdata[i][j]))
		if x!=[]:
			testdata.append(x)
		for i in range(l80,len(mdata)):
			testi.append(float(mdata[i][20]))
		er=0
		testdata=asarray(testdata)
		testi=asarray(testi)
		abserror=0;
		for i in range(len(testdata)):
			abserror+=(abs(float(numpy.matmul(testdata[i],coeff))-float(testi[i])))
			er+=(float(numpy.matmul(testdata[i],coeff))-float(testi[i]))**2
		p=[]
		u=[]
		for i in tup:
			if(i==5):
				u.append("SJR")
			if(i==7):
				u.append("H-index")
			if(i==8):
				u.append("Total Docs")
			if(i==9):
				u.append("Total Docs-3yrs")
			if(i==10):
				u.append("Total refs")
			if(i==11):
				u.append("Total cites-3yrs")
			if(i==12):
				u.append("Citable Docs-3 yrs")
			if(i==13):
				u.append("cites,doc 2 yrs")
			if(i==14):
				u.append("ref/docs")
			
				
		p.append(u)
		#p.append("Error i got")
		p.append(float(abserror/len(testdata)))
		p.append(float(er/(len(testdata))))
		ans.append(p)
		return float(er/(len(testdata)))


def main():
	#i-factor(col=20)
	#factors that we have to keep in mind are
	#SJR(col-5),H-index(col-7),Total Docs(col-8)
	#Total Docs-3yrs(col-9),Total refs(col-10),
	#Total Cities-3 yrs(col-11),citable docs-3 yr(col-12)
	#cites(col-13),doc-2yrs(col-14)
	#ref(col-15),doc(col-16) 
	p=[5,7,8,9,10,11,12,13,14]


	#subarrays contains all the possible combinations for the columns 
	subarrays=[]
	#c=0
	#maxe=0
	y=[]
	for i in range(1,len(p)):
		subarrays.append(list(combinations(p,i)))
	print("--------------------")
	for i in range(len(subarrays)):
		for j in range(len(subarrays[i])):	
			x=getval(subarrays[i][j])

	print("Done with no errors :)")
	with open('ans.csv','w',newline='') as w:
		writer = csv.writer(w)
		writer.writerows(ans)

#closing the files
	w.close()
	f = open('ans.csv')
	csv_f = csv.reader(f)

#creating a list of rows
	minerr=99;
	mdata=[]
	for i in csv_f:
		mdata.append(i)
	print("minimum mean error and root mean error")
	for i in range(1,len(mdata)):
		minerr=min(float(mdata[i][2]),minerr)
	for i in range(1,len(mdata)):
		if(minerr==float(mdata[i][2])):
			print(mdata[i])
			break
if __name__ == '__main__':
	main()
