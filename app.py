from flask import Flask, jsonify
from flask import request
from test import load_model, predict_sample
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins":"*"}})

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/predict", methods=['POST'])
def predict():
    text = request.form['text']
    model = request.form['model']
    result, prob = predict_sample(model, text)
    return jsonify({"Hasil Sentimen":result}, {"Nilai positive":prob[1]}, {"Nilai negative":prob[0]})

if __name__ == '__main__':
    app.run(debug=True, port=8900)