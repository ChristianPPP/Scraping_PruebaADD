#!/usr/bin/env python
# coding: utf-8

#In[0]
#  Copyright (c) 2022.
#  Realizado por: 
#  All rights reserved.
import couchdb
import csv
#Link de la base de datos de couchdb
couch = couchdb.Server('http://admin:agujeronegro@127.0.0.1:5984')
db = couch['tiktok_couch']
#In[2]
#  Copyright (c) 2022.
#  Realizado por: Poleth Arias - Christian Palacios 
#  All rights reserved.
#Lectura del archivo .json
with open('C:\\Users\\Christian Palacios\\Desktop\\PruebaADD\\tiktok_scraping\\mandelbrotset_1644689454267.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    #Bucle para la construcción del documento a partir de la informaciòn del archivo
    for row in reader:
        doc = {
            "id": row['id'],
            "secretID": row['secretID'],
            "text": row['text'],
            "createTime": row['createTime'],
            "authorMeta.id": row['authorMeta.id'],
            "authorMeta.secUid": row['authorMeta.id'],
            "authorMeta.name": row['authorMeta.name'],
            "authorMeta.nickName": row['authorMeta.nickName'],
            "authorMeta.verified": row['authorMeta.verified'],
            "authorMeta.signature": row['authorMeta.signature'],
            "authorMeta.avatar": row['authorMeta.avatar'],
            "authorMeta.following": row['authorMeta.following'],
            "authorMeta.fans": row['authorMeta.fans'],
            "authorMeta.heart": row['authorMeta.heart'],
            "authorMeta.video": row['authorMeta.video'],
            "authorMeta.digg": row['authorMeta.digg'],
            "musicMeta.musicId": row['musicMeta.musicId'],
            "musicMeta.musicName": row['musicMeta.musicName'],
            "musicMeta.musicAuthor": row['musicMeta.musicAuthor'],
            "musicMeta.musicOriginal": row['musicMeta.musicOriginal'],
            "musicMeta.musicAlbum": row['musicMeta.musicAlbum'],
            "musicMeta.playUrl": row['musicMeta.playUrl'],
            "musicMeta.coverThumb": row['musicMeta.coverThumb'],
            "musicMeta.coverMedium": row['musicMeta.coverMedium'],
            "musicMeta.coverLarge": row['musicMeta.coverLarge'],
            "musicMeta.duration": row['musicMeta.duration'],
            "covers.default": row['covers.default'],
            "covers.origin": row['covers.origin'],
            "covers.dynamic": row['covers.dynamic'],
            "webVideoUrl": row['webVideoUrl'],
            "videoUrl": row['videoUrl'],
            "videoUrlNoWaterMark": row['videoUrlNoWaterMark'],
            "videoApiUrlNoWaterMark": row['videoApiUrlNoWaterMark'],
            "videoMeta.height": row['videoMeta.height'],
            "videoMeta.width": row['videoMeta.width'],
            "videoMeta.duration": row['videoMeta.duration'],
            "diggCount": row['diggCount'],
            "shareCount": row['shareCount'],
            "playCount": row['playCount'],
            "commentCount": row['commentCount'],
            "downloaded": row['downloaded'],
            "mentions": row['mentions'],
            "hashtags": row['hashtags'],
            "effectStickers": row['effectStickers']
        }
        db.save(doc)
        print("Saved")