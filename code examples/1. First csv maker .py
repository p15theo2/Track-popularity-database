#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import mysql.connector as sql
import csv

def printque(querry):
    db = sql.connect(
    host = 'localhost',
    user= 'spiros',
    passwd = '2224',
    database = "popularity")
    cursor = db.cursor()
    cursor.execute(querry)
    print(cursor.fetchall())
    
    
def returnque(querry):
    db = sql.connect(
    host = 'localhost',
    user= 'spiros',
    passwd = '2224',
    database = "popularity")
    res=[]
    cursor = db.cursor()
    cursor.execute(querry)
    return cursor.fetchall()
results = returnque("""SELECT track.title,artist.name,track.id_video FROM track
                        LEFT JOIN  artist_track ON track.id = artist_track.track_id 
                         LEFT JOIN artist ON artist_track.artist_id = artist.id""")
results = returnque("""SELECT tr.title ,date_format(spo.date,"%Y-%c-%d"),spo.position FROM spotify_rating spo 
                       left JOIN track tr 
                       on spo.track_id = tr.id;""")
results = returnque("""SELECT tr.id_video,tr.title,ar.name,date_format(spo.date,"%Y-%c-%d"),spo.position
                       from spotify_rating spo
                       left join track tr on spo.track_id = tr.id
                       left join artist_track on tr.id = artist_track.track_id 
                       left join artist ar on artist_track.artist_id = ar.id;""")
with open('alltracks.csv', 'w', newline='') as f_handle:
    writer = csv.writer(f_handle)
    # Add the header/column names
    header = ['track_title','artist_name','track_id']
    writer.writerow(header)
    # Iterate over `data`  and  write to the csv file
    for row in results:
        writer.writerow(row)




