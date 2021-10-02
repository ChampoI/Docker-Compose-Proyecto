from flask import Flask, flash,session,jsonify,render_template,redirect,url_for
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

@app.route('/crear_datos',methods=['GET','POST'])
def crear_datos():
    url = "http://api-fastapi/crear_registros"
    response = requests.get(url)
    response_json = json.loads(response.text)
    return redirect(url_for('index'))

@app.route('/eliminar_datos',methods=['GET','POST'])
def eliminar_datos():
    url = "http://api-fastapi/eliminar_registros"
    response = requests.get(url)
    response_json = json.loads(response.text)
    return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)