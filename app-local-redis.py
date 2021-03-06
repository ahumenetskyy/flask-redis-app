import json
import redis

from flask import Flask
from flask import request

app = Flask(__name__)
app.debug = True
db = redis.Redis(db=1)

@app.route('/', methods = ['POST', 'GET'])
def home():

    if (request.method == 'POST'):
        db.mset(request.json)
        return json.dumps(request.json), 201
    return json.dumps([f"{k.decode('utf-8')}: {db.get(k).decode('utf-8')}" for k in db.keys()]), 200


if __name__ == "__main__":
    app.run()
