from flask import Flask
import pymongo
import os

app = Flask(__name__)

client = pymongo.MongoClient(os.environ.get("URL",None))
db = client.resume

@app.route('/')
def root():
    return "Hello World"

if __name__ == '__main__':
  app.run(host="0.0.0.0")
