from flask import Flask, jsonify
import requests


topic = 'pizza'

r = requests.get(f'https://newsdata.io/api/1/latest?apikey=pub_544362d61bffc435f9c61e041dff5d3bc0e4d&q={topic}')

app = Flask(__name__)

@app.route('/')
def get_api():
    response = {'result': r.json()}
    return jsonify(response)

app.run(port=5000)