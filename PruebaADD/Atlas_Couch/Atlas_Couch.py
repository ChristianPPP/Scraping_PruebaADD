#!/usr/bin/env python
# coding: utf-8

#In[0]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
#Link de la base de datos de couchdb
URL = 'http://admin:agujeronegro@127.0.0.1:5984'
print(URL)
#Verificación de la conexión
try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('CouchDB connection: Success')
    if response.status_code == 401:
        print('CouchDB connection: failed', response.json())
except requests.ConnectionError as e:
    raise e

server=couchdb.Server(URL)
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
#Link de la base de datos de mongo atlas
CLIENT = MongoClient('mongodb+srv://admin:agujeronegro@cluster0.21fzo.mongodb.net/test?authSource=admin&replicaSet=atlas-r7j9yh-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
#Verificación de la conexión
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)


DBS=['couch_atlas']


try:
    dbc=server.create('atlas_couch')
except:
    dbc=server['atlas_couch']
    
#Bucle for que ejecutará los qery desde mongodb atlas para extraer los documentos de la base de datos 
#una vez extraidos se contruye un nuevo documento que serà alamcenado en couchdb
for db in DBS:
    if db not in ('admin', 'local','config'):  
        cols = CLIENT[db].list_collection_names()  
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try:
                    
                    documents=json.loads(json_util.dumps(x))
                    documents["_id"]=str(documents["_id"]["$oid"])
                    print(documents)
                    doc=dbc.save(documents)
                except TypeError as t:
                    print('current document raised error: {}'.format(t))
                    SKIPPED.append(x)  # creating list of skipped documents for later analysis
                    continue    # continue to next document
                except Exception as e:
                    raise e