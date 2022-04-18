from flask import Flask
import requests
import json


app = Flask(__name__)


app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/hworld', methods=['GET'])
def hello():
    return "Hello, World!"

@app.route('/info', methods=['GET'])


def info():
    url = "https://freegeoip.app/json"
    response = requests.request("GET", url)
    return  json.dumps(json.loads(response.text), indent=2)   


#if __name__ == '__main__':
#    app.run(debug=True, port=8000)
