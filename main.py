from flask import Flask,json
import pymongo
import os

app = Flask(__name__)

client = pymongo.MongoClient(os.environ.get("URL",None))
db = client.resume

@app.route('/')
def root():
    return "Hello World"

@app.route('/<id>')
def getUser(id):
    doc = db["resume"].find_one({'userId': id})
    if doc == None:
        return json.jsonify({'error': 'User doesn\'t exist' }), 404
    else:
        return json.jsonify(doc)

if __name__ == '__main__':
  app.run(host="0.0.0.0")
