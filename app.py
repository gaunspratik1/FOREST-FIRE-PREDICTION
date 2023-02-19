import pickle
from flask import Flask,request, jsonify
import pymongo

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

@app.route('/predict_bulk_mongoDB',methods=['POST'])
def predict_bulk_mongoDB():

    client = pymongo.MongoClient("mongodb+srv://gaunspratik1:pymongo_1@cluster0.dczyoah.mongodb.net/?retryWrites=true&w=majority")
    db2 = client['FIRE']
    fire_coll = db2['fire_collection']
    j = []

    data1 = request.json['data']
    limit = list(data1.values())[0]
    print(limit)
    for i in fire_coll.find().limit(limit):
        raw_values = list(i.values())
        raw_values.pop(0)
        j.append(raw_values)

    print(j)
    output_bulk = model.predict(j)

    #return jsonify(output_bulk)
    return str(output_bulk)


if __name__=="__main__":
    app.run(debug=True)
