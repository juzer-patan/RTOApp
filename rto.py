#!/usr/bin/python3 

print("Content-type:text/html")
print("Access-Control-Allow-Origin:*")
print() 

import cgi
import json

data = cgi.FieldStorage() 
num = data.getvalue("number")

file1 = open("info.json") 
    
# Reading from file 
filej = file1.read() 
    
file1.close()

df = json.loads(filej)
df1 = json.loads(df['Vehicle']['vehicleJson'])

jsonop = json.dumps(df1) 

print(jsonop)
