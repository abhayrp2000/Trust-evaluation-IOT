import numpy as np 
from sortedcontainers import SortedDict
n=int(input("Please enter number of nodes"))

vector=[]

for i in range(0,n):
    temp=np.random.randint(0,10,n)
    vector.append(temp)
cosinedictionary={}

for i in range(0,n+1):
    for j in range(i+i,n):
        res=np.dot(vector[i],vector[j])
        cosinedictionary[res]=[i,j]

#print(cosinedictionary)

numberofuntrystablenodes=np.random.randint(1,3)
trustfactor={}

nodecombinationdict={}
def remove_duplicatenodecombination():
    for key,value in cosinedictionary.items():
        if value not in nodecombinationdict.values():
            nodecombinationdict[key]=value

remove_duplicatenodecombination()

def calculate_similarity():
    for i in range(0,n):
        sum=0
        for key,value in nodecombinationdict.items():
            if int(value[0])==i or int(value[1]==i):
                sum=sum+key

        trustfactor[sum]=i

calculate_similarity()

result=SortedDict(trustfactor)

factorsum=0
for key,value in result.items():
    factorsum=factorsum+key

#calculating the final trust factor of all the nodes and printing it
trustvaluedictres={}
for key,value in result.items():
    trustvaluedictres[key/factorsum]=value


print(trustvaluedictres)

count=0
for key,value in trustvaluedictres.items():
    if count!=numberofuntrystablenodes:
        print("untrustable node ",value," Trustfactor :",key)
        count=count+1
    else:
        break