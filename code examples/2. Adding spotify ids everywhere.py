#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials('0ac98a8f556a46f48024c6cde776c1b0','fbf695854344424e9539c05bbae31ad3')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
dtf = pd.read_csv('alltracks.csv')
#removing all parethesis
dtf['track_title']= dtf['track_title'].str.replace(r"\(.*\)","")
mask = (dtf['track_id'].str.len()<22)  | (dtf['track_id'].str.len()>22)
dtf.loc[mask, 'track_id'] = "no-id"
dtf['track_id'].value_counts().nlargest(20)
for index, row in dtf.iterrows():
    if(row['track_id']=="no-id"):
        search = sp.search(q="track:"+row['track_title']+" artist:"+row['artist_name'], type='track',limit=1)
        try:
            trid = search['tracks']['items'][0]['id']
            row['track_id']=trid
        except:
            print("no id for"+row['track_title'])
dtf.to_csv("tracks+features-uncleaned.csv",index=False)
dtf=dtf[dtf.track_id!='no-id']
dtf = dtf.drop_duplicates(subset=['track_id'])
dtf.to_csv("tracksandspotifyids-cleaned.csv",index=False)


