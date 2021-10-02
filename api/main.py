from fastapi import FastAPI
from typing import Optional
import uvicorn
from db import engine,connection_db,conn
from sqlalchemy import func, select
import requests
import json

app = FastAPI()

from models import *
@app.get('/crear_registros')
def crear_registros():
    url = 'http://api-faker/datos'
    response = requests.get(url)
    response_json = json.loads(response.text)
    for i in response_json:
        new_data = {"first_name":i["first_name"],"country":i["country"],"day_of_month":i["day_of_month"],"day_of_week":i["day_of_week"],"word":i["word"]}
        with engine.connect() as con:
            con.execute(datos_falsos.insert().values(new_data))
    return {'data':"Registros creados"}

@app.get('/registros_falsos')
def registros_falsos():
    with engine.connect() as con:
        obtener_data = "select * from datos_falsos"
        respuesta_data = con.execute(obtener_data)
        lista = list()
        for i in respuesta_data:
            data = dict()
            data["first_name"] = i[1]
            data["day_of_month"] = i[2]
            data["day_of_week"] = i[3]
            data["country"] = i[4]
            data["word"] = i[5]
            lista.append(data)
        return {'data':lista}

@app.get('/eliminar_registros')
def eliminar_registros():
    with engine.connect() as con:
        eliminar_data = "delete from datos_falsos"
        try:
            respuesta_data = con.execute(eliminar_data)
        except:
            return {"respuesta":"Data no eliminada , validar "}        
        return {"respuesta":"Data Eliminada"}
