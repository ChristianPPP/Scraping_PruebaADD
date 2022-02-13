#!/usr/bin/env python
# coding: utf-8

#In[0]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
import pymongo
#Conexión a la base de datos de mongo
mongo = pymongo.MongoClient('mongodb+srv://admin:agujeronegro@cluster0.21fzo.mongodb.net/test')
db = mongo['couch_atlas']
dbs = db['data']
i=0
#Lectura del archivo .json para construir un documento y almacenarlo en la base de datos
with open('C:\\Users\\PruebaADD\\couch_atlas\\couch_atlas.json') as json:
    for row in json:
        doc = {str(i): str(row)}
        dbs.insert_one(doc)
        i = i + 1
        print("Saved")