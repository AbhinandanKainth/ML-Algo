def check(data,test):
    wins=0
    loss=0;
    for rows in data:
        if(rows[9]=='positive'):
            wins+=1
        if(rows[9]=='negative'):
            loss+=1
    #print("Probability of winning: ")
    #print(wins/len(data))
    #print(loss/len(data))
#     for rows in data:
#         print(rows)
    winx=[0]*9
    lossx=[0]*9
    #print(winx)
    for rows in data:
        for i in range(9):
            if(rows[i]=='x' and rows[9]=='positive'):
                winx[i]+=1;
            if(rows[i]=='x' and rows[9]=='negative'):
                lossx[i]+=1;

#     for i in range(9):
#         print("probability that the player wins and X is present at " + str(i+1) + " position")
#         print(winx[i]/wins)
#     for i in range(9):
#         print("probability that the player losses and X is present at " + str(i+1) + " position")
#         print(lossx[i]/loss)
    wino=[0]*9
    losso=[0]*9
    #print(winx)
    for rows in data:
        for i in range(9):
            if(rows[i]=='o' and rows[9]=='positive'):
                wino[i]+=1;
            if(rows[i]=='x' and rows[9]=='negative'):
                losso[i]+=1;

#     for i in range(9):
#         print("probability that the player wins and O is present at " + str(i+1) + " position")
#         print(wino[i]/wins)
#     for i in range(9):
#         print("probability that the player losses and O is present at " + str(i+1) + " position")
#         print(losso[i]/loss)
    winb=[0]*9
    lossb=[0]*9
    #print(winx)
    for rows in data:
        for i in range(9):
            if(rows[i]=='b' and rows[9]=='positive'):
                winb[i]+=1;
            if(rows[i]=='b' and rows[9]=='negative'):
                lossb[i]+=1;

#     for i in range(9):
#         print("probability that the player wins and B is present at " + str(i+1) + " position")
#         print(winb[i]/wins)
#     for i in range(9):
#         print("probability that the player losses and B is present at " + str(i+1) + " position")
#         print(lossb[i]/loss)
    #print(len(data))
    winbayes=0
    lossbayes=0
    correct=0
    incorrect=0
    pwin=wins
    ploss=loss
    print(len(data))
    for i in range(9):
        if(test[i]=='x'):
            ploss*=lossx[i]/loss
            pwin*=winx[i]/wins
        if(test[i]=='o'):
            ploss*=losso[i]/loss
            pwin*=wino[i]/wins
        if(test[i]=='b'):
            ploss*=lossb[i]/loss
            pwin*=winb[i]/wins
    if(pwin>ploss):
        if(test[9]=="positive"):
            return True
        else:
            return False
    if(pwin<ploss):
        if(test[9]=="negative"):
            return True
        else:
            return False


def main():
	import csv
	f=open('Tic-Tac.csv')
	csv_f=csv.reader(f)
	data=[]
	for rows in csv_f:
	    data.append(rows)
	data[0][0]='x'
	correct=0
	incorrect=0
	size=len(data)
	#print(size)
	for i in range(size):
	    a=data.pop(0)
	    print(len(data))
	    n=check(data,a)
	    #print(a)
	    if(n==True):
	        correct+=1
	    elif(n==False):
	        incorrect+=1
	    data.append(a)
	    #print(len(data))
	print(correct/(incorrect+correct))

if __name__ == '__main__':
	main()