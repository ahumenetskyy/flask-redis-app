import os
import json
import redis

from flask import Flask
from flask import request

HOST = os.environ.get('REDIS_HOST')
PORT = os.environ.get('REDIS_PORT')

app = Flask(__name__)
app.debug = True
db = redis.Redis(host=HOST, port=PORT)

@app.route('/', methods = ['POST', 'GET'])
def home():
    if (request.method == 'POST'):
        db.mset(request.json)
        return json.dumps(request.json), 201
    return json.dumps([f"{k.decode('utf-8')}: {db.get(k).decode('utf-8')}" for k in db.keys()]), 200


if __name__ == "__main__":
    print(f'HOST = {HOST}, PORT={PORT}')
    app.run()
