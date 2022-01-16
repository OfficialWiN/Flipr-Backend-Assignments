#Importing Pymongo for connection to MongoDB
from pymongo import MongoClient                                                        
#Importing Flask
from flask import Flask, request, render_template                                      
#Importing JSON & Requests
import json                                                                             
import requests                                                                         

#Initializing the API
app = Flask(__name__)                                                                   

#Initializing the method to "POST"
@app.route('/assignment2',methods=['POST'])                                             
def assignment2():
        #Initializing the url used for getting the coordinates
        url="https://maps.googleapis.com/maps/api/geocode/json?"
        #Entering the API Key
        api_key="AIzaSyA5bwbEsAOUMOI4RK2zXcIayG4vjuQSpcw"
        #Getting The Addresses From JSON File
        address=request.get_json()["address"] 
        ans=[]
        #Iterating For Each Address 
        for place in address :
            #Initializing A Dictonary To Store Address And Coordinates
            result=dict()
            #Requesting The Google API For Coordinates
            res_ob = requests.post(url + 'address=' + place + '&key=' + api_key)
            geometry=res_ob.json()['results'][0]['geometry']
            #Getting The Latitude
            lat=geometry['location']['lat']
            #Getting The Longitiude
            long=geometry['location']['lng']
            #Initializing 'add' And 'location' As Keys & place And [lat,long] As Their Values
            result['add']=place
            result['location']=[lat,long]
            #Appending The result To ans List For The Desired Format Of Output
            ans.append(result)
        #Returning The Answer In JSON Format
        return json.dumps(ans)
#Running The Application
app.run()
