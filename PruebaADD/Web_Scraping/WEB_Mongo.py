#!/usr/bin/env python
# coding: utf-8

#In[0]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
from bs4 import BeautifulSoup
import requests
import pymongo

#In[1]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
client= pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
nombredb=client['web']
db=nombredb['webscraping']

#In[0]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
urlBase = "https://apkamp.com/es/uk.org.jakebakermaths.mandelandroid"
maxPages = 20
counter = 0
for i in range(1,maxPages):

    # Construyo la URL
    if i > 1:
        url = "%spage/%d/" %(urlBase,i)
    else:
        url = urlBase

    # Realizamos la petición a la web
    req = requests.get(url)
    # Comprobamos que la petición nos devuelve un Status Code = 200
    statusCode = req.status_code
    if statusCode == 200:

        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text)

        # Obtenemos todos los divs donde estan las entradas
        entradas = html.find_all('div',{'class':'topic-bg'})

        # Recorremos todas las entradas para extraer la fecha y tema 
        for entrada in entradas:
            counter += 1
            fecha = entrada.find('div', {'class' : 'info-img-dt'}).getText()
            tema = entrada.find('div', {'class' : 'topic-tip-name'}).getText()
            

            # Imprimo la Fecha y Tema de las entradas
            print ("%d - %s  |  %s  " %(counter,fecha,tema))
            doc={
                "fecha":fecha,
                "tema":tema
            }
            db.insert_one(doc)

    else:
        # Si ya no existe la página y me da un 400
        break