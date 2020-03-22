from flask import Flask,jsonify
import pymongo
import json
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["ippool"]
    mycol = mydb["sixsixip"]
    a = random.sample([i for i in mycol.find()],1)[0]
    del a['_id']
    return jsonify(a)
    

if __name__ == '__main__':
    app.run()