from faker import Faker
from flask import Flask, flash,session,jsonify
app = Flask(__name__)

@app.route('/datos',methods=['GET'])
def datos():
    fake = Faker()
    lista = list()
    for _ in range(13):
        data = dict()
        data["first_name"] = fake.first_name()
        data["day_of_month"] = fake.day_of_month()
        data["day_of_week"] = fake.day_of_week()
        data["country"] = fake.country()
        data["word"] = fake.word()
        lista.append(data)
    return jsonify(lista)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)