#!/usr/bin/env python
# coding: utf-8

#In[0]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
from facebook_scraper import get_posts
import pymongo
import time

#In[1]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
client= pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")#conexion base de datos
db=client['facebook']
dat=db['the_mandelbrot_set']

#In[2]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
i=1
for post in get_posts('themandelbrotset', pages=10, extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']
        dat.insert_one(doc)

    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))