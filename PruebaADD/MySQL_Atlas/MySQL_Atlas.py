#!/usr/bin/env python
# coding: utf-8

#In[0]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
import mysql.connector
import pymongo
#Links de mongo atlas para establecer la conexión con la base de datos 
mongodb_host = "mongodb+srv://admin:agujeronegro@cluster0.21fzo.mongodb.net/test?authSource=admin&replicaSet=atlas-r7j9yh-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
mongodb_dbname = "mysql_atlas"
#Configuración del cliente de MySQL, credenciales, host y base de datos
mysqldb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Agujeronegro1',
    db='mongo_mysql'
)
#Ejecución del query que nos permitirá extraer los datos de la base de datos de MySQL
mycursor = mysqldb.cursor(dictionary=True)
mycursor.execute("SELECT * from data;")
myresult = mycursor.fetchall()
#Conexión  con la base de datos de mongo atlas
myclient = pymongo.MongoClient(mongodb_host)
mydb = myclient[mongodb_dbname]
mycol = mydb["data"]
#Inserción de los datos extraídos
if len(myresult) > 0:
        x = mycol.insert_many(myresult)
        print(len(x.inserted_ids))