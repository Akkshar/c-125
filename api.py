from flask import Flask, jsonify, request
from model import getpreddata

app = Flask(__name__)
@app.route("/predict-digit", methods = ["POST"])

def apidigitpred():
    image = request.files.get("digit")
    predict = getpreddata(image)
    return jsonify({
        "prediction": predict
    }), 200

if __name__ == "__main__":
    app.run(debug = True)