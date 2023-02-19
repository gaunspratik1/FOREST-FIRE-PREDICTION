import pickle
from flask import Flask,request, jsonify
from sql_pakage.sql import database_connect
import pandas as pd
from mongo_pkg.mongo_fire import database_connect_mongoDB

app = Flask(__name__)
model = pickle.load(open('model_classification.pkl', 'rb'))

@app.route('/predict_api',methods=['POST'])
def predict_api():

    data=request.json['data']
    print(list(data.values()))
    new_data=[list(data.values())]
    output=model.predict(new_data)[0]
    output1 = float(output)
    if output1 == -1:
        fire = 'No Fire'
    else:
        fire = 'Fire'
    return jsonify(fire)

@app.route('/predict_bulk',methods=['POST'])
def predict_bulk():

    data1 = request.json['data']
    limit = list(data1.values())[0]
    bulk_data = database_connect(limit)
    print(bulk_data)
    v = []
    for i in bulk_data:
        c = list(i)
        v.append(c)
    print(v)
    output_bulk = model.predict(v)

    print(output_bulk)
    #return jsonify(output_bulk)
    return str(output_bulk)

@app.route('/predict_bulk_mongoDB',methods=['POST'])
def predict_bulk_mongoDB():

    data1 = request.json['data']
    limit = list(data1.values())[0]
    bulk_data = database_connect_mongoDB(limit)
    print(bulk_data)
    output_bulk = model.predict(bulk_data)

    print(output_bulk)
    #return jsonify(output_bulk)
    return str(output_bulk)


if __name__=="__main__":
    app.run(debug=True)
