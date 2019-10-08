from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
import json
import numpy as np 
from sortedcontainers import SortedDict
from flask import jsonify

app=Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def home():
    return "<h1>IOT Project</h1><h2>Trust Evaluation using Cosine similarity for nodes in Body Area Network.</h2>"

@app.route("/trustevaluation",methods=['POST'])
def calculateTrust():
    if request.headers['Content-Type']=='application/json':
        d=json.dumps(request.json)
    d=json.loads(d)
    vector=[]
    n=d['nodes']#getting the number of nodes

    for i in range(0,n):
        temp=np.random.randint(0,10,n)
        vector.append(temp)
    cosinedictionary={}

    for i in range(0,n+1):
        for j in range(i+i,n):
            res=np.dot(vector[i],vector[j])
            cosinedictionary[res]=[i,j]

    #print(cosinedictionary)

    numberofuntrystablenodes=np.random.randint(1,n-(n%3))
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
    l=[]
    for key,value in trustvaluedictres.items():
        if count!=numberofuntrystablenodes:
            print("untrustable node ",value," Trustfactor :",key)
            a="untrustable node "+str(value)+" Trustfactor :"+str(key)
            l.append(a)
            count=count+1
        else:
            break
    return jsonify(l)



if __name__=="__main__":
    app.run(debug=True)
