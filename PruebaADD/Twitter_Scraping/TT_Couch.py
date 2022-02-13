#!/usr/bin/env python
# coding: utf-8

#In[0]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
import couchdb
import tweepy 
import json
#Declaración de keys y tokens
ckey = 'SKepyS4uZlyBmXV9xtxQP9hN8'
csecret = '02DIS0kb8qGJpRAd1YfFn89Pmw73gSUGBVPJMWu5B8CD46rYNp'
atoken = '115946548-UmysCzkNSMsbdUqad25NO2TlV6KodCfBjJ2RjMDJ'
asecret = 'Lx1VT6yVeC2b3eQPmfyBMhQwKjViObqYZ6tF8dnUcJQU7'
'''
API key: SKepyS4uZlyBmXV9xtxQP9hN8
API secret key: 02DIS0kb8qGJpRAd1YfFn89Pmw73gSUGBVPJMWu5B8CD46rYNp
Access token: 115946548-UmysCzkNSMsbdUqad25NO2TlV6KodCfBjJ2RjMDJ
Access token secret: Lx1VT6yVeC2b3eQPmfyBMhQwKjViObqYZ6tF8dnUcJQU7
'''
#In[1]
#  Copyright (c) 2022.
#  Realizado por:
#  All rights reserved.
#Clase que se encarga de obtener los datos desde la API de Twitter
class listener(tweepy.Stream):
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = dbs.save(dictTweet)
            print("SAVED" + str(doc) + "=>" + str(data))
        except:
            print("Already exist")
            pass
        return True
    
    def on_error(self, status):
        print(status)
        
        

#In[2]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
twitter_stream = listener(ckey, csecret, atoken, asecret)
#Declaración de las varibles para la conexión con la base de datos
couch = couchdb.Server('http://admin:agujeronegro@127.0.0.1:5984')
try:
    dbs = couch['twitter_couch']
except:
    dbs = couch['twitter_couch']
    
    
#In[3]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
#Búsqueda por filtro llamdando al método filter
twitter_stream.filter(track=["Mandelbrot","set","Fractal"])