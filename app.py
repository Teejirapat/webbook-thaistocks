import json, config
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.data)
    data = json.loads(request.data)

if __name__ == "__main__" : 

	app.run(host="0.0.0.0",port=8082,debug=False)