#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('SpotifyAudioFeaturesNov2018.csv')
df = df.drop(df[df.popularity > 3].index)
df = df.drop_duplicates(subset=['track_id'])
df.rename(columns={'popularity':'On_chart','track_name':'track_title'}, inplace=True)

df = df[['track_title','artist_name','track_id','duration_ms','energy','key','mode','time_signature','acousticness','danceability','instrumentalness','liveness','loudness','speechiness','valence','tempo','On_chart']]

df['On_chart'] = 0
df2 = pd.read_csv("famouscomplete.csv")


bigdata = pd.concat([df,df2], ignore_index=True, sort =False)

bigdata.to_csv("complete.csv",index=False)

