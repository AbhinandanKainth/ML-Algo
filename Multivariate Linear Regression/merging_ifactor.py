import csv
import random
import math
from itertools import combinations

#opening of reader file #m2.csv names of the journals and their attributes other then i-factor,
f = open('m2.csv')
csv_f = csv.reader(f)

m2=[]
for rows in csv_f:
	m2.append(rows)
f.close() #list m2 now contains all the content of m2.csv

f = open('m1.csv') #m1 files contains the i-factor of the journals
csv_f = csv.reader(f)
m1=[]
for rows in csv_f:
	m1.append(rows)	#list m1 contains the data from m1.csv(journals.txt)
f.close()


c=0
mdata=[]
for i in range(len(m2)):
	for j in range(len(m1)):
		if m2[i][2].lower() == m1[j][0].lower():
			c+=1
			print(c)
			t=[]
			m2[i].append(m1[j][2])
			t.append(m2[i])
			mdata.extend(t)
print(mdata)	#mdata contains the merged data.

with open('m3.csv','w',newline='') as w:
	writer = csv.writer(w)
	writer.writerows(mdata)

#closing the files
w.close()
