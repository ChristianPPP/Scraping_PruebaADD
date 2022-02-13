#!/usr/bin/env python
# coding: utf-8

#In[0]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
import pymongo 
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
            doc = dbs.insert_one(dictTweet)
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
mongo=pymongo.MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
db=mongo['twitter_mongo']
dbs=db['data']
    
    
#In[3]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
#Búsqueda por filtro llamdando al método filter
twitter_stream.filter(track=["Mandelbrot","set","Fractal"])