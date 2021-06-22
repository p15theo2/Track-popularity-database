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
with open('alltracks.csv', 'w', newline='') as f_handle:
    writer = csv.writer(f_handle)
    # Add the header/column names
    header = ['track_title','artist_name','track_id']
    writer.writerow(header)
    # Iterate over `data`  and  write to the csv file
    for row in results:
        writer.writerow(row)




