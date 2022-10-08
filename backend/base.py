from flask import Flask, send_file
from dotenv import load_dotenv
from getData import *
from makeGraph import saveGraph

load_dotenv()

app = Flask(__name__)

@app.route('/data')
def getData():

    responseBody = pullData(internal=False)

    return responseBody

@app.route('/graph')
def getGraph():
    saveGraph()
    return send_file('test.png')

@app.route('/profit')
def getProfit():
    return {'profit': countProfit()}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)