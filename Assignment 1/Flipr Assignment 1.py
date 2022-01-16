#Importing Pymongo For Connection To MongoDB
from pymongo import MongoClient
#Importing Flask And JSON
from flask import Flask, request, render_template
import json

#Initializing API
app = Flask(__name__)

#Setting The Method To "POST"
@app.route('/assignment1',methods=['POST'])
def assignment1():
        Body=request.form.get("Body")
        Param=request.form.get("Param")
        Query=request.form.get("Query")
        #Connecting to MongoDB
        client = MongoClient(Body)
        #Initializing Concox Database
        db  = client['__CONCOX__']
        #Initializing Devices Collection
        c1  = db[Param]
        #Initializing status Collection
        c2  = db[Query]
        #Sorting For Latest 30 Devices
        temp=c1.find().sort('createdAt',1)
        arr1=[]
        #Storing the Latest 30 Devices
        for i in temp :
            arr1.append(i)
            if(len(arr1)==30):
                break
        dict1=dict()
        #Custom Headers
        dict1['Name']="Khush Advani"
        dict1['Contact']="khushadvani2@gmail.com"
        #Matching The IMEI Numbers In Both Collections And Getting The Coordinates Then Appending Them To Dictionary dict1
        for i in arr1:
            dict1[i['imei']]=[]
            c=0
            for j in c2.find({'imei':i['imei']}).sort('createdAt',1):
                 if(c==50):
                     break
                 elif j['gps']!=None and len(j['gps'])==2:
                     dict1[i['imei']].append(j['gps'])
                     c+=1
        for i in dict1:
                if (i!='Name' and i!='Contact'):
                    dict1[i]=dict1[i][::-1]
        #Returning The Answer In JSON Format
        return json.dumps(dict1)
#Running The Application
app.run()
