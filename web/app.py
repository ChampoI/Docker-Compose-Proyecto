from flask import Flask, flash,session,jsonify,render_template
import requests
import json
app = Flask(__name__)



def datos():
    url = "http://api-fastapi/registros_falsos"
    response = requests.get(url)
    response_json = json.loads(response.text)
    return response_json
@app.route('/',methods=['GET'])
def index():
    response_json = datos()
    return render_template('index.html',datos=response_json["data"])

@app.route('/crear_datos',methods=['GET'])
def crear_datos():
    url = "http://api-fastapi/registros_falsos"
    response = requests.get(url)
    response_json = json.loads(response.text)
    return render_template('index.html',datos=response_json["data"])

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)